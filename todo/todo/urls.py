from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'todo_app.views.main', name='main'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    #url(r'^/register/$', 'django.contrib.auth.views.register''blog.views.user', {'template_name': 'register.html'}),
    url(r'^admin/', include(admin.site.urls)),
)
