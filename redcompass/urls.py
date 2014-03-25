from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'redcompass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^compass/', include('compass.urls', namespace="compass")),
    url(r'^admin/', include(admin.site.urls)),
)
