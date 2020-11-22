from django.urls import path

from . import models
from .views import *

urlpatterns = [
    path('', MyView.as_view()),
]