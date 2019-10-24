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
    url(r'^app-grade-ja/app-tab-ja-4$', views.app_tab_grade_ja_4, name="app_tab_grade_ja_4"),
    url(r'^app-grade-ja/app-tab-ja-5$', views.app_tab_grade_ja_5, name="app_tab_grade_ja_5"),
    url(r'^app-grade-ja/app-tab-ja-6$', views.app_tab_grade_ja_6, name="app_tab_grade_ja_6"),
    url(r'^app-grade-ja/app-tab-ja-7$', views.app_tab_grade_ja_7, name="app_tab_grade_ja_7"),
    url(r'^app-grade-ja/app-tab-ja-8$', views.app_tab_grade_ja_8, name="app_tab_grade_ja_8"),

    url(r'^app-grade-in$', views.app_grade_in, name="app_grade_in"),
    url(r'^app-grade-in/app-tab-in-2$', views.app_tab_grade_in_2, name="app_tab_grade_in_2"),
    url(r'^app-grade-in/app-tab-in-3$', views.app_tab_grade_in_3, name="app_tab_grade_in_3"),
    url(r'^app-grade-in/app-tab-in-4$', views.app_tab_grade_in_4, name="app_tab_grade_in_4"),
    url(r'^app-grade-in/app-tab-in-5$', views.app_tab_grade_in_5, name="app_tab_grade_in_5"),
    url(r'^app-grade-in/app-tab-in-6$', views.app_tab_grade_in_6, name="app_tab_grade_in_6"),
    url(r'^app-grade-in/app-tab-in-7$', views.app_tab_grade_in_7, name="app_tab_grade_in_7"),
    url(r'^app-grade-in/app-tab-in-8$', views.app_tab_grade_in_8, name="app_tab_grade_in_8"),
]