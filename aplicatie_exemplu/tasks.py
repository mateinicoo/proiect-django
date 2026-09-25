import logging
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from .models import CustomUser, Accesare, Carte # presupunem că ai modelul Carte
import random

logger = logging.getLogger(__name__)

def sterge_utilizatori_neconfirmati():
    limita_timp = timezone.now() - timedelta(minutes=settings.K_MINUTES)
    utilizatori = CustomUser.objects.filter(
        email_confirmat=False, 
        date_joined__lt=limita_timp,
        is_superuser=False
    )
    
    count = utilizatori.count()
    for u in utilizatori:
        logger.info(f"Utilizator șters (neconfirmat): {u.username} - Email: {u.email}")
    
    utilizatori.delete()
    print(f"S-au șters {count} utilizatori neconfirmați.")


def trimite_newsletter_dinamic():
    vechime = timezone.now() - timedelta(minutes=settings.X_MINUTES_OLD)
    destinatari = CustomUser.objects.filter(date_joined__lt=vechime, email_confirmat=True)
    
    subiecte = ["Noutăți în bibliotecă", "Recomandările săptămânii", "Descoperă autori noi"]
    citate = [
        "O cameră fără cărți este ca un trup fără suflet.",
        "Lectura este o formă de fericire.",
        "Cărțile sunt oglinzi ale sufletului."
    ]

    for user in destinatari:
        continut = f"Salut {user.first_name if user.first_name else user.username},\n\n"
        continut += f"Citatul zilei: {random.choice(citate)}\n"
        continut += "Nu uita să verifici ultimele noastre titluri adăugate!"
        
        # Aici s-ar apela send_mail() din Django
        logger.info(f"Newsletter trimis către {user.email}")
    
    print(f"Newsletter trimis la {destinatari.count()} utilizatori.")

# --- TASK 3 (Alegere): Curățare loguri/accesări vechi (la fiecare M minute) ---
# Relevanță: Menține baza de date curată prin ștergerea înregistrărilor de trafic foarte vechi.
def curata_accesari_vechi():
    limita = timezone.now() - timedelta(days=7)
    vechi = Accesare.objects.filter(data__lt=limita)
    count = vechi.count()
    vechi.delete()
    logger.info(f"Task Curățare: S-au șters {count} înregistrări din Accesare.")

# --- TASK 4 (Alegere): Raport stoc cărți (Săptămânal Z2, ora O2) ---
# Relevanță: Notifică administratorul despre produsele care au stoc critic (sub 3 bucăți).
def raport_stoc_critic():
    critice = Carte.objects.filter(stoc__lt=3)
    if critice.exists():
        lista = ", ".join([c.titlu for c in critice])
        logger.warning(f"RAPORT STOC: Următoarele cărți au stoc critic: {lista}")
    else:
        logger.info("Raport stoc: Toate produsele sunt în stoc suficient.")