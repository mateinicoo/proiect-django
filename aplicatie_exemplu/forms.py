from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta 
from django.forms.widgets import HiddenInput
from .models import Carte, Categorie
from django.core.mail import mail_admins
from django.utils.html import strip_tags
from .models import CustomUser
from datetime import date
from django import forms
import re



INPUT_CLASS = 'form-control'

class FiltrareProduseForm(forms.Form):
    
    elemente_per_pagina = forms.IntegerField(
        required=False, 
        label='Elemente pe pagină', 
        min_value=1,
        max_value=100, 
        widget=forms.NumberInput(attrs={'placeholder': 'Implicit 8', 'class': INPUT_CLASS})
    )
    
    titlu = forms.CharField(
        required=False, 
        label='Titlu', 
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Căutare după titlu', 'class': INPUT_CLASS})
    )
    
    autor = forms.CharField(
        required=False, 
        label='Autor', 
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Căutare după autor', 'class': INPUT_CLASS})    
    )

    
    
    pret_min = forms.DecimalField(
        required=False, 
        label='Preț Minim', 
        min_value=0,
        error_messages={'min_value': 'Prețul minim nu poate fi negativ.'},
        widget=forms.NumberInput(attrs={'placeholder': 'Min', 'class': INPUT_CLASS})
    )
    
    pret_max = forms.DecimalField(
        required=False, 
        label='Preț Maxim', 
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'Max', 'class': INPUT_CLASS})
    )


    
    categorie = forms.ModelChoiceField(
        required=False,
        label='Categorie',
        queryset=Categorie.objects.all(),
        empty_label="Toate Categoriile",
        widget=forms.Select(attrs={'class': INPUT_CLASS})   
    )
        
    def clean_titlu(self):
            titlu = self.cleaned_data.get('titlu')
            
            if titlu and len(titlu) < 2:
                raise forms.ValidationError(
                    "Te rog, introdu minim 2 caractere pentru căutarea după titlu."
                )
            return titlu
        
        
    def clean(self):
            cleaned_data = super().clean()
            
            pret_min = cleaned_data.get('pret_min')
            pret_max = cleaned_data.get('pret_max')
            
            if pret_min is not None and pret_max is not None:
                if pret_min > pret_max:
                    self.add_error(
                        'pret_max', 
                        "Prețul maxim nu poate fi mai mic decât prețul minim! Te rog corectează intervalul."
                    )
                    
            return cleaned_data
        
        
    def __init__(self, *args, **kwargs):
        only_category_id = kwargs.pop('only_category_id', None)
        
        super().__init__(*args, **kwargs)

        if only_category_id is not None:
            
            self.fields['categorie'].initial = only_category_id
            
            self.fields['categorie'].widget.attrs['disabled'] = 'disabled'
            
            self.fields['categorie'].required = False

    

    

def validate_text_general(value):
    if not value: return 
    if not re.match(r'^[A-ZȘȚÂÎ][a-zșțâîA-ZȘȚÂÎ\s-]*$', value):
        raise ValidationError("Textul trebuie să înceapă cu literă mare și să conțină doar litere, spații și cratime.")

def validate_nume_prenume_format(value):
    if not value: return
    if re.search(r'[\s-][a-zșțâî]', value):
        raise ValidationError("După spațiu sau cratimă trebuie să urmeze o literă mare.")

def validate_no_links(value):
    if "http://" in value.lower() or "https://" in value.lower():
        raise ValidationError("Textul nu poate conține link-uri (http/https).")

def validate_cnp_format(value):
    if not value.isdigit():
        raise ValidationError("CNP-ul trebuie să conțină doar cifre.")
    if value[0] not in '1256':
        raise ValidationError("CNP-ul trebuie să înceapă cu 1, 2, 5 sau 6.")
    
    try:
        an = int(value[1:3])
        luna = int(value[3:5])
        zi = int(value[5:7])
        secol = 1900 if value[0] in '12' else 2000
        date(secol + an, luna, zi)
    except ValueError:
        raise ValidationError("Data extrasă din CNP nu este validă.")

