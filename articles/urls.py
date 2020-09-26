from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'article_lists'

urlpatterns = [
    path('',views.article_list,name = 'lists'),
    path('create/',views.article_create,name = 'create'),
    # url('^create/$',views.article_create,name = 'create'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail, name='details'),
]

# try to use slug in path command

 #    path('<slug:slug>',views.article_detail,name ='details'),

