from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/', views.add, name='add'),
    path('add/addtask/', views.add_task, name='addtask'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
    path('status/<int:id>', views.status, name='status'),
    path("update/<int:id>/", views.update, name="update"),
    path("update_task/<int:id>/", views.update_task, name="update_task"),

   
]