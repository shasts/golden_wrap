from django.conf.urls import patterns, include, url
from golden_wrap import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'golden_wrap.views.home', name='home'),
    url(r'^products/', include('golden_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', 'golden_app.views.contact'),
    url(r'^about/', 'golden_app.views.about'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:   
    url(r'^file_dir/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT})
)
