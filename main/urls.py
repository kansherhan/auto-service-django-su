from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('name/', views.name, name='author_name'),
    path('project/', views.project, name='project_info'),
    path('api/', views.ServiceList.as_view(), name='service_list'),
    path('api/<int:pk>/', views.ServiceList2.as_view(), name='service_list2')
]
