from django.shortcuts import render
from django.views import generic
from .models import Evacuation

class Home(generic.ListView):
   model = Evacuation
   queryset = Evacuation.objects.all()
   template_name = 'map/index.html'
