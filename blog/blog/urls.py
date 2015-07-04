from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.urls import account_urls


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(account_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
