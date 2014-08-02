from django.conf.urls import patterns, url
from Tasks_List import views

urlpatterns = patterns('',
                        url(r'^$', views.index, name='index'),
                        url(r'^add_task/$', views.add_task, name='add_task'),
                        url(r'^history/$', views.history, name='history'),
                        url(r'^delete/(?P<name>\w+)$', views.delete_task, name='delete'),
)
