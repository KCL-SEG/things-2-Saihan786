from django.shortcuts import render
from .forms import ThingForm

def home(request):
    if request.POST:
        form = ThingForm(request.POST)
    else:
        form = ThingForm()

    return render(request, 'home.html', {'form': form})
