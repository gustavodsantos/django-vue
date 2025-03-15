from django.urls import include, path
from rest_framework import routers

from .views import CursoViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cursos', CursoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
