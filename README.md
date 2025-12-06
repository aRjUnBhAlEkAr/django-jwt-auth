# 🔐 Django JWT Authentication API

A lightweight and secure **JWT-based authentication system** built using **Django REST Framework** and **SimpleJWT**.
This project provides a minimal yet production-ready setup for handling user authentication using **Access** and **Refresh** tokens.

---

## 📘 Documentation

This project uses **SimpleJWT** for token-based authentication.

📄 Official SimpleJWT Documentation:
**[https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)**

---

## 📌 About the Project

This project is a starter template for implementing **JWT Authentication** in Django using:

* Django REST Framework (DRF)
* SimpleJWT for token generation & verification
* django-environ for secure environment variable management
* Standard Django authentication model

It includes:

* User registration
* User login
* Access/Refresh token generation
* Token refresh endpoint
* Protected user profile endpoint
* Clean project structure for easy expansion

Ideal for building:

* Backend APIs
* Microservices
* Authentication services
* Modern full-stack applications (React, Vue, Angular, Flutter, etc.)

---

## 🚀 Features

* ✔ JWT Access & Refresh tokens
* ✔ Token blacklisting support
* ✔ Secure password hashing
* ✔ Minimal & modular architecture
* ✔ Ready for role-based permissions
* ✔ Environment-based settings

---

## 🛠 Tech Stack

* **Django**
* **Django REST Framework**
* **SimpleJWT**
* **PostgreSQL / SQLite**
* **django-environ**

---

## ▶️ Installation

```bash
git clone https://github.com/aRjUnBhAlEkAr/django-jwt-auth.git
cd django-jwt-auth
```

Create and activate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

Run migrations:

```bash
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```
---

## 💻 Author

Taskify is built with ❤️ by Arjun Bhalekar

If you like this project, please ⭐️ star the repo — it helps others find it!

📧 [arjunbhalekar37@gmail.com](mailto:arjunbhalekar37@gmail.com)

🌐 [LinkedIn](https://www.linkedin.com/in/arjun-bhalekar/)

---  

## 📜 License
This project is licensed under the MIT License.

You’re free to use, modify, and distribute it as you wish.


## 🤝 Contributing

Contributions are welcome! 🎉
To contribute:

Fork this repository.

Create a new branch (feature/your-feature-name).

Commit your changes.

Push and create a Pull Request.
