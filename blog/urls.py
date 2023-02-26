from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('<slug:slug>/', views.EventDetails.as_view(), name='upcoming'),
    path('attend/<slug:slug>', views.EventAttendee.as_view(), name='attending_event'),
    path('game.html', views.GameView.as_view(), name='Game'),
    path('schedule.html', views.EventDetails.as_view(), name='sched'),
    path('past-meets.html', views.PastMeetsView.as_view(), name='gallery'),
]