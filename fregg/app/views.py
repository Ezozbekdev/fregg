from django.shortcuts import render
from .models import (
    About, Service, Testimonial, Contact
)
from .forms import ContactForm


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'html/contact.html', {"form": form})


def service(request):
    service = Service.objects.all()

    return render(request, "html/service.html", {'service': service})


def aboutUs(request):
    abouts = About.objects.all()
    return render(request, "html/about.html", {'about': abouts})


def main(request):
    abouts = About.objects.all()

    service = Service.objects.all()
    testimonial = Testimonial.objects.all()
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'about': abouts,
        'service': service,
        'test': testimonial,
        'form': form
    }
    return render(request, "html/index.html", context)
