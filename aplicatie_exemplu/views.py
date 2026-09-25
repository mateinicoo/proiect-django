from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from urllib.parse import unquote, urlparse, parse_qs
from .forms import FiltrareProduseForm, ContactForm, LoginFormPersonalizat, InregistrareForm, PromotieForm
from django.contrib.auth.decorators import login_required
from .models import Accesare, Carte, Categorie, CustomUser, Vizualizare, Promotie
from django.db import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Count, Q
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from datetime import datetime, date
from django.contrib import messages
from django.utils import timezone
from .forms import CarteModelForm
from decimal import Decimal
from django.core.mail import send_mass_mail
from django.template import Template, Context
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.urls import reverse
import uuid
import time
import json
import os
from django.core.mail import mail_admins
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def salvare_accesare(request):
    ip = get_ip(request)
    url_complet = request.build_absolute_uri()
    
    parsed = urlparse(url_complet)
    path_pagina = parsed.path if parsed.path else "/"

    acc = Accesare.objects.create(
        ip_client=ip,
        url=url_complet,
        data=timezone.now(),
        pagina=path_pagina 
    )
    return acc


def log(request):
    if not request.user.groups.filter(name='Administratori_site').exists():
        raise PermissionDenied("Doar administratorii site-ului pot vedea log-urile.")
    
    salvare_accesare(request)

    params = request.GET
    ultimele = params.get("ultimele", None)
    accesari_param = params.get("accesari", None)
    iduri_list = params.getlist("iduri")
    dubluri = params.get("dubluri", "false").lower() == "true"
    tabel = params.get("tabel", None)

    lista_qs = Accesare.objects.all().order_by('-id')

    err_ultimele = None
    
    
    if ultimele is not None:
        if not ultimele.isdigit():
            return HttpResponse("Eroare: parametrul ultimele trebuie sa fie un numar intreg.")
        
        n = int(ultimele)
        k = lista_qs.count() 
        
        if n < k:
            lista_qs = lista_qs[:n] 
        elif n > k:
            err_ultimele = f"Exista doar {k} accesari fata de {n} cerute"

    if iduri_list:
        ids = []
        for batch in iduri_list:
            for val in batch.split(","):
                if val.isdigit():
                    ids.append(int(val))
        
        if not dubluri:
            seen = set()
            ids = [x for x in ids if not (x in seen or seen.add(x))]

        lista_qs = lista_qs.filter(id__in=ids)

    lista = list(lista_qs) 



    total_nr = Accesare.objects.count() if accesari_param == "nr" else None

    accesari_pagini = Accesare.objects.values('pagina').annotate(count=Count('pagina')).order_by('count')
    
    cea_mai_putin = accesari_pagini.first()['pagina'] if accesari_pagini else None
    cea_mai_mult = accesari_pagini.last()['pagina'] if accesari_pagini else None

    
    if tabel:
        if tabel == "tot":
            campuri = ["id", "ip_client", "url", "data", "pagina"]
        else:
            campuri = tabel.split(",") 
    else:
        campuri = None
        
    lista_template = []
    for a in lista:
        lista_template.append({
            "id": a.id,
            "ip_client": a.ip_client,
            "url": a.get_url(),               
            "data": a.get_data_formatata(),  
            "pagina": a.get_pagina_path(),
        })

    return render(request, "log.html", {
        "lista": lista_template, 
        "err_ultimele": err_ultimele,
        "total_nr": total_nr,
        "detalii": accesari_param == "detalii",
        "campuri": campuri,
        "cea_mai_putin": cea_mai_putin,
        "cea_mai_mult": cea_mai_mult,
    })
    
    
def url(request):
    url_complet = request.build_absolute_uri()
    return HttpResponse(url_complet)


def get_ip(request):
    req_headers = request.META
    str_lista_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if str_lista_ip:
        return str_lista_ip.split(',')[-1].strip()
    else:
        return request.META.get('REMOTE_ADDR')


