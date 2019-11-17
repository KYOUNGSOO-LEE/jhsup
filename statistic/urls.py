from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^app-region$', views.app_region, name="app_region"),
    url(r'^app-region/app-region-tab-dj$', views.app_region_tab_dj, name="app_region_tab_dj"),
    url(r'^app-region/app-region-tab-sj$', views.app_region_tab_sj, name="app_region_tab_sj"),
    url(r'^app-region/app-region-tab-cn$', views.app_region_tab_cn, name="app_region_tab_cn"),
    url(r'^app-region/app-region-tab-cb$', views.app_region_tab_cb, name="app_region_tab_cb"),

    url(r'^app-grade$', views.app_grade, name="app_grade"),
    url(r'^app-grade-search$', views.app_grade_search, name="app_grade_search"),
    url(r'^app-grade-ja/app-grade-search2$', views.app_grade_search2, name="app_grade_search2"),
    url(r'^app-grade-ja/app-grade-search3$', views.app_grade_search3, name="app_grade_search3"),
    url(r'^app-grade-ja/app-grade-search4$', views.app_grade_search4, name="app_grade_search4"),
    url(r'^app-grade-ja/app-grade-search5$', views.app_grade_search5, name="app_grade_search5"),
    url(r'^app-grade-ja/app-grade-search6$', views.app_grade_search6, name="app_grade_search6"),
    url(r'^app-grade-ja/app-grade-search7$', views.app_grade_search7, name="app_grade_search7"),
    url(r'^app-grade-ja/app-grade-search8$', views.app_grade_search8, name="app_grade_search8"),
]