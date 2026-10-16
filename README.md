# 🌱 Sempulam – Agri-Based Finance and Demand-Based Bidding

**Sempulam** is a Django-based agricultural platform designed to connect farmers and investors through agricultural financing and demand-based investment opportunities.

The platform allows farmers to register their agricultural land and crops, while investors can explore available opportunities and submit investment requests. Sempulam aims to make agricultural investment more accessible by creating a digital connection between farmers seeking financial support and investors interested in agriculture.

## 🎯 Project Objectives

- Connect farmers with potential agricultural investors.
- Enable farmers to register their land and crop details.
- Allow investors to explore agricultural investment opportunities.
- Facilitate investment requests and acceptance or rejection workflows.
- Provide separate dashboards for farmers and investors.
- Support communication through in-app notifications.

## ✨ Features

### 👨‍🌾 Farmer Module
- Farmer registration and login.
- Farmer dashboard.
- Agricultural land registration.
- Crop registration and management.
- View investment requests from investors.
- Accept or reject investment requests.

### 💼 Investor Module
- Investor registration and login.
- Investor dashboard.
- Explore agricultural investment opportunities.
- Submit investment requests to farmers.
- Track investment-related activities.

### 🔔 Notification System
- In-app notifications for important investment-related activities.
- Updates when investment requests are submitted or processed.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web application framework |
| HTML5 | Page structure |
| CSS3 | Styling and layout |
| JavaScript | Frontend interactivity |
| SQLite | Database management |
| Git and GitHub | Version control and source code hosting |

## 📂 Project Structure

```text
sempulam/
├── config/             # Django project configuration
├── core/               # Main application and business logic
├── manage.py           # Django management utility
├── .gitignore          # Files excluded from version control
└── README.md           # Project documentation
```

## ⚙️ Installation and Setup

Follow these steps to run Sempulam on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/sree723/sempulam-agri-based-finance-and-demand-based-bidding-.git
```

### 2. Navigate to the Project Directory

```bash
cd sempulam-agri-based-finance-and-demand-based-bidding-
```

### 3. Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

If a `requirements.txt` file exists:

```bash
pip install -r requirements.txt
```

If it does not exist yet, install Django:

```bash
pip install django
```

> Install any additional dependencies required by the project.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open the following address in your browser:

**http://127.0.0.1:8000/**

## 🔐 Security Notes

- Do not commit passwords, secret keys, environment files, or private user documents.
- Keep the Django production secret key outside the source code.
- Use environment variables for sensitive configuration.
- Configure production security settings before deploying the application.

## 🚀 Future Enhancements

- Farmer and investor profile management.
- Agricultural investment tracking.
- Identity verification with appropriate privacy safeguards.
- Digital agreement generation after investment acceptance.
- Improved notification and communication features.
- Deployment to a production hosting platform.

## 🎓 Project Purpose

Sempulam demonstrates how web technologies can be used to support agricultural financing by connecting farmers and investors through a centralized digital platform.

## 👥 Contributors

Developed as an agricultural technology project.

## 📄 License

No license has been specified yet. All rights are reserved unless a license is added to this repository.
