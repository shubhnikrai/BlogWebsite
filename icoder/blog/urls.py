from django.contrib import admin
from django.urls import path,include
from . import views
admin.site.site_header="iCoder Admin"
admin.site.site_title="iCoder Admin Panel"
admin.site.index_title="Welcome to iCoder Admin Panel"
urlpatterns = [
   path('', views.blogHome, name='blogHome'),
   path('postComment',views.postComment,name="postComment"),
   path('<str:slug>', views.blogPost, name='blogPost'),

   # API to post comment

   
  
]