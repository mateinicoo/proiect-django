from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from urllib.parse import urlparse, parse_qs
from django.utils.text import slugify
from django.conf import settings
from datetime import date, datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.db import models
from django.urls import reverse

class Accesare(models.Model):
    ip_client = models.CharField(max_length=50, null=True, blank=True)
    url = models.TextField(null=True, blank=True) 
    data = models.DateTimeField(default=timezone.now)
    pagina = models.CharField(max_length=255, db_index=True, null=True, blank=True)

    
    def get_lista_parametri(self):
        if not self.url:
            return []
        parsed = urlparse(self.url)
        query = parse_qs(parsed.query)
        lista = []
        for k, v in query.items():
            lista.append((k, v[0] if v else None)) 
        return lista

    def get_url(self):
        return self.url

    def get_data_formatata(self, format_str="%Y-%m-%d %H:%M:%S"):
        return self.data.strftime(format_str)

    def get_pagina_path(self):
        return self.pagina
    
    def __str__(self):
        return f"[{self.id}] {self.ip_client} — {self.url}"

    class Meta:
        verbose_name_plural = "Accesări"
        
            
class Autor(models.Model):
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100, null=True, blank=True)
    data_nastere = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.prenume:
            return f"{self.prenume} {self.nume}"
        return self.nume
    
class Editura(models.Model):
    nume_editura = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.nume_editura






class Categorie(models.Model):
    nume = models.CharField(max_length=100, unique=True)
    descriere = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, editable=False)

    culoare_hex = models.CharField(
        max_length=7,
        default="#AAAAAA",
        help_text="Cod HEX al culorii (ex: #FF0000)"
    )


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nume)
            original_slug = self.slug
            count = 1
            while Categorie.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{count}"
                count += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nume
        
        

class Carte(models.Model):


    ISBN = models.BigIntegerField(primary_key=True) 
    
    autor = models.ManyToManyField(
        'Autor',
        related_name='carti'
    )
    id_editura = models.ForeignKey(
        'Editura',
        on_delete=models.CASCADE,
        related_name='carti'
    )
    titlu = models.CharField(max_length=100)
    an_publicatie = models.IntegerField(null=True, blank=True)
    pret = models.DecimalField(max_digits=20, decimal_places=2, default=10)
    imagine = models.ImageField(upload_to='documente/', blank=True, null=True)
    categorie = models.ForeignKey(
        'Categorie',
        on_delete=models.SET_NULL, 
        related_name='carti_din_categorie',
        null=True, 
        blank=True
    )

    def afiseaza_autori(self):
            return ", ".join([str(autor) for autor in self.autor.all()])

    afiseaza_autori.short_description = 'Autori'
    
    def __str__(self):
        return self.titlu
    
    def get_absolute_url(self):
        return reverse('carte_detail', kwargs={'pk': self.pk})




 
class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    titlu = models.CharField(max_length=100)
    procent_reducere = models.PositiveIntegerField()

    def __str__(self):
        return f"Oferta {self.id_oferta} - {self.procent_reducere}%   {self.titlu}"

