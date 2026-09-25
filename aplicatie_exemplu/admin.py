from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Carte
from .models import Editura
from .models import CopieCarte
from .models import Oferta
from .models import Antichitate
from .models import Voucher
from .models import Abonament
from .models import Comanda
from .models import Utilizator
from .models import Autor
from .models import Categorie
from .models import CustomUser
from .models import Vizualizare

admin.site.site_header = "Panou de Administrare Site"
admin.site.index_title = "Bine ai venit în panoul de administrare"
admin.site.site_title = "Site Admin"


class CarteAdmin(admin.ModelAdmin):
    list_display = ('titlu', 'an_publicatie', 'afiseaza_autori')  # afișează câmpurile în lista de obiecte
    list_filter = ('an_publicatie',)  # adaugă filtre laterale
    search_fields = ('titlu',)  # permite căutarea după anumite câmpuri
    empty_value_display = 'nul' # se va afișa cuvântul 'nul; pentru campurile fără valori
    ordering = [ 'titlu', '-ISBN'] #crescator pentru titlu; dar autorii aceleiași cărți în ordine descrescătoare
    list_per_page = 5 # numarul de înregistrări afișate pe pagină
    
    
    fieldsets = (
        ('Informații Generale', {
            'fields': ('titlu', 'autor', 'categorie', 'pret', 'id_editura', 'an_publicatie', 'ISBN')
        }),
        ('Interfata', {
            'fields': ( 'imagine',),
            'classes': ('collapse',),
        }),
    )




class AutorAdmin(admin.ModelAdmin):
    search_fields = ('nume', 'prenume')  

class EdituraAdmin(admin.ModelAdmin):
    search_fields = ('nume_editura',)  

class AntichitateAdmin(admin.ModelAdmin):
    search_fields = ('tip_obiect', )  

class OfertaAdmin(admin.ModelAdmin):
    search_fields = ('titlu', 'procent_reducere') 

class CopieCarteAdmin(admin.ModelAdmin):
    search_fields = ('limba',)  
    
    
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Date Suplimentare', {'fields': ('bio', 'data_nasterii', 'telefon', 'oras', 'tip_abonament', 'cod', 'email_confirmat')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        ('Stare Cont', {'fields': ('blocat',)}),
    )
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Moderatori').exists() and not request.user.is_superuser:
            all_fields = [f.name for f in self.model._meta.fields]
            allowed = ['first_name', 'last_name', 'email', 'blocat']
            return [f for f in all_fields if f not in allowed]
        return self.readonly_fields

    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Vizualizare)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Utilizator)
admin.site.register(Comanda)
admin.site.register(Abonament)
admin.site.register(Voucher)
admin.site.register(Antichitate, AntichitateAdmin)
admin.site.register(Oferta, OfertaAdmin)
admin.site.register(CopieCarte, CopieCarteAdmin)
admin.site.register(Carte, CarteAdmin)
admin.site.register(Editura, EdituraAdmin)
admin.site.register(Categorie)


admin.site.site_header = "Panou de administrare"
admin.site.site_title = "Admin site"
admin.site.site_url = "Bine ai venit in panoul de administrare  "

# Register your models here.
