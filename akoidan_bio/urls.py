from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from akoidan_bio import settings


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'akoidan_bio.views.home', name='home'),
    url(r'auth', 'akoidan_bio.views.auth'),
    url(r'request', 'akoidan_bio.views.requests'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form', 'akoidan_bio.views.change_form'),
    url(r'^register', 'akoidan_bio.views.register'),
    url(r'^logout/$', 'akoidan_bio.views.log_out'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Adds public access to PHOTO directory