def afis_cod(request,data):
    return HttpResponse(f"<b>Am primit codul:</b> {data}")



def afis_data(request):
    import locale
    from datetime import datetime
    from zoneinfo import ZoneInfo

    locale.setlocale(locale.LC_TIME, "ro_RO.UTF-8")
    romania_tz = ZoneInfo("Europe/Bucharest")

    data = request.GET.get("data")
    acum = datetime.now(romania_tz)
    
    if data == "zi":
        a = acum.strftime("%A, %d %B %Y")
        return a
    if data == "timp":
        a = acum.strftime("Ora: %H Minutul: %M")
        return a

def info(request):
    if not request.user.groups.filter(name='Administratori_site').exists():
        raise PermissionDenied("Acces restricționat la informațiile de sistem.")
    
    
    parametri = request.GET
    numar_parametri = len(parametri)
    nume_parametri = ', '.join(parametri.keys()) if parametri else 'Niciun parametru'

    context = {
        'numar_parametri': numar_parametri,
        'nume_parametri': nume_parametri,
        'ip_utilizator': get_ip(request),
    }

    return render(request, 'info.html', context)

def pag1(request):
    return HttpResponse(2+3)




l=[]
def pag2(request):
    global l
    a=request.GET.get("a",10)
    print(request.GET)
    l.append(a)
    return HttpResponse(f"<b>Am primit</b>: {l}")



def index(request):
    salvare_accesare(request)
    return render(request, 'index.html', {'ip_utilizator': request.META.get('REMOTE_ADDR')})

def despre(request):
    salvare_accesare(request)
    return render(request, 'despre.html', {'ip_utilizator': request.META.get('REMOTE_ADDR')})

def contact(request):
    salvare_accesare(request)
    return render(request, 'contact.html', {'ip_utilizator': request.META.get('REMOTE_ADDR')})




def carti(request):
    salvare_accesare(request)
    
    produse_qs = Carte.objects.all()
    
    form = FiltrareProduseForm(request.GET)
    
    query_params = request.GET.copy() 
    
    nr_elemente = 8

    if form.is_valid():
        data = form.cleaned_data
        
        if data.get('elemente_per_pagina') is not None:
            nr_elemente = data['elemente_per_pagina']
            
            if nr_elemente != 8 and nr_elemente != int(request.session.get('nr_elemente_pagina', 8)):
                 mesajEroare = "În urma repaginării (schimbarea numărului de elemente pe pagină), te rugăm să reselectezi pagina dorită. Este posibil să fi sărit peste unele produse sau să le vezi din nou pe cele deja vizualizate."
                 nrPagina = 1 
                 if 'pagina' in query_params:
                     query_params['pagina'] = 1
        
        request.session['nr_elemente_pagina'] = nr_elemente
        
        if data.get('titlu'):
            produse_qs = produse_qs.filter(titlu__icontains=data['titlu'])
            
        if data.get('autor'):
            produse_qs = produse_qs.filter(autor__icontains=data['autor'])
            
        if data.get('pret_min') is not None:
            produse_qs = produse_qs.filter(pret__gte=data['pret_min']) 
            
        if data.get('pret_max') is not None:
            produse_qs = produse_qs.filter(pret__lte=data['pret_max']) 

        if data.get('categorie'):
            produse_qs = produse_qs.filter(categorie=data['categorie']) 

    
    criteriu_sortare = request.GET.get('sort', 'titlu')
    
    if criteriu_sortare == 'a':
        produse_qs = produse_qs.order_by('titlu')
    elif criteriu_sortare == 'd':
        produse_qs = produse_qs.order_by('-titlu')
    else:
        produse_qs = produse_qs.order_by('-ISBN') 
        
    
    paginator = Paginator(produse_qs, nr_elemente)
    nrPagina = request.GET.get("pagina", 1)
    
    mesajEroare = None

    try:
        obPagina = paginator.page(nrPagina)
    except PageNotAnInteger:
        obPagina = paginator.page(1)
        mesajEroare = "Număr de pagină invalid. Am afișat pagina 1."
    except EmptyPage:
        obPagina = paginator.page(paginator.num_pages)
        mesajEroare = "Pagina cerută nu există. Am afișat ultima pagină."

    if 'pagina' in query_params:
        del query_params['pagina']

    context = {
        'pagina': obPagina,                     
        'eroare': mesajEroare,
        'nrcarti': paginator.count,             
        'sortare_curenta': criteriu_sortare, 
        'categorie_curenta': None,            
        'filtrare_form': form,                   
        'query_params': query_params.urlencode(),
        }
    
    context.update(get_categorii_context())
    
    return render(request, 'carti.html', context)


