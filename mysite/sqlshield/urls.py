from django.urls import path
from . import views

app_name = 'sqlshield'

urlpatterns = [
    path('', views.index, name='index'),
]
