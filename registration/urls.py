from django.urls import path
from registration.views import SignUpView
from django.contrib import admin
from . import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]