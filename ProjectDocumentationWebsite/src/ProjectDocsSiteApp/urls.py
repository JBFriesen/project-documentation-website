from django.urls import path 
from . import views

app_name = 'ProjectDocsSiteApp'
urlpatterns = [
    path('', views.all_projects_index, name='all_projects_index'),
    path('map/', views.all_projects_map, name='all_projects_map'),
    path('<int:project_id>/', views.project, name='project'),
    ]