from django.shortcuts import render
from .forms import ThingForm

def home(request):
    # if request.GET:
    #     form = ThingForm(request.GET)
    # else:
    #     form = ThingForm()
    form = ThingForm()

    return render(request, 'home.html', {'form': form})
