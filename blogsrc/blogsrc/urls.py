from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.main', name='home'),
    url(r'^post/(post_id)','blog.views.post', name='post'),
    #(r"", "main"),
    url(r'^admin/', include(admin.site.urls)),
)
