from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^app-region$', views.app_region, name="app_region"),
    url(r'^app-region/app-region-tab-dj$', views.app_region_tab_dj, name="app_region_tab_dj"),
    url(r'^app-region/app-region-tab-sj$', views.app_region_tab_sj, name="app_region_tab_sj"),
    url(r'^app-region/app-region-tab-cn$', views.app_region_tab_cn, name="app_region_tab_cn"),
    url(r'^app-region/app-region-tab-cb$', views.app_region_tab_cb, name="app_region_tab_cb"),

    url(r'^app-grade-ja$', views.app_grade_ja, name="app_grade_ja"),
    url(r'^app-grade-ja/app-grade-ja-tab-2$', views.app_grade_ja_tab_2, name="app_grade_ja_tab_2"),
    url(r'^app-grade-ja/app-grade-ja-tab-3$', views.app_grade_ja_tab_3, name="app_grade_ja_tab_3"),
    url(r'^app-grade-ja/app-grade-ja-tab-4$', views.app_grade_ja_tab_4, name="app_grade_ja_tab_4"),
    url(r'^app-grade-ja/app-grade-ja-tab-5$', views.app_grade_ja_tab_5, name="app_grade_ja_tab_5"),
    url(r'^app-grade-ja/app-grade-ja-tab-6$', views.app_grade_ja_tab_6, name="app_grade_ja_tab_6"),
    url(r'^app-grade-ja/app-grade-ja-tab-7$', views.app_grade_ja_tab_7, name="app_grade_ja_tab_7"),
    url(r'^app-grade-ja/app-grade-ja-tab-8$', views.app_grade_ja_tab_8, name="app_grade_ja_tab_8"),

    url(r'^app-grade-in$', views.app_grade_in, name="app_grade_in"),
    url(r'^app-grade-ja/app-grade-in-tab-2$', views.app_grade_in_tab_2, name="app_grade_in_tab_2"),
    url(r'^app-grade-ja/app-grade-in-tab-3$', views.app_grade_in_tab_3, name="app_grade_in_tab_3"),
    url(r'^app-grade-ja/app-grade-in-tab-4$', views.app_grade_in_tab_4, name="app_grade_in_tab_4"),
    url(r'^app-grade-ja/app-grade-in-tab-5$', views.app_grade_in_tab_5, name="app_grade_in_tab_5"),
    url(r'^app-grade-ja/app-grade-in-tab-6$', views.app_grade_in_tab_6, name="app_grade_in_tab_6"),
    url(r'^app-grade-ja/app-grade-in-tab-7$', views.app_grade_in_tab_7, name="app_grade_in_tab_7"),
    url(r'^app-grade-ja/app-grade-in-tab-8$', views.app_grade_in_tab_8, name="app_grade_in_tab_8"),

    url(r'^subject-grade$', views.subject_grade, name="subject_grade"),
]