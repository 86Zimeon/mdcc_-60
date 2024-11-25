from django.urls import path
from . import views
urlpatterns=[
    path("<place>",views.task),
]