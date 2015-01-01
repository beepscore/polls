from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )

# http://stackoverflow.com/questions/4938491/django-admin-change-header-django-administration-text
# django.contrib.admin.AdminSite.site_header
admin.site.site_header = 'Polls administration'
