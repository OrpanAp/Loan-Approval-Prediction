# 🏦 Loan Approval Prediction

A **Django-based Machine Learning web application** that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant information.

The project combines a Django web interface with a trained **scikit-learn Logistic Regression pipeline**. Users submit their financial and personal information through a web form, the application passes the validated data through the saved machine-learning model, displays the prediction, and stores the application and result in a SQLite database.

---

## 📌 Project Overview

Loan approval is a binary classification problem where historical loan applications are used to learn patterns associated with approval outcomes.

This project demonstrates how a trained machine-learning model can be integrated into a Django application to provide an interactive prediction system.

### Main workflow

```text
User
 │
 ▼
Django Loan Form
 │
 ▼
Form Validation
 │
 ▼
Convert Input → Pandas DataFrame
 │
 ▼
Saved ML Pipeline
 │
 ├── Categorical Encoding
 │
 └── Logistic Regression
 │
 ▼
Prediction
 │
 ├── 1 → Approved
 │
 └── 0 → Rejected
 │
 ▼
Save Application + Result
 │
 ▼
Display Result
```

---

# ✨ Features

* 📝 Interactive loan application form
* 🤖 Machine-learning-based loan prediction
* 📊 Logistic Regression classification model
* 🔄 Integrated scikit-learn preprocessing pipeline
* 🔤 Automatic categorical feature encoding
* 🧹 Missing-value handling during model training
* 💾 Persisted trained model using Joblib
* 🗄️ SQLite database for prediction records
* 📜 Prediction history page
* 🛠️ Django admin interface
* 🎨 Bootstrap 5 user interface
* 🧩 django-crispy-forms integration
* 🔐 Django CSRF protection
* ✅ Server-side form validation
* 📅 Timestamped prediction records

---

# 🛠️ Technology Stack

## Backend

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| **Python**       | Main programming language |
| **Django 6.0.2** | Web framework             |
| **SQLite**       | Application database      |
| **Django ORM**   | Database operations       |

## Machine Learning

| Technology              | Purpose                   |
| ----------------------- | ------------------------- |
| **scikit-learn 1.8.0**  | Machine-learning pipeline |
| **Logistic Regression** | Binary classification     |
| **Pandas 3.0.1**        | Data processing           |
| **NumPy 2.4.2**         | Numerical computation     |
| **Joblib 1.5.3**        | Model persistence         |

## Frontend

| Technology                  | Purpose                        |
| --------------------------- | ------------------------------ |
| **HTML5**                   | Page structure                 |
| **Bootstrap 5.3.8**         | Responsive UI                  |
| **django-crispy-forms 2.6** | Form rendering                 |
| **crispy-bootstrap5**       | Bootstrap 5 form template pack |

The dependency versions are pinned in `requirements.txt`.

---

# 🧠 Machine Learning Model

The project uses:

```text
Logistic Regression
```

for binary classification.

The target variable comes from the `Loan_Status` column:

```text
Y → 1 → Approved
N → 0 → Rejected
```

The trained model is saved using:

```python
joblib.dump(model, "loan_model.pkl")
```

and the Django application loads that persisted pipeline when the application starts.

---

# 🔬 Machine Learning Pipeline

The training process is implemented in:

```text
ml/train_model.py
```

The pipeline performs the following operations.

## 1. Load Dataset

The training script reads:

```text
train_u6lujuX_CVtuZ9i.csv
```

using Pandas.

---

## 2. Handle Missing Numerical Values

Numerical columns are detected automatically and missing values are replaced with their respective column median.

Conceptually:

```text
Missing numerical value
        │
        ▼
Column median
        │
        ▼
Filled value
```

---

## 3. Handle Missing Categorical Values

Categorical columns are detected automatically.

Missing categorical values are replaced using the most frequent value—the column mode.

---

## 4. Clean Column Names

Column names are stripped of unnecessary leading/trailing whitespace.

```python
df.columns = df.columns.str.strip()
```

---

## 5. Remove `Loan_ID`

`Loan_ID` is treated as an identifier rather than a predictive feature and is removed before training.

```python
df = df.drop(columns=["Loan_ID"])
```

---

## 6. Create the Target

The target column is converted from:

```text
Y / N
```

to:

```text
1 / 0
```

using:

```python
df["Loan_Status"].map({"Y": 1, "N": 0})
```

---

## 7. Separate Features and Target

The dataset is separated into:

```text
X → Input features
y → Loan approval target
```

---

## 8. Detect Feature Types

The training script automatically identifies:

```text
Categorical columns
        +
Numerical columns
```

This allows the preprocessing pipeline to treat the two types differently.

---

## 9. One-Hot Encoding

