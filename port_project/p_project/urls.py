from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from dict.views import pageNotFound
from p_project import settings

urlpatterns = [
    path('', include('dict.urls')),
    path('admin/', admin.site.urls),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 =pageNotFound




