from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
   contacts = Contact.objects.all()
   return  render(request, "index.html", {'contacts':contacts})