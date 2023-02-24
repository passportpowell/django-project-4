
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .forms import CommentForm

from .models import Event, UserComment, Attendee
# Create your views here.


# def home(request):
#     context = {
#         'page': 'home',
#     }
#     return render(request, 'home.html', context)

class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-published_date')
    template_name = 'index.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)
        context['page'] = 'upcoming-events'
        return context


class EventDetails(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        user_comments = event.usercomments.filter(
            approved=True).order_by("created_at")
        description = event.description
        user_liked = False
        if event.likes.filter(id=self.request.user.id).exists():
            user_liked = True

        context = {
                "event": event,
                "description": Event.description,
                "event_info": event.event_info,
                "comments": user_comments,
                "liked": user_liked,
                "comment_form": CommentForm(),
                "commented": False,
                "page": "event-details"
            }

        return render(request, "schedule.html", context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        user_comments = event.usercomments.filter(
            approved=True).order_by("created_at")
        user_liked = False
        if event.likes.filter(id=self.request.user.id).exists():
            user_liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.event = event  # Set the event object as the event
            comment.save()
            commented = True
        else:
            commented = False

        context = {
                "event": event,
                "event_info": event.event_info,
                "comments": user_comments,
                "liked": user_liked,
                "comment_form": comment_form,
                "commented": commented,
                "page": "event-details"
            }

        return render(request, "schedule.html", context)


class EventAttendee(View):

    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)
        if event.likes.filter(id=self.request.user.id).exists():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)

        return HttpResponseRedirect(reverse('upcoming', args=[slug])) 


class PastMeetsView(View):
    def get(self, request):
        context = {
            'page': 'past-meets'
        }
        return render(request, 'past-meets.html', context)


class GameView(View):
    def get(self, request):
        context = {
            'page': 'game'
        }
        return render(request, 'game.html', context)


# Use class for the views.py as you can make the view reusable


# to fix - AttributeError at /event-test-this-is-the-slug/
# 'ManyToManyDescriptor' object has no attribute 'filter'
#     fixed by - changed code "if Event.likes.filter(id=self.request.user.id).exists():"
#     by making ht ecapital E into a lower case e
