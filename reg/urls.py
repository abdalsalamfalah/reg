from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from salam.views import Index,inserting,Delete,Update,Me
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',Index,name='index'),
    path('',inserting,name='regform'),
    path('delete/<int:item_id>',Delete,name='Delete'),
    path('update/<int:item_id>',Update,name='Update'),
    url(r'^me/$',Me,name='me'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    

 
]
