from django.shortcuts import redirect
from .models import Booking
from services.models import ProviderProfile


def book_service(request, id):

    provider = ProviderProfile.objects.get(id=id)

    Booking.objects.create(
        customer=request.user,
        provider=provider
    )

    return redirect('home')