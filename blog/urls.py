from django.urls import path 
from .views import index,post_detail,creat_post

urlpatterns = [
    path("", index, name="index"),
    path("post/<int:id>/", post_detail, name="post_detail"),  
    path("creat/", creat_post, name="create_post"),
  
]

