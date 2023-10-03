from django.urls import path
# from django.conf.urls import handler404
from . import views

app_name = 'todo'

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>', views.detail, name='detail'),
  path('create/', views.create, name='create'),
  path('register/', views.register, name='register'),
  path('<int:id>/edit/',views.edit, name="edit"),
  path('<int:id>/update', views.update, name='update'),
  path('<int:id>/delete', views.delete, name='delete'),

]
