from django.conf.urls import patterns, include, url
import re

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bildlog.views.home', name='home'),
    # url(r'^bildlog/', include('bildlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'bildcontrols.views.index', name="index"),                       # The index
    url(r'^signup/$', 'bildloguser.views.signup', name="signup"),               # The signup page
    url(r'^login/$', 'bildloguser.views.login_view', name="login"),             # The login page
    url(r'^logout/$', 'bildloguser.views.logout_view', name="logout"),          # The logout page
    url(r'^createBild/$', 'bildcontrols.views.createBild', name="createBild"),  # Bild creation form is submitted here
    url(r'^createLog/$', 'bildcontrols.views.createLog', name="createLog"),     # Log creation form is submitted here
    url(r'^(?P<username>\S{,30})/$', 'bildloguser.views.view_user_profile', name="view_user_profile"), # View a users profile (usernames have a max length of 30 chars) THIS  NEEDS TO BE AT THE END
)
