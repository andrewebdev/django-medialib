from django.conf.urls.defaults import *

urlpatterns = patterns('medialib.views',
    url(r'^browser/$', 'media_browser', name="medialib_media_browser"),
)
