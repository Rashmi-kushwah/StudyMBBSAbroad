from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect



from django.shortcuts import render
from django.http import JsonResponse

def landing_page(request):
    return render(request, 'index.html')

from  studyapp.models import Lead

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')

        # Data ko database me save karna
        lead = Lead.objects.create(name=name, email=email, phone=phone, country=country)
        print("sdsjfsdfdf",lead)
        print("sdsjfsdfdf",lead.id)

        return JsonResponse({'message': 'Form submitted successfully!', 'lead_id': lead.id})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)