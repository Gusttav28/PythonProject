from django.urls import path, include
from . import views
from .views import index, UserViewSets
from rest_framework import routers
# from rest_framework.routers import DefaultRouter
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSets)
# router2 = DefaultRouter()
# router2.register('api/users', UserViewAPI, 'users')

urlpatterns = [
    path('', index),
    path('users/', include(router.urls)),
    path('schemas/<int:schema_id>/items/', DynamicItemView.as_view()),
    path('schemas/', DynamicSchemaView.as_view()),
]
    