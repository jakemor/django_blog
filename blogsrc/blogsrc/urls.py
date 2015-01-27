from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.main', name='home'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/profile/$', 'blog.views.user', name='home'),

    # url(r'^blog/', include('blog.urls')),
    #(r"", "main"),
    url(r'^admin/', include(admin.site.urls)),
)