def validate_major(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError("Trebuie să aveți minim 18 ani pentru a trimite acest mesaj.")

def validate_email_domain(value):
    forbidden_domains = ['guerillamail.com', 'yopmail.com']
    domain = value.split('@')[-1].lower()
    if domain in forbidden_domains:
        raise ValidationError(f"Domeniul {domain} nu este acceptat (e-mail temporar).")

def validate_mesaj_continut(value):
    cuvinte = re.findall(r'\w+', value)
    if not (5 <= len(cuvinte) <= 100):
        raise ValidationError(f"Mesajul trebuie să conțină între 5 și 100 de cuvinte. (Acum are {len(cuvinte)})")
    
    for cuvant in cuvinte:
        if len(cuvant) > 15:
            raise ValidationError(f"Cuvântul '{cuvant}' este prea lung (maxim 15 caractere).")


class ContactForm(forms.Form):
    TIPURI_MESAJ = [
        ('neselectat', 'Neselectat'),
        ('reclamatie', 'Reclamație'),
        ('intrebare', 'Întrebare'),
        ('review', 'Review'),
        ('cerere', 'Cerere'),
        ('programare', 'Programare'),
    ]

    nume = forms.CharField(
        max_length=10,
        validators=[validate_text_general, validate_nume_prenume_format],
        error_messages={'required': 'Numele este obligatoriu.'}
    )
    
    prenume = forms.CharField(
        max_length=10,
        required=False,
        validators=[validate_text_general, validate_nume_prenume_format]
    )
    
    cnp = forms.CharField(
        min_length=13, max_length=13,
        required=False,
        validators=[validate_cnp_format]
    )
    
    data_nasterii = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        validators=[validate_major]
    )
    
    email = forms.EmailField(validators=[validate_email_domain])
    confirmare_email = forms.EmailField()
    
    tip_mesaj = forms.ChoiceField(choices=TIPURI_MESAJ, initial='neselectat')
    
    subiect = forms.CharField(
        max_length=100,
        validators=[validate_text_general, validate_no_links]
    )
    
    zile_asteptare = forms.IntegerField(min_value=1, max_value=30)
    
    mesaj = forms.CharField(
        widget=forms.Textarea,
        label="Mesaj (vă rugăm să vă și semnați la final)",
        validators=[validate_mesaj_continut, validate_no_links]
    )

    def clean(self):
            cleaned_data = super().clean()
            
            email = cleaned_data.get("email")
            confirmare = cleaned_data.get("confirmare_email")
            nume = cleaned_data.get("nume")
            mesaj = cleaned_data.get("mesaj")
            tip = cleaned_data.get("tip_mesaj")
            zile = cleaned_data.get("zile_asteptare")
            cnp = cleaned_data.get("cnp")
            data_nasterii = cleaned_data.get("data_nasterii")

            if email and confirmare and email != confirmare:
                self.add_error('confirmare_email', "Adresele de e-mail nu coincid. Vă rugăm să verificați.")

            if mesaj and nume:
                cuvinte_mesaj = re.findall(r'\w+', mesaj)
                if cuvinte_mesaj:
                    ultimul_cuvant = cuvinte_mesaj[-1]
                    if ultimul_cuvant.lower() != nume.lower():
                        self.add_error('mesaj', f"Trebuie să vă semnați la finalul mesajului cu numele '{nume}'.")

            if zile and tip:
                if tip in ['review', 'cerere'] and zile < 4:
                    self.add_error('zile_asteptare', "Pentru acest tip de mesaj (review/cerere), minimul este de 4 zile.")
                elif tip in ['cerere', 'intrebare'] and zile < 2:
                    self.add_error('zile_asteptare', "Pentru acest tip de mesaj (cerere/întrebare), minimul este de 2 zile.")
            
            
            if cnp and data_nasterii and len(cnp) == 13:
                an_cnp = int(cnp[1:3])
                luna_cnp = int(cnp[3:5])
                zi_cnp = int(cnp[5:7])
                
                secol = 1900 if cnp[0] in '12' else 2000
                an_complet_cnp = secol + an_cnp
                
                if (data_nasterii.year != an_complet_cnp or 
                    data_nasterii.month != luna_cnp or 
                    data_nasterii.day != zi_cnp):
                    self.add_error('cnp', "Data nașterii din CNP nu coincide cu data nașterii selectată.")

            #Preprocesari


            data_nasterii = cleaned_data.get('data_nasterii')
            if data_nasterii:
                diff = relativedelta(date.today(), data_nasterii)
                cleaned_data['varsta_text'] = f"{diff.years} ani și {diff.months} luni"

            mesaj = cleaned_data.get('mesaj')
            if mesaj:
                mesaj = mesaj.replace('\n', ' ')
                mesaj = re.sub(r'\s+', ' ', mesaj).strip()

                def capitalize_match(match):
                    return match.group(1) + match.group(2).upper()
                
                mesaj = re.sub(r'([.!?]+\s+)([a-zșțâî])', capitalize_match, mesaj)
                mesaj = mesaj[0].upper() + mesaj[1:] if mesaj else mesaj
                cleaned_data['mesaj'] = mesaj

            tip = cleaned_data.get('tip_mesaj')
            zile = cleaned_data.get('zile_asteptare')
            urgent = False

            if tip and zile:
                minim_zile = 1 
                if tip in ['review', 'cerere']: minim_zile = 4
                elif tip in ['intrebare']: minim_zile = 2
                
                if zile == minim_zile:
                    urgent = True
            
            cleaned_data['urgent'] = urgent

            return cleaned_data
        
        