def carte_detail(request, pk):
    salvare_accesare(request)
    carte = get_object_or_404(Carte, pk=pk) 
    return render(request, 'carte_detail.html', {'carte': carte})




def in_lucru(request):
    salvare_accesare(request)
    return render(request, 'in_lucru.html', {'ip_utilizator': get_ip(request)})


def demo_view(request):
    messages.info(request, "Aplicația a pornit.")
    messages.info(request, "Citire fișier configurare…")


    messages.debug(request, "Initializare module interne…")
    messages.debug(request, "Conexiune DB pe portul 5432.")


    messages.success(request, "Conectare la baza de date realizată cu succes.")
    messages.success(request, "Operația a fost realizată cu succes.")


    messages.warning(request, "Fișierul de configurare este incomplet. Se folosesc valorile implicite.")
    messages.warning(request, "Operație potențial riscantă detectată.")


    messages.error(request, "Parametru lipsă: <db_host>!")
    messages.error(request, "Împărțire la zero detectată!")


    return render(request, "mesage.html")

def redirectionare(request):
    messages.success(request, "Ai fost redirectionat!")
    return redirect('home')


def get_categorii_context():
    try:
        categorii = Categorie.objects.all().order_by('nume')
    except Exception:
        categorii = []
    return {'categorii_menu': categorii}


