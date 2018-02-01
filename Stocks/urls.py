from django.conf.urls import url
from Stocks.views import index, center

urlpatterns = [
    url(r'^index/$', index),
    url(r'^center/$', center)
]