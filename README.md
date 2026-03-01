# Loan Approval Prediction

An end-to-end project combining a backend application and a machine-learning model to predict loan approvals.

This repository implements loan approval logic with a backend (likely Django, based on the structure), machine-learning assets, templates for UI, and a local SQLite database.

---

## 🗂️ Project Structure
```text
├── db.sqlite3
├── manage.py
├── loans/ # Core app logic for loan functionality
├── ml/ # Machine learning model training & prediction
├── smartloan_project/ # Main project configuration (likely Django)
├── templates/ # HTML templates for web UI
└── requirements.txt # Python dependencies
```

---

## 🚀 Key Features

- Web application for submitting loan application data
- ML model (in `ml/`) that predicts loan approval
- Uses a local SQLite database for persistence
- Templates likely render frontend UI

---

## 🧠 How It Works (Typical Flow)

1️⃣ User submits loan application via web UI  
2️⃣ Backend receives the form data  
3️⃣ ML model in `ml/` processes and predicts approval  
4️⃣ Result is shown to the user  
5️⃣ Data is stored in the local database (`db.sqlite3`)

---

## 🛠️ Tech Stack

- Python 3.x  
- Django (asset structure suggests a Django project)  
- scikit-learn or similar for machine-learning  
- SQLite (default local DB)

---

## 📦 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/OrpanAp/Loan-Approval-Prediction.git
cd Loan-Approval-Prediction
```

### 2️⃣ Create & Activate a Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies

If there’s no requirements.txt, generate one after installing packages used:
```bash
pip install django scikit-learn pandas numpy
pip freeze > requirements.txt
```

Or if a requirements file does exist, simply install:
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
### 5️⃣ Start the Development Server

```bash
python manage.py runserver
```

Now open your browser at:

```bash
http://127.0.0.1:8000/
```
