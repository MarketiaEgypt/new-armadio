from django.urls import path

from Armadio import views

app_name = 'Armadio'

urlpatterns = [
    path('', views.home, name='home')
]
