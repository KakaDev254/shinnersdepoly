from django.shortcuts import render,redirect
from .forms import TestimonialForm
from django.contrib import messages
from .models import Client, GalleryItem, TeamBuildingItem, CharityEvent,Testimonial



def home(request):
    testimonials = Testimonial.objects.filter(approved=True).order_by('-submitted_at')[:6]
    clients = Client.objects.all()
    form = TestimonialForm()
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your testimonial has been submitted for review.")
            return redirect('home')  # Use the name of your home URL pattern

    return render(request, 'core/home.html', {
        'testimonials': testimonials,
        'form': form,
        "clients": clients,
    })

def emcee(request):
    return render(request, 'core/emcee.html', )

def gallery_page(request):
    context = {
        "gallery_items": GalleryItem.objects.all(),
        "team_items":    TeamBuildingItem.objects.all(),
    }
    return render(request, "core/gallery.html", context)

def donate_view(request):
    charity_events = CharityEvent.objects.all()
    return render(request, 'core/donate.html', {'charity_events': charity_events})