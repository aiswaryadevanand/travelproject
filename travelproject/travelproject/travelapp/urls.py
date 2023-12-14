
from . import views
from django.urls import path
urlpatterns = [

    path('',views.demo,name='demo'),
    #path('about/',views.about,name='about'),
    #path('addition/',views.addition,name='addition'),
    #path('addition/add/',views.add,name='add')


]