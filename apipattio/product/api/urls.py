from django.conf.urls import url
from django.contrib import admin

from .views import (
  ProductListAPIView
)

urlpatterns = [
  url( '/', ProductListAPIView.as_view(), name='list')
]