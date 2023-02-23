from django.urls import path
from . import views



# app_name = 'djangoproject4'

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('<slug:slug>/', views.EventDetails.as_view(), name='upcoming'),

]
