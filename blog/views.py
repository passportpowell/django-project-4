from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView

from .models import Event, UserComment, Attendee
# Create your views here.


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-published_date')
    template_name = 'index.html'
    paginate_by = 4


# class EventDetails(View):
#     def get(self, request, slug, *args, **kwargs):
#         queryset = Event.objects.filter(status=1)
#         event = get_object_or_404(queryset, slug=slug)
#         user_comments = event.comments.filter(accepted=True).order_by(
#             "created_at")
#         user_liked = False
#         if Event.likes.filter(id=self.request.user.id).exists():
#             user_liked = True

#         return render(
#             request,
#             "index.html",
#             {
#                 "event": event,
#                 "comments": user_comments,
#                 "liked": user_liked
#             },
#         )


# Use class for the views.py as you can make the view reusable
