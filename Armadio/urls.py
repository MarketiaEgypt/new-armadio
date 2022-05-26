from django.urls import path

from Armadio import views

app_name = 'Armadio'

urlpatterns = [
    path('', views.home, name='home'),
    path('sitemap.xml/',views.sitemap, name='sitemap'),
    path('robots.txt/', views.robots, name='robots')
]
