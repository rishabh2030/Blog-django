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

print(Post.objects.filter(author__username='rishabhAdmin'))
print(Post.objects.filter(publish__year=2023))
print(Post.objects.filter(title__startswith='blog').exclude(publish__year=2022))
print(Post.objects.order_by('-title'))