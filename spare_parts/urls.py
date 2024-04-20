from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="spare_parts_index"),
    path('create/', views.create, name="create_spare_parts"),
    path('update/<int:id>/', views.update, name="update_spare_part"),
    path('delete/<int:id>/', views.delete, name="delete_spare_part"),
    path('api/', include([
        path('', views.index_api, name="spare_parts_index_api"),
        path('update/<int:id>/', views.update_api, name="spare_parts_update_api")
    ]))
]