class CopieCarte(models.Model):
    id_copie = models.AutoField(primary_key=True)
    semnat_de_autor = models.BooleanField(default=False)
    observatii = models.CharField(max_length=300, blank=True, null=True)
    limba = models.CharField(max_length=100, default="Romana")
    isbn = models.ForeignKey('Carte', on_delete=models.CASCADE, related_name='copii')
    id_oferta = models.ForeignKey('Oferta', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"Copie {self.id_copie} - Carte {self.isbn.titlu}"


class Antichitate(models.Model):
    TIP_OBIECT = [
        ('vaza', 'Vază'),
        ('tablou', 'Tablou'),
        ('obiect_muzeal', 'Obiect muzeal'),
    ]

    id_antichitate = models.AutoField(primary_key=True)
    tip_obiect = models.CharField(max_length=50, choices=TIP_OBIECT)
    id_oferta = models.ForeignKey('Oferta', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Antichitate {self.id_antichitate} - {self.tip_obiect}"


class Comanda(models.Model):
    id_comanda = models.AutoField(primary_key=True)
    pret = models.DecimalField(max_digits=10, decimal_places=2)
    tip_tranzactie = models.CharField(max_length=50)  # ex: "cumparare" / "inchiriere"
    data_tranzactie = models.DateTimeField(auto_now_add=True)
    adresa = models.CharField(max_length=200)

    id_user = models.ForeignKey(
        'Utilizator', on_delete=models.CASCADE, related_name='comenzi'
    )
    id_antichitate = models.ForeignKey(
        Antichitate, on_delete=models.SET_NULL, null=True, blank=True, related_name='comenzi'
    )
    id_copie = models.ForeignKey(
        CopieCarte, on_delete=models.SET_NULL, null=True, blank=True, related_name='comenzi'
    )

    def __str__(self):
        return f"Comanda #{self.id_comanda} - {self.tip_tranzactie}"



class Utilizator(models.Model):
    id_user = models.AutoField(primary_key=True)
    CNP = models.CharField(max_length=13, unique=True)
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    parola = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    nr_telefon = models.CharField(max_length=15)
    tara = models.CharField(max_length=50)
    judet = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50, blank=True, null=True)
    strada = models.CharField(max_length=100)
    nr_adresa = models.CharField(max_length=10)
    id_comanda = models.ForeignKey(
        Comanda, on_delete=models.SET_NULL, null=True, blank=True, related_name='utilizatori'
    )

    def __str__(self):
        return f"{self.nume} {self.prenume}"

class Abonament(models.Model):
    TIP_ABONAMENT = [
        ('normal', 'Normal'),
        ('Premium', 'Premium'),
        ('Angajat', 'Angajat'),
    ]
    id_abonament = models.AutoField(primary_key=True)
    tip_abonament = models.CharField(max_length=30, choices=TIP_ABONAMENT)
    data_incepere = models.DateField(default=date.today)
    data_expirare = models.DateField(null=True, blank=True)
    procent_reducere = models.PositiveIntegerField()
    id_user = models.ForeignKey(
        Utilizator, on_delete=models.SET_NULL, null=True, blank=True, related_name='abonamente'
    )
    
    
    def __str__(self):
        return f"Abonament {self.tip_abonament}"

class Voucher(models.Model):
    id_voucher = models.AutoField(primary_key=True)
    suma = models.DecimalField(max_digits=10, decimal_places=2)
    data_incepere = models.DateField(default=date.today)
    data_expirare = models.DateField(null=True, blank=True)
    id_user = models.ForeignKey('Utilizator', on_delete=models.CASCADE, related_name='vouchere')

    def __str__(self):
        return f"Voucher #{self.id_voucher}*{self.suma} RON"

def verifica_media_path():
    """Afișează calea absolută a directorului MEDIA_ROOT."""
    calea_absoluta = settings.MEDIA_ROOT
    print(f"\nDjango se așteaptă ca fișierele Media să fie la calea:\n{calea_absoluta}\n")
    
    
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    data_nasterii = models.DateField(null=True, blank=True)
    telefon = models.CharField(
        max_length=10, 
        validators=[RegexValidator(r'^\d{10}$', 'Introduceți un număr de telefon valid (10 cifre).')]
    )
    oras = models.CharField(max_length=100)
    tip_abonament = models.CharField(
        max_length=20, 
        choices=[('basic', 'Basic'), ('premium', 'Premium')],
        default='basic'
    )
    cod = models.CharField(max_length=100, null=True, blank=True)
    email_confirmat = models.BooleanField(default=False)
    blocat = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("poate_bloca_utilizator", "Poate bloca sau debloca utilizatori"),
        ]
    
    
class Vizualizare(models.Model):
    utilizator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produs = models.ForeignKey('Carte', on_delete=models.CASCADE) 
    data_vizualizarii = models.DateTimeField(auto_now_add=True)
    
    
class Promotie(models.Model):
    nume = models.CharField(max_length=100)
    data_creare = models.DateTimeField(auto_now_add=True)
    data_expirare = models.DateTimeField()
    procent_reducere = models.IntegerField() 
    cod_voucher = models.CharField(max_length=20)
    categorii = models.ManyToManyField('Categorie')
    
    class Meta:
        permissions = [
            ("vizualizeaza_oferta", "Poate vedea oferta specială de 50%"),
        ]
        



@receiver(user_logged_out)
def sterge_permisiune_oferta(sender, request, user, **kwargs):
    if user:
        permisiune = Permission.objects.get(codename='vizualizeaza_oferta')
        user.user_permissions.remove(permisiune)