def categorie_detail(request, slug_categorie):
    salvare_accesare(request)
    categorie = get_object_or_404(Categorie, slug=slug_categorie)
    
    carti_qs = categorie.carti_din_categorie.all() 
    
    query_params = request.GET.copy()
    mesajEroare = None
    nr_elemente_default = 8 
    nr_elemente = nr_elemente_default
    
    
    query_params['categorie'] = categorie.id 
    
    form = FiltrareProduseForm(query_params, only_category_id=categorie.id)
    
    if form.is_valid():
        data = form.cleaned_data
        
        elemente_solicitate = data.get('elemente_per_pagina')
        if elemente_solicitate is not None:
            nr_elemente = elemente_solicitate
        
        nr_elemente_anterior = request.session.get('nr_elemente_pagina_categorie', nr_elemente_default)
        
        if nr_elemente != nr_elemente_anterior:
             mesajEroare = "În urma repaginării (schimbarea numărului de elemente pe pagină), te rugăm să reselectezi pagina dorită. Este posibil să fi sărit peste unele produse sau să le vezi din nou pe cele deja vizualizate."
             nrPagina = 1 
             if 'pagina' in query_params:
                 query_params['pagina'] = 1 
        
        request.session['nr_elemente_pagina_categorie'] = nr_elemente
        
        if data.get('titlu'):
            carti_qs = carti_qs.filter(titlu__icontains=data['titlu'])
            
        if data.get('autor'):
            carti_qs = carti_qs.filter(autor__icontains=data['autor'])

        if data.get('pret_min') is not None:
            carti_qs = carti_qs.filter(pret__gte=data['pret_min'])
            
        if data.get('pret_max') is not None:
            carti_qs = carti_qs.filter(pret__lte=data['pret_max'])

    criteriu_sortare = request.GET.get('sort', 'titlu')
    if criteriu_sortare == 'a':
        carti_qs = carti_qs.order_by('titlu')
    elif criteriu_sortare == 'd':
        carti_qs = carti_qs.order_by('-titlu')
    else:
        carti_qs = carti_qs.order_by('ISBN')

    paginator = Paginator(carti_qs, nr_elemente) 
    
    if 'nrPagina' not in locals():
        nrPagina = request.GET.get("pagina", 1) 
    
    try:
        obPagina = paginator.page(nrPagina)
    except PageNotAnInteger:
        obPagina = paginator.page(1)
        if not mesajEroare:
            mesajEroare = "Număr de pagină invalid. Am afișat pagina 1."
    except EmptyPage:
        obPagina = paginator.page(paginator.num_pages)
        if not mesajEroare:
            mesajEroare = "Pagina cerută nu există. Am afișat ultima pagină."

    if 'pagina' in query_params:
        del query_params['pagina'] 

    context = {
        'pagina': obPagina,
        'eroare': mesajEroare, 
        'nrcarti': paginator.count,
        'sortare_curenta': criteriu_sortare,
        'categorie_curenta': categorie,
        'filtrare_form': form,                      
        'query_params': query_params.urlencode(),    
    }

    context.update(get_categorii_context())

    return render(request, 'carti.html', context)



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            date_mesaj = form.cleaned_data.copy()

            date_mesaj.pop('confirmare_email', None)

            date_mesaj['ip_utilizator'] = get_ip(request)
            date_mesaj['data_ora_sosire'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            timestamp = int(time.time()) 
            status_urgent = "_urgent" if date_mesaj.get('urgent') else ""
            nume_fisier = f"mesaj_{timestamp}{status_urgent}.json"

            cale_folder = os.path.join(os.path.dirname(__file__), 'Mesaje')
            if not os.path.exists(cale_folder):
                os.makedirs(cale_folder)

            cale_completa = os.path.join(cale_folder, nume_fisier)
            
            for cheie, valoare in date_mesaj.items():
                if isinstance(valoare, (date, datetime)):
                    date_mesaj[cheie] = valoare.isoformat()

            with open(cale_completa, 'w', encoding='utf-8') as fisier_json:
                json.dump(date_mesaj, fisier_json, indent=4, ensure_ascii=False)

            return render(request, 'succes.html', {'nume_fisier': nume_fisier})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})




