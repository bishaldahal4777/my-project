from django.urls import path
from . import views


urlpatterns = [
    path("posts/", views.post_list, name= "post_list"),
    path("posts/<int:post_id>/", views.post_detail, name= "post_detail"),
    path("create/", views.create_post, name= "create_post"),


]
