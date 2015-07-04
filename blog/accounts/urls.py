from django.conf.urls import patterns, include, url
import views

account_urls =patterns('',
                url(r'^sign-in/$', views.signin, name='ref_login'),
                url(r'^sign-out/$',views.signout, name='ref_logout'),
                url(r'^register/$', views.signup, name='ref_signup'),
                )