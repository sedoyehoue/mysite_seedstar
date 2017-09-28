from django.conf.urls import url

from . import views

app_name = 'myapp'

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # # ex: /add/
    url(r'^add/$', views.add, name='add'), 
    # # ex: /list/
    url(r'^list/$', views.list, name='list'),
    
    url(r'^save/$', views.save, name='save'),

    url(r'^delete/$', views.delete, name='delete'),
    
   
]

