from django.conf.urls import patterns, include, url
from Tasks_List import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Practice_Site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^Tasks_List/', include('Tasks_List.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
