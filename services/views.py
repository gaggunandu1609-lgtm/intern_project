from django.shortcuts import render
from .models import ProviderProfile


def home(request):
    providers = ProviderProfile.objects.all()
    return render(request, "home.html", {"providers": providers})


def dashboard(request):
    return render(request,'dashboard/dashboard.html')