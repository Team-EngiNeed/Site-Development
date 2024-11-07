"""
WSGI config for EngiNeed project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""



import os

# Check if the platform is Windows and import the appropriate server library
if os.name == 'nt':  # Windows
    from waitress import serve
else:  # Unix-based system (Linux/MacOS)
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EngiNeed.settings')

    application = get_wsgi_application()

    # If you are using Gunicorn, your system will automatically use it as long as
    # the gunicorn command is used during deployment or local server execution.
    # Example: gunicorn EngiNeed.wsgi:application --bind 0.0.0.0:8000

    # No changes are needed if you're using Gunicorn on Unix-based systems.

