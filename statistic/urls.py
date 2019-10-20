from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^num_application$', views.num_application, name="num_application"),
]