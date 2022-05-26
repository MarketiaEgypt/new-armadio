from django.urls import path

from Armadio import views

app_name = 'Armadio'

urlpatterns = [
    path('', views.home, name='home'),
    path('sitemap/',views.sitemap, name='sitemap')
    path('robots/', views.robots, name='robots')
]
