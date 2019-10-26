from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^app-region$', views.app_region, name="app_region"),
    url(r'^app-region/app-tab-dj$', views.app_tab_region_dj, name="app_tab_region_dj"),
    url(r'^app-region/app-tab-sj$', views.app_tab_region_sj, name="app_tab_region_sj"),
    url(r'^app-region/app-tab-cn$', views.app_tab_region_cn, name="app_tab_region_cn"),
    url(r'^app-region/app-tab-cb$', views.app_tab_region_cb, name="app_tab_region_cb"),

    url(r'^app-grade-ja$', views.app_grade_ja, name="app_grade_ja"),
    url(r'^app-grade-ja/app-grade-ja-tab-2$', views.app_grade_ja_tab_2, name="app_grade_ja_tab_2"),
    url(r'^app-grade-ja/app-grade-ja-tab-3$', views.app_grade_ja_tab_3, name="app_grade_ja_tab_3"),
    url(r'^app-grade-ja/app-grade-ja-tab-4$', views.app_grade_ja_tab_4, name="app_grade_ja_tab_4"),
    url(r'^app-grade-ja/app-grade-ja-tab-5$', views.app_grade_ja_tab_5, name="app_grade_ja_tab_5"),
    url(r'^app-grade-ja/app-grade-ja-tab-6$', views.app_grade_ja_tab_6, name="app_grade_ja_tab_6"),
    url(r'^app-grade-ja/app-grade-ja-tab-7$', views.app_grade_ja_tab_7, name="app_grade_ja_tab_7"),
    url(r'^app-grade-ja/app-grade-ja-tab-8$', views.app_grade_ja_tab_8, name="app_grade_ja_tab_8"),

    url(r'^app-grade-in$', views.app_grade_in, name="app_grade_in"),
    url(r'^app-grade-in/app-tab-in-2$', views.app_tab_grade_in_2, name="app_tab_grade_in_2"),
    url(r'^app-grade-in/app-tab-in-3$', views.app_tab_grade_in_3, name="app_tab_grade_in_3"),
    url(r'^app-grade-in/app-tab-in-4$', views.app_tab_grade_in_4, name="app_tab_grade_in_4"),
    url(r'^app-grade-in/app-tab-in-5$', views.app_tab_grade_in_5, name="app_tab_grade_in_5"),
    url(r'^app-grade-in/app-tab-in-6$', views.app_tab_grade_in_6, name="app_tab_grade_in_6"),
    url(r'^app-grade-in/app-tab-in-7$', views.app_tab_grade_in_7, name="app_tab_grade_in_7"),
    url(r'^app-grade-in/app-tab-in-8$', views.app_tab_grade_in_8, name="app_tab_grade_in_8"),
]