import debug_toolbar
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('user/', include("user.urls")),
    path('test/', include('testapp.urls')),
    path('', include("news.urls")),
    path('captcha/', include('captcha.urls')),

]

if settings.DEBUG:
    urlpatterns = [
                       path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