Categorical features are transformed using:

```python
OneHotEncoder(handle_unknown="ignore")
```

This converts categorical values into numerical features that can be processed by Logistic Regression.

The `handle_unknown="ignore"` setting allows the pipeline to safely encounter a categorical value that was not present during training.

---

## 10. Preprocessing Pipeline

The preprocessing and classifier are combined into a single scikit-learn `Pipeline`.

```text
Raw Features
     │
     ▼
ColumnTransformer
     │
     ├── OneHotEncoder → categorical features
     │
     └── Passthrough → numerical features
     │
     ▼
Logistic Regression
```

This is important because the same preprocessing configuration used during training is preserved inside the saved model pipeline.

---

# 📊 Training Configuration

The dataset is split into:

```text
80% → Training
20% → Testing
```

with:

```python
random_state=42
```

The Logistic Regression classifier uses:

```python
LogisticRegression(max_iter=1000)
```

The test-set accuracy is printed after training.

The project does **not** hard-code an accuracy value in the README because the repository's training script calculates the metric at runtime rather than documenting a fixed benchmark.

---

# 🗃️ Dataset Features

The application accepts the following applicant information:

| Feature             | Description                   |
| ------------------- | ----------------------------- |
| `Gender`            | Applicant gender              |
| `Married`           | Marital status                |
| `Dependents`        | Number of dependents          |
| `Education`         | Graduate / Not Graduate       |
| `Self_Employed`     | Employment status             |
| `ApplicantIncome`   | Applicant income              |
| `CoapplicantIncome` | Co-applicant income           |
| `LoanAmount`        | Requested loan amount         |
| `Loan_Amount_Term`  | Loan repayment term in months |
| `Credit_History`    | Credit history indicator      |
| `Property_Area`     | Urban / Semiurban / Rural     |

The Django form explicitly defines the allowed categorical choices and numeric validation rules.

---

# 📝 Loan Application Form

The Django application uses a custom `LoanForm`.

### Available choices

#### Gender

```text
Male
Female
```

#### Married

```text
Yes
No
```

#### Dependents

```text
0
1
2
3+
```

#### Education

```text
Graduate
Not Graduate
```

#### Self Employed

```text
Yes
No
```

#### Credit History

```text
Yes → 1.0
No  → 0.0
```

#### Property Area

```text
Urban
Semiurban
Rural
```

Numeric fields require non-negative values.

These validations are implemented directly in `loans/forms.py`.

---

# 🔄 Prediction Flow

The main prediction view is:

```text
loans/views.py
```

The prediction endpoint handles both displaying the form and processing submitted applications.

### Request flow

```text
GET /
 │
 ▼
Create LoanForm
 │
 ▼
Render home.html
```

When the form is submitted:

```text
POST /
 │
 ▼
LoanForm(request.POST)
 │
 ▼
form.is_valid()
 │
 ▼
form.cleaned_data
 │
 ▼
Pandas DataFrame
 │
 ▼
Convert numeric fields
 │
 ▼
model.predict()
 │
 ▼
1 or 0
 │
 ▼
Approved / Rejected
 │
 ▼
Save database record
 │
 ▼
Render result.html
```

---

# 🤖 Model Inference

The trained model is loaded from:

```text
ml/loan_model.pkl
```

using:

```python
joblib.load(MODEL_PATH)
```

The path is constructed from Django's `BASE_DIR`.

The submitted form data is converted into a single-row Pandas DataFrame:

```python
input_data = pd.DataFrame([form.cleaned_data])
```

Numerical values are explicitly converted to floating-point values before prediction.

The model then returns a prediction:

```text
1 → Approved
0 → Rejected
```

The Django view converts that numeric result into a human-readable status:

```python
result = "Approved" if pred == 1 else "Rejected"
```

---

# 💾 Prediction Storage

After prediction, the application saves the submitted application and result into the database.

The database model is:

```text
LoanPrediction
```

It stores:

```text
ID
Gender
Married
Dependents
Education
Self_Employed
ApplicantIncome
CoapplicantIncome
LoanAmount
Loan_Amount_Term
Credit_History
Property_Area
Prediction
Created_At
```

The model definition is implemented in `loans/models.py`.

---

# 🗄️ Database

The project uses:

```text
SQLite
```

with the database file:

```text
db.sqlite3
```

Django is configured to use:

```python
django.db.backends.sqlite3
```

and the database is located at:

```text
BASE_DIR / "db.sqlite3"
```

---

# 📜 Prediction History

The application includes a history page:

```text
/history/
```

It retrieves all stored loan predictions and orders them from newest to oldest:

```python
LoanPrediction.objects.all().order_by("-Created_At")
```

The history page displays:

