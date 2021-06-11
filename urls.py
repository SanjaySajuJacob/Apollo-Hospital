from django.urls import path
from . import views

app_name = 'apollo'
urlpatterns = [
                path('', views.homepage, name = 'homepage'),
                path('emploginpage', views.emploginpage, name = 'emploginpage'),
                path('patregister', views.patregisterpage, name = 'patregisterpage'),
                path('patlogin', views.patloginpage, name = 'patloginpage'),
                path('payment', views.paymentpage, name = 'paymentpage')
]
