from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^app-region$', views.app_region, name="app_region"),
    url(r'^app-region/app-tab-dj$', views.app_tap_region_dj, name="app_tap_region_dj"),
    url(r'^app-region/app-tab-sj$', views.app_tap_region_sj, name="app_tap_region_sj"),
    url(r'^app-region/app-tab-cn$', views.app_tap_region_cn, name="app_tap_region_cn"),
    url(r'^app-region/app-tab-cb$', views.app_tap_region_cb, name="app_tap_region_cb"),
]