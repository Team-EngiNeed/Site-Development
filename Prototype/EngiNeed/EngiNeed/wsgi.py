import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the Prototype directory to the Python path
sys.path.append(r'C:\Users\NanetteBugna\Desktop\Site Development\Prototype')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EngiNeed.settings')

# Initialize the WSGI application
application = get_wsgi_application()
