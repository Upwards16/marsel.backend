from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/clients/', include('clients.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/cash/', include('cash.urls')),
    path('api/leads/', include('leads.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/time-sheets/', include('time_sheets.urls')),
    path('api/', include('analytics.urls')),
]
urlpatterns += doc_urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
