from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.api.urls')),
    path('notes/', include('notes.api.urls')),

    path('schema/', get_schema_view(title='API Docs', description='Noteneo app API'), name='api-schema'),
    path('docs/', include_docs_urls(title='API Docs'), name='docs'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

