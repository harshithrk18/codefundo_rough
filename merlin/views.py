from django.shortcuts import render
import requests
from .models import ReliefCamp
# Create your views here.

def index(request):
    data = ReliefCamp.objects.all()
    return render(request, 'merlin/index.html',{'data':data})