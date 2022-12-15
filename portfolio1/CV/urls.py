from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('competance/',views.list_comp, name='list_comp'),
    path('stage/',views.list_stage, name='list_stage'),
    path('formation/',views.list_formation,name='list_formation')
    


]