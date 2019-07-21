from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('$/', views.posts, name='posts'),
    path('$/', views.comments, name='comments'),
    # path('<int:goal_id>/', views.move_goal, name='move_goal'),
    path('<goal_name>/', views.add_goal, name='add_goal'),
    path('<goal_name>/home', views.home, name='home'),
    path('movegoal/<int:goal_id>', views.movegoal, name='movegoal'),
    # path('<message>/', views.detail, name='detail'),
    # path('<message>/results', views.results, name='results'),
    # path('<message>/vote', views.vote, name='vote'),

]
