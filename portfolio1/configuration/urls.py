from django.urls import path
from . import views

urlpatterns = [
    
    path('form/',views.list_form,name='list_form'),
    path('form/del_form/<int:id>',views.del_form,name='del_form'),
    path('form/update_form/<int:id>', views.update_form, name='update_form'),
    path('form/update_form/update_form_action/<int:id>', views.update_form_action, name='update_form_action'),
    path('form/addForm/', views.add_form, name='add_form'),
    path('form/addForm/add_form_action/', views.add_form_action, name='add_form_action'),
    path('type/',views.list_type,name='list_type'),
    path('type/del_type/<int:id>',views.del_type,name='del_type'),
    path('type/update_type/<int:id>', views.update_type, name='update_type'),
    path('type/update_type/update_type_action/<int:id>', views.update_type_action, name='update_type_action'),
    path('type/addType/', views.add_type, name='add_type'),
    path('type/addType/add_type_action/', views.add_type_action, name='add_type_action'),  
    path('', views.connect, name='connect'),
    path('login/', views.signIn, name='signIn'),
    path('login/login/', views.signIn, name='signIn'),
    path('disconnect/', views.signOut, name='disconnect')  
]