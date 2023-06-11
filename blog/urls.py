from django.urls import path
from . import views
from blog.views import delete_booking
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", views.EventList.as_view(), name="home"),
    path("create-booking/", views.make_booking, name="create_booking"),
    path("bookings/", views.make_booking, name="make_booking"),
    path("<slug:slug>/", views.EventDetails.as_view(), name="upcoming"),
    path("attend/<slug:slug>", views.EventAttendee.as_view(), name="attending_event"),
    path("game.html", views.GameView.as_view(), name="Game"),
    path("schedule.html", views.EventDetails.as_view(), name="sched"),
    path("past-meets.html", views.PastMeetsView.as_view(), name="gallery"),
    path("book/<slug:slug>/", views.BookingView.as_view(), name="book_event"),
    path("edit-booking/<str:pk>/", views.edit_booking, name="edit_booking"),
    path('bookings/delete/<int:booking_id>/', delete_booking, name='delete_booking'),
    path('bookings/', views.bookings, name='bookings'),
    path('login/', auth_views.LoginView.as_view(), name='login'),



]


# urlpatterns = [
#     path("", views.EventList.as_view(), name="home"),
#     path("create-booking/", views.make_booking, name="create_booking"),
#     path("<slug:slug>/", views.EventDetails.as_view(), name="upcoming"),
#     path("attend/<slug:slug>", views.EventAttendee.as_view(), name="attending_event"),
#     path("game.html", views.GameView.as_view(), name="Game"),
#     path("schedule.html", views.EventDetails.as_view(), name="sched"),
#     path("past-meets.html", views.PastMeetsView.as_view(), name="gallery"),
#     path("book/<slug:slug>/", views.BookingView.as_view(), name="book_event"),
#     path("edit-booking/<str:pk>/", views.edit_booking, name="edit_booking"),
# ]
