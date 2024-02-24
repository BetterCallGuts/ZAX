from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urls = list(admin.site.urls)

urls[0] +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urls[0] +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ [
path('web/', include('core.urls')),
path('', admin.site.urls),
# path('', include(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))),
] 
admin.site.index_title = "Dashboard"
