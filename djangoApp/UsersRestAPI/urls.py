from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user_ocupation', views.OcupationViewSerializer)
router.register(r'table_schema', views.DynamicTableViewSerializer)
router.register(r'table_item', views.DynamicItemViewSerializer)

urlpatterns = [
    path('', include(router.urls)),
]