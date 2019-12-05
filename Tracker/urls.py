from django.urls import path

from . import views

urlpatterns = [
    path('sightings/', views.index, name='index'),
    path('sightings/add/', views.add,name="add"),
    path('sightings/<unique_squirrel_id>/', views.detail,name="detail"),
    path('map/',views.map,name='map'),
    ]


