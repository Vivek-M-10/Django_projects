from django.urls import path
from  . import views

urlpatterns = [
    path('students/', views.StudentView,),
    path('students/<int:pk>/', views.studentViewlist,),
]
