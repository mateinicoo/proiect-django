# 📚 Django Project - Antique Bookstore

The platform offers books and various vintage art objects at affordable prices. Products can be delivered to the customer's home or purchased from physical stores. We also buy books from individuals willing to sell their personal collections. 

The website helps users easily find their favorite books by filtering through categories (e.g., theme, author, publisher). The interface is simple and intuitive, ensuring a smooth experience whether placing an order, selling a product, or simply browsing for information. In case of any issues, there is a dedicated Frequently Asked Questions (FAQ) section, and if the problem remains unresolved, the website provides direct contact information for the support team.

## 🚀 Main Features
- **User Authentication:** Registration, login, password reset, and role-based permissions.
- **Admin Panel:** Centralized data management through a custom-configured Django Admin interface.
- **Full CRUD Operations:** Users can create, read, update, and delete books/listings.
- **Filtering and Search:** Quick search functionality by title or category.
- **Interactive Promotion Module (Marketing Pop-ups):** Dynamic system displaying randomized or personalized discounts to users, utilizing trigger-based modals driven by interface events.
- **Customer Support & Complaints Module:** Dedicated system for handling customer requests, featuring rigorous backend validation (Django Forms), organized ticket storage, and automatic submission traceability (timestamping).

## 🛠️ Tech Stack
- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Frontend:** Django Templates, HTML5, CSS3

## ⚙️ How to Run the Project Locally

1. **Clone the repository:**
   \`\`\`bash
   git clone https://github.com/mateinicoo/proiect-django.git
   cd proiect-django
   \`\`\`

2. **Create and activate the virtual environment:**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # Pe Linux/macOS sau: venv\Scripts\activate pe Windows
   \`\`\`

3. **Install dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run database migrations:**
   \`\`\`bash
   python manage.py migrate
   \`\`\`

5. **Start the server:**
   \`\`\`bash
   python manage.py runserver
   \`\`\`
   The application will be accessible at `http://127.0.0.1:8000/`.
## 📸 Screenshots / Demo
<img width="1439" height="686" alt="Captură de ecran din 2026-09-25 la 19 54 57" src="https://github.com/user-attachments/assets/a9c84954-1d77-483b-bca9-f23a19c46b81" />

<img width="1415" height="697" alt="Captură de ecran din 2026-09-25 la 19 54 20" src="https://github.com/user-attachments/assets/37e7d424-bc27-40a4-9031-76a40e916bbc" />

<img width="1428" height="688" alt="Captură de ecran din 2026-09-25 la 19 53 56" src="https://github.com/user-attachments/assets/712032b8-54bf-4c62-8383-0a697a3b8452" />

<img width="620" height="547" alt="Captură de ecran din 2025-10-16 la 10 23 28" src="https://github.com/user-attachments/assets/be463dde-983f-4463-8faf-747b92d6b1f9" />
