from django.urls import path
from . import views

app_name = 'apollo'
urlpatterns = [
                path('', views.homepage, name = 'homepage'),
                path('login', views.emploginpage, name = 'emploginpage'),
                path('login', views.patloginpage, name = 'patloginpage'),
]
