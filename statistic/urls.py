from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^statistic1$', views.statistic1, name="statistic1"),
]