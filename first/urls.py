from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('select/', views.select),
    path('result/', views.result),

    #path('select/<int:year>',.. ,..),


]

