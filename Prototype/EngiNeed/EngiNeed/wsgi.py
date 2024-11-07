import os
import sys
from django.core.wsgi import get_wsgi_application


# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EngiNeed.settings')

# Initialize the WSGI application
application = get_wsgi_application()


sys.path.append('C:\Users\NanetteBugna\Desktop\Site Development\Prototype')  # Adjust this to the correct path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EngiNeed.settings')

