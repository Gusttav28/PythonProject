from django.urls import path, include
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user_ocupation', views.OcupationViewSerializer)

urlpatterns = [
    path('', include(router.urls))
]