# E-Commerce Neel

E-Commerce Neel is a simple **e-commerce web application** built using **Django (Python)** for the backend, **HTML, CSS, and JavaScript** for the frontend, and **SQLite3** as the database. This project allows users to browse products, view product details, and manage a shopping experience.
<img width="1886" height="828" alt="Screenshot 2026-01-06 161735" src="https://github.com/user-attachments/assets/74f0a760-fd6b-4674-971a-e06cae8fe276" />


---

## 🛠️ Features

- Display a list of products with images and details.
- Product detail page.
- Shopping cart functionality (basic or planned for future implementation).
- Admin panel for managing products.
- Fully responsive frontend layout using HTML, CSS, and JavaScript.
<img width="1880" height="855" alt="image" src="https://github.com/user-attachments/assets/dc1e0fd5-fcf3-4472-90f0-46c595a39c11" />
---

## 💻 Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite3  
- **Media Storage:** Local `media/product/` folder  

---

## 📂 Project Structure
E_Commerce-Neel/
│
├── app/ # Main Django application code
├── ecomm/ # E-commerce module
├── media/product/ # Product images
├── manage.py # Django management script
├── db.sqlite3 # SQLite database
├── static/ # CSS & JS files
└── templates/ # HTML templates

---

## ⚡ Prerequisites

- Python 3.8+  
- Django 4.x+  
- pip (Python package manager)

---

## 🚀 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Shanjid188/E_Commerce-Neel.git
cd E_Commerce-Neel

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

http://127.0.0.1:8000/


