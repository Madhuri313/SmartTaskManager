SmartTaskManager - Django Task Manager (custom CSS UI)
-----------------------------------------------------
What's included:
- Django project with two apps: accounts, tasks
- Login / Signup with session auth
- Task model with tags, priority, due date, completed status
- Filters, dashboard, and nice custom CSS (no Bootstrap)

Quick start:
1. Create a Python virtualenv and activate it.
   python -m venv venv
   source venv/bin/activate    (Linux/Mac) or venv\Scripts\activate (Windows)

2. Install Django:
   pip install django

3. From project root (/mnt/data/SmartTaskManager) run migrations:
   python manage.py migrate

4. Create a superuser (optional):
   python manage.py createsuperuser

5. Run server:
   python manage.py runserver

Static files: static/ folder contains CSS and JS already configured for development.

Notes:
- Replace SECRET_KEY in project/settings.py for production.
- DEBUG=True is set for convenience. Turn off for production.
