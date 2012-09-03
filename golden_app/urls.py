from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('golden_app.views',
	(r'^$', 'index'),
	(r'^(?P<product_id>\d+)/$', 'detail'),
	(r'^add/$', 'add_to_cart')	     
)
