README.md

NaijaSure Insurance Manager is a simple yet powerful insurance management system designed with the Nigerian context in mind.
It helps insurance companies, agents, and policyholders handle registrations, products, payments, reminders, and penalties in a structured way.

This project was built with Python (OOP principles) and is designed to demonstrate how digital insurance systems can work in a modern Nigerian setting.

🚀 Features
✔️ Policyholder Management

Register new policyholders

Suspend or reactivate accounts

Assign insurance products

✔️ Product Management

Create insurance products (e.g., Health, Life, Auto)

Update product names and prices

Suspend/reactivate products

✔️ Payment System

Process policyholder payments

Send reminders for unpaid policies

Apply penalties for late payments

Store timestamps for real-world payment context

✔️ Nigerian Context

Localized branding: NaijaSure Insurance Manager

Nigerian currency format (₦)

User-friendly feedback with emojis 🎉

🏗️ Project Structure
NaijaSure-Insurance-Manager/
│
├── policyholder.py   # Handles policyholder registration, suspension, reactivation
├── product.py        # Handles insurance products (create, update, suspend, activate)
├── payment.py        # Handles payments, reminders, penalties
├── main.py           # Entry point (demo run)
└── README.md         # Documentation
📦 Installation & Setup
Clone the repository (or create a new folder in VS Code):

git clone https://github.com/your-username/NaijaSure-Insurance-Manager.git
cd NaijaSure-Insurance-Manager
Ensure you have Python 3.8+ installed:

python --version
Run the program:

python main.py
🎬 Example Run
🌍 Welcome to NaijaSure Insurance Manager 🌍
------------------------------------------------
📄 Funmi Johnson has been assigned product: Health Cover
📄 Chinyem Okocha has been assigned product: Life Assurance
💳 Payment of ₦50000 successful for Funmi Johnson on 2025-08-20 14:33:12.
💳 Payment of ₦75000 successful for Chinyem Okocha on 2025-08-20 14:33:12.

👤 Policyholder: Funmi Johnson (funmi.johnson@yahoo.com)
   Status: Active ✅
   Registered: 2025-08-20 14:33:12
   Products:
   - Health Cover | ₦50000

👤 Policyholder: Chinyem Okocha (chichi.ko@gmail.com)
   Status: Active ✅
   Registered: 2025-08-20 14:33:12
   Products:
   - Life Assurance | ₦75000
🎯 Learning Objectives
This project is designed to:

Demonstrate Object-Oriented Programming (OOP) concepts in Python

Show how to model real-world systems in code

Provide a localized example relevant to Nigeria’s insurance industry

Prepare students for software development projects in fintech/insurtech

✨ Possible Extensions
If you want to extend this project, you can add:

🔑 User login & authentication

💾 Database integration (SQLite/PostgreSQL)

🌐 Web interface (Flask/Django)

📊 Analytics dashboard for payments & products
