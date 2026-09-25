from django.urls import path, re_path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import sitemaps # Importăm dicționarul creat mai sus


urlpatterns = [
    path("", views.index, name="index"),
    path("info/", views.info, name="info"),
    path("pag1", views.pag1, name="f"),
    path("pag2", views.pag2, name="g"),
    re_path(r'^pag_cod/(?P<data>\d{3})/$', views.afis_cod),
    path('log/', views.log, name='log'),
    path('despre/', views.despre, name='despre'),
    path('carti/', views.carti, name='carti'),
    # path('categorii/<slug:slug_categorie>/', views.categorie_detail, name='categorie_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('cos_virtual/', views.in_lucru, name='cos_virtual'),
    path('carti/<int:pk>/', views.carte_detail, name='carte_detail'),
    path('categorii/<slug:slug_categorie>/', views.categorie_detail, name='categorie_detail'),
    path('adauga_carte/', views.adauga_carte, name='adauga_carte'),
    path('inregistrare/', views.inregistrare_view, name='inregistrare'),
    path('schimbare-parola/', views.schimbare_parola_view, name='password_change'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profil/', views.profil_view, name='profil'),
    path('confirma_mail/<str:cod>/', views.confirma_mail, name='confirma_mail'),
    path('promotii/', views.promotii_view, name='promotii'),
    path('promotie_succes/', views.promotie_succes_view, name='promotie_succes'),
    path('interzis/', views.pagina_interzisa_test, name='interzis'),
    path('aloca-oferta/', views.aloca_permisiune_oferta, name='aloca_permisiune_oferta'),
    path('oferta-speciala/', views.pagina_oferta, name='pagina_oferta'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
