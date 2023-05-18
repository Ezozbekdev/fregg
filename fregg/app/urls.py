from django.urls import path
from .views import main, aboutUs, service, contact

urlpatterns = [
    path('', main, name='main'),
    path('about/', aboutUs, name='about'),
    path('service/', service, name="service"),
    path('contact/', contact, name='contact')
]