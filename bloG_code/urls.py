from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.Blog_list.as_view(),name="blog_list"),
    path('<int:id>',views.Blog_detail.as_view(),name="blog_detail"),
]
