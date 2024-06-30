#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tierra/', views.tierra, name = 'tierra' ),
    path('macetero/', views.macetero, name = 'macetero' ),
    path('flores/', views.flores, name = 'flores' ),
    path('arbustos/', views.arbustos, name = 'arbustos' ),
]