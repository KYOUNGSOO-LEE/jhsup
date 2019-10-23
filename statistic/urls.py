from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^app-region$', views.app_region, name="app_region"),
    url(r'^app-region/app-tab-dj$', views.app_tab_region_dj, name="app_tab_region_dj"),
    url(r'^app-region/app-tab-sj$', views.app_tab_region_sj, name="app_tab_region_sj"),
    url(r'^app-region/app-tab-cn$', views.app_tab_region_cn, name="app_tab_region_cn"),
    url(r'^app-region/app-tab-cb$', views.app_tab_region_cb, name="app_tab_region_cb"),

    url(r'^app-grade-ja$', views.app_grade_ja, name="app_grade_ja"),
    url(r'^app-grade-ja/app-tab-ja-2$', views.app_tab_grade_ja_2, name="app_tab_grade_ja_2"),
    url(r'^app-grade-ja/app-tab-ja-3$', views.app_tab_grade_ja_3, name="app_tab_grade_ja_3"),
]