def adauga_carte(request):
    if not request.user.has_perm('aplicatie_exemplu.add_carte'):
        return handler403(request, exception="Nu ai voie să adaugi cărți!")
    
    
    if request.method == 'POST':
        form = CarteModelForm(request.POST)
        if form.is_valid():
            carte = form.save(commit=False)
            
            pret_achizitie = form.cleaned_data.get('pret_furnizor')
            taxa = form.cleaned_data.get('taxa_transport')
            
            carte.pret = (pret_achizitie * Decimal('1.3')) + taxa            
            carte.save()
            
            form.save_m2m()
            
            messages.success(request, f"Cartea '{carte.titlu}' a fost adăugată cu succes în bibliotecă!")
            
            return redirect('adauga_carte')
    else:
        form = CarteModelForm()
    
    return render(request, 'adauga_carte.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginFormPersonalizat(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                messages.debug(request, f"DEBUG: Sesiune creată pentru ID: {user.id}. Backend: {user.backend}")
                messages.debug(request, f"DEBUG: Userul are permisiunile: {list(user.get_all_permissions())}")
                if user.blocat:
                    messages.error(request, "Contul tău a fost blocat. Contactează un administrator.")
                    return render(request, 'login.html', {'form': form})
                
                login(request, user)
                return redirect('index')
            user = form.get_user()
            
            
            request.session['fail_count'] = 0
            if not user.email_confirmat:
                form.add_error(None, "Trebuie să îți confirmi adresa de email înainte de a te loga!")
            else:
                login(request, user)
            
                if form.cleaned_data.get('remember_me'):
                    request.session.set_expiry(86400) 
                else:
                    request.session.set_expiry(0) 

                request.session['user_data'] = {
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'bio': user.bio,
                    'data_nasterii': str(user.data_nasterii) if user.data_nasterii else "Nespecificat", 
                    'telefon': user.telefon,
                    'oras': user.oras,
                    'tip_abonament': user.tip_abonament
                }
                return redirect('profil')
    else:
        acum = datetime.datetime.now()
        last_fail = request.session.get('last_fail_time')
        count = request.session.get('fail_count', 0)

        if last_fail:
            ultima_data = datetime.datetime.fromisoformat(last_fail)
            if (acum - ultima_data).total_seconds() < 120:
                count += 1
            else:
                count = 1 
        else:
            count = 1

        request.session['fail_count'] = count
        request.session['last_fail_time'] = acum.isoformat()

        if count >= 3:
            subject = "Logari suspecte"
            ip = get_ip(request)
            username = request.POST.get('username')
            
            html_msg = f'<html><body><h1 style="color:red;">{subject}</h1>' \
                        f'<p>Username: {username}</p><p>IP: {ip}</p></body></html>'
            
            mail_admins(subject, strip_tags(html_msg), html_message=html_msg)
            request.session['fail_count'] = 0
        form = LoginFormPersonalizat()
    return render(request, 'login.html', {'form': form})

@login_required
def profil_view(request):
    user_info = request.session.get('user_data', {})
    return render(request, 'profil.html', {'user_info': user_info})

def logout_view(request):
    logout(request)
    return redirect('login')


def inregistrare_view(request):
    if request.method == 'POST':
        form = InregistrareForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.cod = str(uuid.uuid4())
            user.is_active = True 
            user.save()
            relative_url = reverse('confirma_mail', kwargs={'cod': user.cod})
            link_confirmare = request.build_absolute_uri(relative_url)
            subiect = 'Confirmare înregistrare site'
            context = {
                'user': user,
                'cod': user.cod,
                'link_confirmare': link_confirmare,
            }
            html_message = render_to_string('email_confirmare.html', context)
            plain_message = strip_tags(html_message)
            
            send_mail(
                subiect,
                plain_message,
                settings.EMAIL_HOST_USER,
                [user.email],
                html_message=html_message,
                fail_silently=True,
            )
            return render(request, 'in_lucru.html')
    else:
        form = InregistrareForm()
    
    return render(request, 'inregistrare.html', {'form': form})


@login_required
def schimbare_parola_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Parola a fost schimbată cu succes!')
            return redirect('profil')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'schimbare_parola.html', {'form': form})


def confirma_mail(request, cod):
    try:
        user = CustomUser.objects.get(cod=cod)
        user.email_confirmat = True
        user.cod = None 
        user.save()
        return render(request, 'confirmare_succes.html', {'mesaj': "Email-ul a fost confirmat cu succes!"})
    except CustomUser.DoesNotExist:
        return render(request, 'confirmare_succes.html', {'mesaj': "Cod invalid sau expirat."})
    
    



def vizualizari_carte(request, isbn):
    carte = get_object_or_404(Carte, ISBN=isbn)
    
    if request.user.is_authenticated:
        Vizualizare.objects.create(utilizator=request.user, produs=carte)
        
        vizualizari = Vizualizare.objects.filter(utilizator=request.user).order_by('-data_vizualizarii')
        if vizualizari.count() > 5:
            id_de_sters = vizualizari.values_list('id', flat=True)[5:]
            Vizualizare.objects.filter(id__in=id_de_sters).delete()
            
    return render(request, 'in_lucru.html', {'carte': carte})





