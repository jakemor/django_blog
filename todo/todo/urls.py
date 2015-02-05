from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'todo_app.views.main', name='main'),
    url(r'^home/$', 'todo_app.views.main', name='main'),
    url(r'^logout/$', 'todo_app.views.user_logout'),
    url(r'^complete_todo/$', 'todo_app.views.complete_todo'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^register/$', 'todo_app.views.register', name='register'),
    url(r'^admin/', include(admin.site.urls)),

)
