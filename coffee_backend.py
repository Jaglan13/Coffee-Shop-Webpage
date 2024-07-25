# coffeeshop_backend.py

# Import Django modules
from django.http import JsonResponse
from django.urls import path
from django.core.management import execute_from_command_line
from django.conf import settings

# Define Django settings
SECRET_KEY = 'your_secret_key'
DEBUG = True
ALLOWED_HOSTS = []

# Configure Django settings
settings.configure(
    SECRET_KEY=SECRET_KEY,
    DEBUG=DEBUG,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Add your own apps here
        'coffeeshop',
    ],
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
)

# Define Django models
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

# Define Django views
def get_menu(request):
    # Retrieve menu items from the database
    menu_items = MenuItem.objects.all().values('name', 'price')
    return JsonResponse(list(menu_items), safe=False)

def add_to_cart(request):
    # Logic to add item to cart
    return JsonResponse({'status': 'success'})

# Define Django URL patterns
urlpatterns = [
    path('menu/', get_menu, name='get_menu'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    # Add more URL patterns for other views
]

# Run Django server
if __name__ == "__main__":
    import sys
    execute_from_command_line(sys.argv)