def promotii_view(request):
    if request.method == 'POST':
        form = PromotieForm(request.POST)
        if form.is_valid():
            
            p = Promotie.objects.create(
                nume=form.cleaned_data['nume_promotie'],
                data_expirare=form.cleaned_data['data_expirare'],
                procent_reducere=form.cleaned_data['procent_reducere'],
                cod_voucher=form.cleaned_data['cod_voucher']
            )
            
            subiect = form.cleaned_data['subiect']
            categorii_selectate = form.cleaned_data['categorii']
            datamails = []

            for cat_slug in categorii_selectate:
                utilizatori = CustomUser.objects.filter(
                    vizualizare__produs__categorie__slug=cat_slug
                ).annotate(nr_viz=models.Count('vizualizare')).filter(nr_viz__gte=2).distinct()

                
                try:
                    with open(f'aplicatie_exemplu/templates/email_promotii/{cat_slug}.txt', 'r') as f:
                        template_content = f.read()
                except Exception as e:
                    subject = "Eroare in executia codului"
                    eroare_text = str(e)
                    
                    html_msg = f'<html><body><h1 style="color:red;">{subject}</h1>' \
                            f'<div style="background-color:red; color:white; padding:10px;">' \
                            f'Eroare: {eroare_text}</div></body></html>'
                    
                    mail_admins(subject, strip_tags(html_msg), html_message=html_msg)
                    return render(request, 'eroare_generica.html', {'eroare': "Sistemul de mailuri are o problema."})
                
                t = Template(template_content)
                
                for user in utilizatori:
                    context = Context({
                        'subiect': subiect,
                        'nume': p.nume,
                        'reducere': p.procent_reducere,
                        'voucher': p.cod_voucher,
                        'data_expirare': p.data_expirare,
                        'user': user
                    })
                    mesaj_final = t.render(context)
                    
                    datamails.append((subiect, mesaj_final, settings.EMAIL_HOST_USER, [user.email]))

            send_mass_mail(tuple(datamails), fail_silently=False)
            
            return render(request, 'promotie_succes.html')
    else:
        form = PromotieForm()
    return render(request, 'promotii.html', {'form': form})

def promotie_succes_view(request):
    return render(request, 'promotie_succes.html')



def handler403(request, exception=None):
    nr = request.session.get('nr_403', 0)
    nr += 1
    request.session['nr_403'] = nr
    if nr >= settings.N_MAX_403:
        messages.warning(request, "Atenție! Activitatea ta pare suspectă. Ai accesat prea multe pagini restricționate.")
    elif nr == settings.N_MAX_403 - 1:
        messages.warning(request, "Avertisment: Mai ai o singură încercare înainte de a primi o notificare de securitate.")
    path = request.path
    titlu = "Eroare 403"
    if "adauga_carte" in path:
        titlu = "Eroare adaugare produse"
        
    context = {
        'titlu': titlu,
        'mesaj_personalizat': str(exception) if exception else "Nu aveți permisiunile necesare.",
        'nr_accesari': nr,
        'n_max': settings.N_MAX_403,
    }
    
    
    return render(request, '403.html', context, status=403)

def pagina_interzisa_test(request):
    raise PermissionDenied("Aceasta este o pagină de test pentru eroarea 403.")




def setup_groups(request):
    prod_group, _ = Group.objects.get_or_create(name='Administratori_produse')
    content_type = ContentType.objects.get_for_model(Carte)
    permissions = Permission.objects.filter(content_type=content_type)
    prod_group.permissions.set(permissions)

    site_group, _ = Group.objects.get_or_create(name='Administratori_site')
    site_group.permissions.set(Permission.objects.all())
    
    return HttpResponse("Grupuri configurate!")


@login_required
def aloca_permisiune_oferta(request):
    content_type = ContentType.objects.get_for_model(Promotie)
    permisiune = Permission.objects.get(codename='vizualizeaza_oferta', content_type=content_type)
    
    request.user.user_permissions.add(permisiune)
    
    return redirect('pagina_oferta')


def pagina_oferta(request):
    if not request.user.has_perm('aplicatie_exemplu.vizualizeaza_oferta'):
        return handler403(request, exception="Nu ai voie să vizualizezi oferta.")
    messages.info(request, "Ai primit o ofertă specială de 50%! Verifică secțiunea promoții.")
    return render(request, 'oferta_speciala.html', {'titlu': 'Oferta Ta Speciala'})