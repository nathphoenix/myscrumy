from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('$/', views.posts, name='posts'),
    path('$/', views.comments, name='comments'),

]
