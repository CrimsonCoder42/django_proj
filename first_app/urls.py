from django.conf.urls import url
from django.urls import path
from first_app import views
 
 #url has been depricated https://ofstack.com/python/41042/explanation-of-the-difference-between-url--path-and-re_path-in-django.html
urlpatterns = [
    path('', views.index, name='index'),
]