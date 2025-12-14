from django.urls import path
from . import views


urlpatterns = [
    path('course-data', views.course_data),
    path('addcourse', views.add_course),
    path('', views.coursesPage),
    path('loginP', views.loginP),
]