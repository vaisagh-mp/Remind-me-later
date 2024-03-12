#Project Documentation: Remind-me-later

#Overview
Remind-me-later is a simple web app designed to allow users to set up reminders with a message. The app provides a user-friendly interface to input date, time, message, and the desired reminder method (SMS or Email). It is built using Django, a Python web framework.

#Features
Set up reminders with date, time, and message.
Choose between SMS and Email as reminder methods.
Basic CRUD functionality for reminders (Create, Retrieve, Update, Delete).

#Project Structure
RemindMeLaterProject: Django project folder.
reminders: Django app folder.
admin.py: Django admin configurations.
apps.py: App configuration.
models.py: Database models (Reminder).
serializers.py: Serializers for converting complex data types to Python data types.
views.py: Django views for handling HTTP requests.
urls.py: URL patterns for the app.

#Installation
1.Create a virtual environment: python -m venv venv
2.Activate the virtual environment:
3.venv\Scripts\activate
4.Install dependencies: pip install -r requirements.txt
5.Run migrations: python manage.py makemigrations and python manage.py migrate
6.Start the development server: python manage.py runserver

#API Endpoints
Create Reminder: POST /api/create/
List Reminders: GET /api/list/
Detail, Update, and Delete Reminder: GET/PUT/DELETE /api/<reminder_id>/

#Usage
1.Access the web app through the provided URL.
2.Use the UI to set up reminders with date, time, and message.
3.Choose between SMS and Email as the reminder method.
4.Utilize the API endpoints for programmatic interaction.

