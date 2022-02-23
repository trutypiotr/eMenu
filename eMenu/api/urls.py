from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('token-auth/', obtain_auth_token)
]

router = DefaultRouter()
router.register(r'menus', views.MenuViewSet, basename='menus')
router.register(r'image', views.DishImageViewSet, basename='image')
urlpatterns += router.urls
