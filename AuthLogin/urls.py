from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from Autenticacao.router import router
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/docs/schema/', SpectacularAPIView.as_view(), name='schema'),

    path('api/docs/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'
         ),

    path('api/docs/redoc/',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'
         ),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
]
