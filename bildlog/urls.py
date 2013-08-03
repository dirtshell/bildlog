from django.conf.urls import patterns, include, url

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
    
    url(r'^$', 'bild.views.index', name="index"),                    # The index
    url(r'^signup/$', 'bildloguser.views.signup', name="signup"),            # The signup page
    url(r'^login/$', 'bildloguser.views.login_view', name="login"),    # The login page
    url(r'^logout/$', 'bildloguser.views.logout_view', name="logout"),  # The logout page
)
