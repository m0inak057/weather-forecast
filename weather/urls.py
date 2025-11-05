from django.urls import path
from . import views

urlpatterns = [
    # Map the root URL ('') to the 'index' view
    path('', views.index, name='index'),
]