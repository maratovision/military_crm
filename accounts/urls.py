from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('register', RegisterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dossier/', DossierModelViewSet.as_view(), name='dossier')
]