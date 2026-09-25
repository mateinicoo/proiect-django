from django.contrib.sitemaps import Sitemap, GenericSitemap
from django.urls import reverse
from .models import Carte

# 1. Sitemap pentru pagini statice (Index, Contact, Info)
class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        # Returnăm numele rutelelor (name din urls.py) care nu depind de login
        return ['index', 'info', 'contact'] 

    def location(self, item):
        return reverse(item)

# 2. Configurare GenericSitemap pentru modele (Cărți)
# Acesta generează automat link-uri de tipul /carte/id/
info_dict = {
    'queryset': Carte.objects.all(),}

# Dicționarul pe care îl vom pasa în urls.py
sitemaps = {
    'static': StaticViewSitemap,
    'carti': GenericSitemap(info_dict, priority=0.7),
}