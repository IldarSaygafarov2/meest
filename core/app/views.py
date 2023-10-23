from django.shortcuts import render, redirect

from .forms import UserRequestForm
from .models import UserRequest
from .utils import save_to_excel
import os
from django.conf import settings


def home(request):
    if request.method == "POST":
        form = UserRequestForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRequestForm()

    context = {
        "form": form
    }
    return render(request, "app/index.html", context)


def elements_view(request):
    query = request.GET
    date_from = query.get('date_from')
    date_to = query.get('date_to')
    phone_number = query.get("phone_number")
    pinfl = query.get("pinfl")
    query_fullname = query.get('fullname')
    passport_series = query.get("passport_series")

    if query_fullname:
        elements = UserRequest.objects.filter(fullname__iregex=query_fullname)
    elif phone_number:
        elements = UserRequest.objects.filter(phone_number__iregex=phone_number)
    elif passport_series:
        elements = UserRequest.objects.filter(passport_number__iregex=passport_series)
    elif pinfl:
        elements = UserRequest.objects.filter(pinfl__iregex=pinfl)
    elif date_from and date_to:
        elements = UserRequest.objects.filter(created_at__gt=date_from, created_at__lt=date_to)
        print(elements)
    else:
        elements = UserRequest.objects.all()

    context = {
        "elements": elements
    }

    return render(request, "app/elements.html", context)


def get_excel(request):
    elements = UserRequest.objects.all().values_list('track_number', 'fullname', 'passport_series', 'passport_number', 'pinfl', 'phone_number')
    save_to_excel(
        filename=settings.BASE_DIR / 'app/static/test.xlsx',
        data=elements
    )

    return render(request, 'app/result.html')
