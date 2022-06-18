from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('shows', views.index),
    path('shows/new', views.create_new),
    path('shows/create', views.add_new),
    path('shows/<int:id>', views.dis_show, name='Display'),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/update', views.update_show),
    path('shows/<int:id>/destroy', views.del_show)
]
