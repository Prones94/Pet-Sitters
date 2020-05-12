from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('contact/', views.contact, name='contact'),
    path('petlist/', views.petlist, name="petlist"),
    path('calendar/', views.calendar, name='calendar'),
    path('petlist/<int:pet_id>/', views.petdetail, name="petlist"),
]