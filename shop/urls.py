from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shop import views


router = routers.SimpleRouter()
router.register(r'product', views.ProductAPIView)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('firm/list/', views.FirmListCreateAPIView.as_view()),
    path('firm/<int:pk>/', views.FirmRetrieveUpdateDestroyAPIView.as_view()),
    path('cat/', views.CategoryAPIView.as_view()),
    path('cat/<int:pk>/', views.CategoryAPIView.as_view())
]