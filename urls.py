from django.urls import path
from . import views

app_name = 'apollo'
urlpatterns = [
                path('', views.homepage, name = 'homepage'),
                path('emploginpage', views.emploginpage, name = 'emploginpage'),
                path('patloginpage', views.patloginpage, name = 'patloginpage'),
                path('patlogin_', views.patloginpage_, name = 'patloginpage_')
]
