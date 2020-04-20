from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('', views.index), 
    path('courses/add/', views.newCourse), 
    path('courses/destroy/<int:id>/', views.destroyCourse), 
    path('courses/destroy/<int:id>/delete/', views.deleteCourse), 

] 
 
 
