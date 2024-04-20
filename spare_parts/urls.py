from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="spare_parts_index"),
    path('create/', views.create, name="create_spare_parts"),
    path('update/<int:id>/', views.update, name="update_spare_part"),
    path('delete/<int:id>/', views.delete, name="delete_spare_part")
]
