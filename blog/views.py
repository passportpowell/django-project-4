from .models import Event, UserComment, Attendee, Booking
from .forms import CommentForm
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import BookingForm


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by("-published_date")
    template_name = "index.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "upcoming-events"
        return context


class EventDetails(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        user_comments = event.usercomments.filter(approved=True).order_by("created_at")
        attending = False
        if self.request.user.is_authenticated:
            if event.attending.filter(id=self.request.user.id).exists():
                attending = True

        bookings = Booking.objects.filter(event=event)

        context = {
            "event": event,
            "event_info": event.event_info,
            "comments": user_comments,
            "attending": attending,
            "bookings": bookings,
            "comment_form": CommentForm(),
            "commented": False,
            "page": "event-details",
        }

        return render(request, "schedule.html", context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        user_comments = event.usercomments.filter(approved=True).order_by("created_at")
        attending = False
        if self.request.user.is_authenticated:
            if event.attending.filter(id=self.request.user.id).exists():
                attending = True

        bookings = Booking.objects.filter(event=event)

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.user = self.request.user
            comment.save()
            commented = True
        else:
            commented = False

        context = {
            "event": event,
            "event_info": event.event_info,
            "comments": user_comments,
            "attending": attending,
            "bookings": bookings,
            "comment_form": comment_form,
            "commented": commented,
            "page": "event-details",
        }

        return render(request, "schedule.html", context)


class EventAttendee(View):
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)
        if self.request.user.is_authenticated:
            if event.attending.filter(id=self.request.user.id).exists():
                event.attending.remove(request.user)
            else:
                event.attending.add(request.user)

        return HttpResponseRedirect(reverse("upcoming", args=[slug]))


# @login_required(login_url="/login")
class BookingView(View):
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)
        if self.request.user.is_authenticated:
            booking = Booking(user=request.user, event=event)
            booking.save()

        return HttpResponseRedirect(reverse("upcoming", args=[slug]))


def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('/bookings')
    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {"form": form})


def edit_booking(request, pk):
    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)

    if booking.user.is_authenticated and booking.user == request.user:

        if request.method == 'POST':
            form = BookingForm(request.POST, instance=booking)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                return redirect('/bookings')
        context = {'form': form}
        return render(request, 'bookings/edit_booking.html', {"form": form})
    else:
        return render(request, 'bookings/404.html')



# Use class for the views.py as you can make the view reusable


# to fix - AttributeError at /event-test-this-is-the-slug/
# 'ManyToManyDescriptor' object has no attribute 'filter'
#     fixed by - changed code "if Event.likes.filter(id=self.request.user.id).exists():"
#     by making ht ecapital E into a lower case e

# from .models import Event
# from .forms import CommentForm
# from django.views import generic, View
# from django.http import HttpResponseRedirect
# from django.shortcuts import render, get_object_or_404, reverse


# class EventList(generic.ListView):
#     model = Event
#     queryset = Event.objects.filter(status=1).order_by("-published_date")
#     template_name = "index.html"
#     paginate_by = 4

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["page"] = "upcoming-events"
#         return context


# class EventDetails(View):
#     def get(self, request, slug, *args, **kwargs):
#         queryset = Event.objects.filter(status=1)
#         event = get_object_or_404(queryset, slug=slug)
#         user_comments = event.usercomments.filter(approved=True).order_by("created_at")
#         description = event.event_info
#         attending = False
#         if event.attending.filter(id=self.request.user.id).exists():
#             attending = True

#         context = {
#             "event": event,
#             "event_info": event.event_info,
#             "comments": user_comments,
#             "attending": attending,
#             "comment_form": CommentForm(),
#             "commented": False,
#             "page": "event-details",
#         }

#         return render(request, "schedule.html", context)

#     def post(self, request, slug, *args, **kwargs):
#         queryset = Event.objects.filter(status=1)
#         event = get_object_or_404(queryset, slug=slug)
#         user_comments = event.usercomments.filter(approved=True).order_by("created_at")
#         attending = False
#         if event.attending.filter(id=self.request.user.id).exists():
#             attending = True

#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             comment_form.instance.email = request.user.email
#             comment_form.instance.name = request.user.username
#             comment = comment_form.save(commit=False)
#             comment.event = event  # Set the event object as the event
#             comment.save()
#             commented = True
#         else:
#             commented = False

#         context = {
#             "event": event,
#             "event_info": event.event_info,
#             "comments": user_comments,
#             "attending": attending,
#             "comment_form": comment_form,
#             "commented": commented,
#             "page": "event-details",
#         }

#         return render(request, "schedule.html", context)


# class EventAttendee(View):
#     def post(self, request, slug, *args, **kwargs):
#         event = get_object_or_404(Event, slug=slug)
#         if event.attending.filter(id=self.request.user.id).exists():
#             event.attending.remove(request.user)
#         else:
#             event.attending.add(request.user)

#         return HttpResponseRedirect(reverse("upcoming", args=[slug]))


class PastMeetsView(View):
    def get(self, request):
        context = {"page": "past-meets"}
        return render(request, "past-meets.html", context)


class GameView(View):
    def get(self, request):
        context = {"page": "game"}
        return render(request, "game.html", context)


