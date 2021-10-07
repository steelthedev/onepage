from . import views
from django.urls import path





urlpatterns = [
    path('', views.Homepage , name="home"),
    path('send_email', views.Email_Send, name="email")
    ]
