from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name="search"),
    path('<str:slug>', views.single_post, name="single-post"),
    path('category/<str:category>', views.category, name="category"),
    
] 
