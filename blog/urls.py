from django.urls import path
from . import views

# app_name = 'djangoproject4'

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('<slug:slug>/', views.EventDetails.as_view(), name='schedules'),
    # path('', views.EventDetails.as_view(), name='schedule'),
    #path('schedule.html', views.EventList.as_view(), name='schedule'),

    # Add a default value for the slug parameter
    # path('schedule/', views.EventDetails.as_view(), name='schedule_default'),
    #  path('schedule/', views.EventDetails.as_view(), {'slug': 'default-slug'}, name='schedule_default'),


]
    # path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),

    # path('index.html', views.Home.as_view(), name='home'),
    # path('signup.html', views.SignupView.as_view(), name='signup'),
    # path('game.html', views.GameView.as_view(), name='Game'),
    # path('past-meets.html', views.PastMeetsView.as_view(), name='gallery'),
    # path('gallery.html', views.GalleryView.as_view(), name='gallery'),
    # path('comment/<slug:slug>/',
    #      views.CommentCreateView.as_view(), name='comment_create'),
    # path('event/new/', views.event_create, name='event_create'),
#]



# from django.urls import path
# from . import views

# app_name = 'djangoproject4'

# urlpatterns = [
#     path('', views.EventListView.as_view(), name='home'),
#     path('<slug:slug>/', views.EventDetailView.as_view(), name='event_detail'),
#     path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),

#     path('index.html', views.Home.as_view(), name='home'),
#     path('signup.html', views.SignupView.as_view(), name='signup'),
#     path('schedule.html', views.ScheduleView.as_view(), name='schedule'),
#     path('game.html', views.GameView.as_view(), name='Game'),
#     path('past-meets.html', views.PastMeetsView.as_view(), name='gallery'),
#     path('gallery.html', views.GalleryView.as_view(), name='gallery'),
#     path('comment/<slug:slug>/',
#          views.CommentCreateView.as_view(), name='comment_create'),
#     path('event/new/', views.event_create, name='event_create'),
# ]
