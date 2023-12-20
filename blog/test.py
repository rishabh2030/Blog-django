import os
import sys

# Add the path to your Django project directory
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))  # Adjust this based on your project structure

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")  # Update with your project's settings module
import django
django.setup()

# Now import your models and use them
from blog.models import Post
from django.core.mail import send_mail
send_mail('Django mail','This e-mail was sent with Django.','saraswat.rishabh30@gmail.com',['saraswat.rishabh30@gmail.com'],fail_silently=False)