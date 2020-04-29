from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('collector_list', views.collector_list, name='collector_list'),
    path('collector/<int:pk>/edit/', views.collector_edit, name='collector_edit'),
    path('collector/<int:pk>/delete/', views.collector_delete, name='collector_delete'),
    path('console_list', views.console_list, name='console_list'),
    path('console/create/', views.console_new, name='console_new'),
    path('console/<int:pk>/edit/', views.console_edit, name='console_edit'),
    path('console/<int:pk>/delete/', views.console_delete, name='console_delete'),
    path('videogame_list', views.videogame_list, name='videogame_list'),
    path('videogame/create/', views.videogame_new, name='videogame_new'),
    path('videogame/<int:pk>/edit/', views.videogame_edit, name='videogame_edit'),
    path('videogame/<int:pk>/delete/', views.videogame_delete, name='videogame_delete'),
    path('collector/<int:pk>/summary/', views.summary, name='summary'),
]
