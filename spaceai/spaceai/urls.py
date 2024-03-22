from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('home.urls','home'),namespace='spaceai')),
]

# If we are currently in DEBUG mode, we want to add the following two specific URL patterns.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
elif settings.DEBUG != True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 