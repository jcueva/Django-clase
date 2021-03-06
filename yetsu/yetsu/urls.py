from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'principal.views.yetsu'),
    url(r'^posts/', 'principal.views.posts'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^simple/$','principal.views.simple'),
    url(r'^post/(?P<id_post>\d+)$','principal.views.detalle_post' ) ,
)
