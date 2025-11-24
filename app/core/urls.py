from django.urls import path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)




urlpatterns = [
    path('', SpectacularSwaggerView.as_view(url_name='api-schema'),name='api-docs'),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema')
]