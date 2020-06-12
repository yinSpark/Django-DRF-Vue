from django.urls import path, include
from rest_framework.routers import DefaultRouter
from link import views

router = DefaultRouter()
router.register(r'snippets', views.LinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]