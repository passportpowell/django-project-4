from django.urls import path
from . import views
from django.urls import path
from blog import views

# urlpatterns = [
#     path("", views.EventList.as_view(), name="home"),
#     path("<slug:slug>/", views.EventDetails.as_view(), name="upcoming"),
#     path("attend/<slug:slug>", views.EventAttendee.as_view(), name="attending_event"),
#     path("game.html", views.GameView.as_view(), name="Game"),
#     path("schedule.html", views.EventDetails.as_view(), name="sched"),
#     path("past-meets.html", views.PastMeetsView.as_view(), name="gallery"),
    
#     path('create-booking/', views.make_booking, name='make_booking'),
#     path('book/<slug:slug>/', views.BookingView.as_view(), name='book_event'),
#     path('edit-booking/<str:pk>/', views.edit_booking, name='edit_booking'),
# ]


urlpatterns = [
    path("", views.EventList.as_view(), name="home"),
    path("create-booking/", views.make_booking, name="create_booking"),
    path("<slug:slug>/", views.EventDetails.as_view(), name="upcoming"),
    path("attend/<slug:slug>", views.EventAttendee.as_view(), name="attending_event"),
    path("game.html", views.GameView.as_view(), name="Game"),
    path("schedule.html", views.EventDetails.as_view(), name="sched"),
    path("past-meets.html", views.PastMeetsView.as_view(), name="gallery"),
    path("book/<slug:slug>/", views.BookingView.as_view(), name="book_event"),
    path("edit-booking/<str:pk>/", views.edit_booking, name="edit_booking"),
]


# from django.urls import path
# from blog import views

# urlpatterns = [
#     path("", views.EventList.as_view(), name="home"),
#     path("<slug:slug>/", views.EventDetails.as_view(), name="upcoming"),
#     path("attend/<slug:slug>/", views.EventAttendee.as_view(), name="attending_event"),
#     path("book/<slug:slug>/", views.BookingView.as_view(), name="book_event"),
#     path("game.html", views.GameView.as_view(), name="game"),
#     path("schedule.html", views.ScheduleView.as_view(), name="schedule"),
#     path("past-meets.html", views.PastMeetsView.as_view(), name="past_meets"),
# ]
