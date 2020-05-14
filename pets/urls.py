from django.urls import path
from . import views
from pets.views import HomeView, PetCreateView, PetListView, PetDetailView, CalendarListView, AppointmentCreateView


urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('contact/', views.contact, name='contact'),
    path('pets/',PetListView.as_view(), name="pet-list=page"),
    path('pet/create/', views.PetCreateView.as_view(), name='pet-create-page'), 
    path('pets/<int:pet_id>/', PetDetailView.as_view(), name="pet-detail-page"),
    path('calendar/', CalendarListView.as_view(), name='calendar-list-page'),
    path('appointment/create/', AppointmentCreateView.as_view(), name='appointment-create-page'),
]