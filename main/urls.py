from .admin import omar_admin_site
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urls = list(omar_admin_site.urls)

urls[0] +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urls[0] +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ [

path("manfu/", include("manufacturers.urls")),

path('', omar_admin_site.urls),

] 
omar_admin_site.index_title = "Dashboard"
# 0100 6086 528