* Prediction ID
* Prediction result
* Applicant income
* Loan amount
* Creation date

---

# 🎯 Result Page

After a successful prediction, the user is redirected to a result view.

The result page displays:

```text
Prediction Result

Your loan is Approved
```

or:

```text
Prediction Result

Your loan is Rejected
```

Bootstrap alert styling changes according to the prediction:

```text
Approved → Success alert
Rejected → Danger alert
```

A **Try Again** button returns the user to the application form.

---

# 🎨 Frontend

The project uses Django templates together with:

```text
Bootstrap 5.3.8
django-crispy-forms
crispy-bootstrap5
```

The base template loads Bootstrap 5.3.8 through the jsDelivr CDN.

The loan form uses:

```django
{{ form|crispy }}
```

to render the Django form using the Bootstrap 5 crispy-forms template pack.

---

# 🧱 Project Architecture

```text
Loan-Approval-Prediction/
│
├── loans/
│   ├── migrations/
│   │   └── 0001_initial.py
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── ml/
│   ├── train_model.py
│   └── loan_model.pkl
│
├── smartloan_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── result.html
│   └── history.html
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

The repository's top-level structure contains the Django app, ML directory, project configuration, templates, SQLite database, management script, and dependency file.

---

# 📁 Important Files

## `manage.py`

Django's command-line entry point.

It configures:

```text
smartloan_project.settings
```

as the project's settings module.

---

## `loans/forms.py`

Defines the user-facing loan application form and its validation rules.

---

## `loans/models.py`

Defines the `LoanPrediction` database model used to store prediction records.

---

## `loans/views.py`

Contains the application's main business flow:

* Display form
* Validate submission
* Prepare model input
* Run prediction
* Save prediction
* Render result
* Retrieve history

---

## `loans/urls.py`

Defines:

```text
/          → predict_loan
/history/  → history
```

---

## `loans/admin.py`

Registers `LoanPrediction` with Django Admin.

The admin interface provides:

* List display
* Prediction filtering
* Property-area filtering
* Credit-history filtering
* Search by gender and education

---

## `ml/train_model.py`

Contains the machine-learning training workflow:

```text
Load dataset
     ↓
Handle missing values
     ↓
Clean columns
     ↓
Remove Loan_ID
     ↓
Create target
     ↓
Detect categorical/numeric features
     ↓
One-hot encode categorical features
     ↓
Train/test split
     ↓
Logistic Regression
     ↓
Evaluate accuracy
     ↓
Save model
```

---

## `ml/loan_model.pkl`

Contains the trained scikit-learn pipeline used by the Django application for inference.

Because the preprocessing transformer and classifier are saved together as a pipeline, the Django application can load the complete prediction workflow rather than separately reconstructing the encoder configuration.

---

# 🌐 URL Structure

| URL         | Function                      |
| ----------- | ----------------------------- |
| `/`         | Loan application / prediction |
| `/history/` | Prediction history            |
| `/admin/`   | Django administration         |

The root project includes the `loans.urls` configuration and Django's admin URL.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/OrpanAp/Loan-Approval-Prediction.git
```

```bash
cd Loan-Approval-Prediction
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

The repository pins Django, scikit-learn, pandas, NumPy, Joblib, Crispy Forms, and related dependencies in `requirements.txt`.

---

## 4. Apply migrations

```bash
python manage.py migrate
```

The repository already contains an initial migration for the `LoanPrediction` model.

If you modify the Django models later:

```bash
python manage.py makemigrations
```

then:

```bash
python manage.py migrate
```

---

## 5. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 🔑 Django Admin

Create an administrator account:

```bash
python manage.py createsuperuser
```

Then start the server:

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000/admin/
```

The `LoanPrediction` model is registered in Django Admin for inspecting stored predictions.

---

# 🧪 Training the Model

The training script is:

```text
ml/train_model.py
```

Run it from a location where the expected training CSV is available:

```bash
python ml/train_model.py
```

The script expects:

```text
train_u6lujuX_CVtuZ9i.csv
```

and writes:

```text
loan_model.pkl
```

using Joblib.

### Important

The current training script reads the dataset using:

```python
pd.read_csv("train_u6lujuX_CVtuZ9i.csv")
```

This is a relative path, so the CSV must be available from the process's current working directory when the training script is executed.

The Django application itself does not retrain the model when a prediction is requested; it loads the already-trained `ml/loan_model.pkl` file.

---

# 🔄 Complete System Architecture

