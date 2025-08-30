from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/accounts/', include('accounts.urls')),
    path('api/approvals/', include('approvals.urls')),
    path('api/departments/', include('departments.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('operations/', include('operations.urls')),
    path('uploads/', include('uploads.urls')),
]
