from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.utils import timezone

from pets.models import Pet, Appointment


class HomeView(ListView):
    def get(self, request):
        return render(request, 'home.html')

class PetCreateView(CreateView):
    model = Pet
    fields = ['pet_name', 'species', 'breed', 'weight_in_pounds', 'owner']
    template_name = 'pet/createpet.html'

class PetListView(ListView):
    model = Pet

    def get(self, request):
        pets = self.get_queryset().all()
        return render(request, 'pet/petlist.html', {'pets': pets})

class PetDetailView(DetailView):
    def get(self, request, pet_id):
        return render(request, 'pet/petdetail.html', { 'pet': Pet.objects.get(id=pet_id)})

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['date_of_appointment',
              'duration_minutes',
              'special_instructions',
              'pet',
              'appointment_name']
    template_name = 'calendar/create_appointment.html'

class CalendarListView(ListView):
    model = Appointment

    def get(self, request):
        appointments = self.get_queryset().all()
        return render(request, 'calendar/calendarlist.html',{
            'appointment': appointments.filter(
                date_of_appointment__gte = timezone.now()
            ).order_by('date_of_appointment' 'date_of_appointment')
        })


def contact(request):
    if request.method == "POST":
        contact_name = request.POST['contact-name']
        contact_email = request.POST['contact-email']
        message = request.POST['message']
        
        # Send an email 
        send_mail(
            contact_name, # Subject
            message, # Message
            contact_email, # Sender email
            ['ian.rones@students.makeschool.com'], # Receivable email
        )

        return render(request, 'contact.html', {'contact_name': contact_name})

    else:
        return render(request, 'contact.html', {})