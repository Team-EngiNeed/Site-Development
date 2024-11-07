import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the Prototype directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set the settings module for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EngiNeed.settings')

# Initialize the WSGI application
application = get_wsgi_application()