def validate_fara_simboluri_speciale(value):
    if re.search(r'[@#$%^&*()_+={}\[\]]', value):
        raise ValidationError("Textul conține simboluri interzise (@#$% etc.).")

def validate_fara_litere(value):
    valoare_str = str(value)
    if re.search(r'[a-zA-Z@#$%^&*()_+={}\[\]]', valoare_str):
        raise ValidationError("Pretul nu poate conține litere sau simboluri interzise (@#$% etc.).")


def validate_nu_e_doar_cifre(value):
    valoare_str = str(value)
    if valoare_str.isdigit():
        raise ValidationError("Acest câmp nu poate conține doar cifre.")


class CarteModelForm(forms.ModelForm):
    pret_furnizor = forms.DecimalField(
        max_digits=10, 
        decimal_places=2,
        label="Preț Furnizor (RON)",
        help_text="Prețul de achiziție de la editură/distribuitor.",
        error_messages={'required': 'Introdu prețul de achiziție pentru a calcula prețul final.'}
    )
    
    taxa_transport = forms.DecimalField(
        max_digits=10, 
        decimal_places=2,
        label="Cost Transport",
        help_text="Costul logistic per unitate.",
        initial=0
    )

    class Meta:
        model = Carte
        fields = ['ISBN', 'titlu', 'id_editura', 'autor', 'categorie']
        
        labels = {
            'ISBN': 'Codul ISBN al Cărții',
            'id_editura': 'Editura Parteneră'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titlu'].validators.extend([validate_fara_simboluri_speciale, validate_nu_e_doar_cifre])
        self.fields['pret_furnizor'].validators.append(validate_fara_litere)

    def clean_ISBN(self):
        isbn = self.cleaned_data.get('ISBN')
        if len(str(isbn)) < 10:
            raise ValidationError("Un cod ISBN valid trebuie să aibă cel puțin 10 cifre.")
        return isbn

    def clean_titlu(self):
        titlu = self.cleaned_data.get('titlu')
        if "test" in titlu.lower():
            raise ValidationError("Titlul nu poate conține cuvântul 'test'.")
        return titlu

    def clean_taxa_transport(self):
        taxa = self.cleaned_data.get('taxa_transport')
        if taxa < 0:
            raise ValidationError("Taxa de transport nu poate fi negativă.")
        return taxa

    def clean(self):
        cleaned_data = super().clean()
        titlu = cleaned_data.get('titlu')
        editura = cleaned_data.get('id_editura')

        if titlu and editura:
            nume_editura = editura.nume_editura
            if nume_editura.lower() in titlu.lower():
                raise ValidationError(
                    f"Titlul cărții nu trebuie să includă numele editurii ({nume_editura})."
                )
        return cleaned_data
    
    
    
class InregistrareForm(UserCreationForm):
    data_nasterii = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'], 
        label="Data Nașterii"
    )
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'bio', 'data_nasterii', 'telefon', 'oras', 'tip_abonament')

    def clean_oras(self):
        oras = self.cleaned_data.get('oras')
        if oras and not oras[0].isupper():
            raise ValidationError("Numele orașului trebuie să înceapă cu literă mare.")
        return oras

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if bio and len(bio.split()) < 10:
            raise ValidationError("Descrierea bio trebuie să aibă cel puțin 10 cuvinte.")
        return bio

    def clean_data_nasterii(self):
        data = self.cleaned_data.get('data_nasterii')
        from datetime import date
        if data and data > date.today():
            raise ValidationError("Data nașterii nu poate fi în viitor.")
        return data
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username.lower() == 'admin':
            subject = "Cineva incearca sa ne preia site-ul"
            email_suspect = self.data.get('email') 
            
            html_msg = f'<html><body><h1 style="color:red;">{subject}</h1>' \
                       f'<p>Email atacator: {email_suspect}</p></body></html>'
            
            mail_admins(subject, strip_tags(html_msg), html_message=html_msg)
            
            raise forms.ValidationError("Acest username este rezervat sistemului.")
        return username
    
    
    
class LoginFormPersonalizat(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, label="Ține-mă minte (1 zi)")
    
    
    
    
class PromotieForm(forms.Form):
    subiect = forms.CharField(max_length=100)
    mesaj_general = forms.CharField(widget=forms.Textarea)
    nume_promotie = forms.CharField(max_length=100)
    data_expirare = forms.DateTimeField(widget=forms.SelectDateWidget)
    procent_reducere = forms.IntegerField(min_value=1, max_value=99)
    cod_voucher = forms.CharField(max_length=20)
    
    CATEGORII_CU_TEMPLATE = [
        ('fictiune', 'Ficțiune'),
        ('educatie', 'Educație'),
    ]
    categorii = forms.MultipleChoiceField(
        choices=CATEGORII_CU_TEMPLATE,
        widget=forms.CheckboxSelectMultiple,
        initial=[c[0] for c in CATEGORII_CU_TEMPLATE]
    )