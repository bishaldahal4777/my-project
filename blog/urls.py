from django.urls import path
from . import views


urlpatterns = [
    path("posts/", views.post_list, name= "post_list"),
    path("post/<int:post_id>/", views.post_detail, name= "post_detail"),
    path("create/", views.create_post, name= "create_post"),
    path("post/<int:post_id>/update/", views.update_post, name= "update_post"),
    path("post/<int:post_id>/delete/", views.delete_post, name= "delete_post"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),



]
