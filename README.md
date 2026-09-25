# Proiect Django - Anticariat 
Site-ul pune la dispozitie carti si diverse obiecte vechi de arta la preturi accesibile. Produsele pot fi livrate la domiciliu sau achizitionate din magazine fizice. De asemenea cumparam carti de la cei care sunt dispusi sa puna la dispozitie propriile carti. Site-ul web ajuta oamenii sa isi aleaga cartile preferate in functie de categorii (ex. tema, autor, editura). Interfata ofera simplitate si este intuitiva pentru usurinta plasarii unei comenzi, vanzarea unui produs sau pentru simpla informare asupra unor carti. In cazul intampinarii unor probleme, exista sectiune special destinata intrebarilor intalnite frecvent (FAQ) si in cazul in care problema nu e lamurita, site-ul ofera informatii de contact organizatorilor.
## Funcționalități principale
* **Autentificare utilizatori:** Înregistrare, login, resetare parolă, permisiuni bazate pe roluri.
* **Panou de administrare:** Gestionarea datelor prin Django Admin configurat personalizat.
* **CRUD complet:** Utilizatorii pot crea, citi, actualiza și șterge carti.
* **Filtrare și căutare:** Căutare rapidă după titlu/categorie.
* **Modul interactiv de promovare (Marketing Pop-ups):** Sistem dinamic de afișare a discount-urilor aleatorii/personalizate către utilizatori, bazat pe evenimente declanșate în interfață (trigger-based modals).
* **Modul Customer Support & Reclamații:** Sistem dedicat de preluare a solicitărilor de la clienți, ce include validare riguroasă pe backend (Django Forms), salvare organizată a tichetelor și trasabilitate automată a datelor de trimitere (timestamping).
## 🛠️ Stack Tehnologic
* **Backend:** Python, Django
* **Bază de date:** SQLite (dezvoltare) / PostgreSQL (producție)
* **Frontend:** Django Templates, Bootstrap 5 / Tailwind CSS, HTML5, CSS3
## ⚙️ Cum rulezi proiectul local
1. **Clonează depozitul:**
   \`\`\`bash
   git clone https://github.com/mateinicoo/proiect-django.git
   cd proiect-django
   \`\`\`

2. **Creează și activează mediul virtual:**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # Pe Linux/macOS sau: venv\Scripts\activate pe Windows
   \`\`\`

3. **Instalează dependențele:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Rulează migrațiile bazei de date:**
   \`\`\`bash
   python manage.py migrate
   \`\`\`

5. **Pornește serverul:**
   \`\`\`bash
   python manage.py runserver
   \`\`\`
   Aplicația va fi accesibilă la adresa `http://127.0.0.1:8000/`.
## 📸 Capturi de ecran / Demo
<img width="1439" height="686" alt="Captură de ecran din 2026-09-25 la 19 54 57" src="https://github.com/user-attachments/assets/a9c84954-1d77-483b-bca9-f23a19c46b81" />

<img width="1415" height="697" alt="Captură de ecran din 2026-09-25 la 19 54 20" src="https://github.com/user-attachments/assets/37e7d424-bc27-40a4-9031-76a40e916bbc" />

<img width="1428" height="688" alt="Captură de ecran din 2026-09-25 la 19 53 56" src="https://github.com/user-attachments/assets/712032b8-54bf-4c62-8383-0a697a3b8452" />

<img width="620" height="547" alt="Captură de ecran din 2025-10-16 la 10 23 28" src="https://github.com/user-attachments/assets/be463dde-983f-4463-8faf-747b92d6b1f9" />
