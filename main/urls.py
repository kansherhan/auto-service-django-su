from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('name/', views.name, name='author_name'),
    path('project/', views.project, name='project_info')
]
