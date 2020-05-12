from django.shortcuts import render
from .models import Pet, Appointment
from django.core.mail import send_mail


def home(request):
    
    return render(request, 'pets/home.html',{})

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

def petlist(request, *args, **kwargs):
    context = {
        "pets": Pet.objects.all()
    }
    return render(request, 'petlist.html', context)

def petdetail(request, pet_id):
    context = {
        "pet": Pet.objects.get(id=pet_id)
    }
    return render(request, 'petdetail.html', context)

def calendar(request):
    context = {
        'appointments': Appointment.objects.all().order_by('date_of_appointment')
    }
    return render(request, 'calendar.html', context)