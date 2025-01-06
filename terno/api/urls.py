from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('organisation', views.get_org_details, name='get_org_details'),
    path('check-user', views.create_user, name='create_user'),
]
