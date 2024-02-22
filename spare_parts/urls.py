from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="spare_parts_index")
]
