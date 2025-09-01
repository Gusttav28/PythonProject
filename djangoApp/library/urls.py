from django.urls import path, include
from . import views 
from rest_framework import routers

router1 = routers.DefaultRouter()
router2 = routers.DefaultRouter()
router3 = routers.DefaultRouter()
router4 = routers.DefaultRouter()
router1.register(r'Author', views.AuthorViewSerializer)
router2.register(r'Book', views.BookViewSerializer)
router3.register(r'Member', views.MemberViewSerializer)
router4.register(r'Loan', views.LoanViewSerializer)


urlpatterns = [
    path('', include(router1.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls)),
    path('', include(router4.urls)),
]
