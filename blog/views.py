from django.shortcuts import render
from django.views import generic
from .models import Event
# Create your views here.


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-published_date')
    template_name = 'index.html'
    paginate_by = 4

# Use class for the views.py as you can make the view reusable