```text
                    ┌─────────────────────┐
                    │       Browser       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Django URLconf   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   loans.views.py    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     LoanForm        │
                    │    Validation       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Pandas DataFrame  │
                    └──────────┬──────────┘
                               │
                               ▼
              ┌─────────────────────────────────┐
              │       loan_model.pkl            │
              │                                 │
              │   ColumnTransformer             │
              │          ↓                      │
              │   OneHotEncoder                 │
              │          ↓                      │
              │   Logistic Regression           │
              └────────────────┬────────────────┘
                               │
                               ▼
                     ┌──────────────────┐
                     │    Prediction    │
                     │ Approved/Rejected│
                     └────────┬─────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
        ┌─────────────────┐       ┌─────────────────┐
        │   SQLite DB     │       │   Result Page   │
        │ LoanPrediction  │       │    result.html  │
        └─────────────────┘       └─────────────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Prediction      │
        │ History         │
        └─────────────────┘
```

---

# 🔐 Security

The Django project includes standard security middleware such as:

```text
SecurityMiddleware
SessionMiddleware
CsrfViewMiddleware
AuthenticationMiddleware
MessageMiddleware
XFrameOptionsMiddleware
```

The loan form also includes Django's CSRF token:

```django
{% csrf_token %}
```

which protects the POST form against cross-site request forgery.

---

# ⚠️ Production Security

This repository is currently configured as a **development project**.

Before deploying publicly, the following settings should be changed.

## Secret Key

The current `settings.py` contains a hard-coded Django secret key.

For production, move this value to an environment variable or secret-management system.

## Debug

The project currently uses:

```python
DEBUG = True
```

Production should use:

```python
DEBUG = False
```

## Allowed Hosts

The current configuration uses:

```python
ALLOWED_HOSTS = []
```

A production deployment should explicitly configure the application's allowed hostnames.

These settings are currently visible in `smartloan_project/settings.py`.

---

# 📈 Limitations

This project is a machine-learning demonstration and should not be treated as a real-world automated lending decision system.

The model is trained on historical application data and therefore inherits the limitations of:

* The training dataset
* Feature selection
* Data quality
* Missing-value assumptions
* Model choice
* Train/test split
* Historical patterns

A prediction from this application should be interpreted as a **model prediction**, not as a guaranteed financial decision.

---

# 🔮 Future Improvements

Possible improvements include:

### Machine Learning

* Cross-validation
* Hyperparameter tuning
* Compare Logistic Regression with Random Forest, XGBoost, SVM, etc.
* ROC-AUC evaluation
* Precision / Recall / F1 reporting
* Confusion matrix visualization
* Feature importance analysis
* Probability-based predictions
* Model calibration
* Model versioning

### Application

* User authentication
* Applicant accounts
* Personalized prediction history
* Search and filtering
* Pagination
* Export prediction history
* REST API
* AJAX-based prediction
* Better error handling
* Prediction confidence display

### Production

* PostgreSQL
* Environment variables
* Production WSGI/ASGI deployment
* Static file collection
* HTTPS
* Secure secret management
* Automated tests
* CI/CD
* Model monitoring
* Dataset/model version tracking

---

# 📚 Learning Objectives

This project demonstrates how different areas of software engineering and machine learning can work together.

### Django

* Project/app structure
* URL routing
* Views
* Forms
* Models
* Templates
* ORM
* Migrations
* Admin
* CSRF protection

### Machine Learning

* Data cleaning
* Missing-value handling
* Feature preprocessing
* One-hot encoding
* Train/test splitting
* Logistic Regression
* Model evaluation
* Model persistence
* Model inference

### Integration

Most importantly, the project demonstrates how to connect a trained machine-learning pipeline to a web application:

```text
Machine Learning
       │
       │ saved with Joblib
       ▼
loan_model.pkl
       │
       │ loaded by Django
       ▼
Django Application
       │
       ▼
User Input
       │
       ▼
Prediction
```

---

# 👨‍💻 Author

**OrpanAp**

GitHub:

https://github.com/OrpanAp

Repository:

https://github.com/OrpanAp/Loan-Approval-Prediction

---

# 📄 License

No explicit open-source license is currently specified in the repository.

If this project is intended for public distribution or reuse, an appropriate license should be added.

---

# ⭐ Project Summary

**Loan Approval Prediction** is an end-to-end Django + Machine Learning project that demonstrates the integration of a trained classification model into a web application.

The system combines:

```text
Python
   +
Django
   +
Pandas
   +
scikit-learn
   +
Logistic Regression
   +
Joblib
   +
SQLite
   +
Bootstrap 5
```

to create an interactive loan prediction system.

The application accepts applicant information, validates it through Django, transforms it into a Pandas DataFrame, sends it through the saved scikit-learn preprocessing/model pipeline, returns an **Approved** or **Rejected** prediction, and stores the result for later viewing in the prediction history.
