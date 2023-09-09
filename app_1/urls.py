
from django.urls import path
from . import views

urlpatterns = [
    path("v1/", views.ProjectOneAPIView.as_view(), name='project')
]
