from django.urls import include, path
from rest_framework import routers
from ImageAlbum import views

router = routers.DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'images', views.ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
