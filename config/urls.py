from django.conf.urls import include, url
from django.contrib import admin
from config.views import HomeView
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^analysis/', include('analysis.urls')),
    url(r'^statistic/', include('statistic.urls')),

    url(r'^ajax/load_univ_name$', views.load_univ_name, name="ajax_load_univ_name"),
    url(r'^ajax/load_univ_major$', views.load_univ_major, name="ajax_load_univ_major"),
    url(r'^ajax/load_admission1$', views.load_admission1, name="ajax_load_admission1"),
    url(r'^ajax/load_admission2$', views.load_admission2, name="ajax_load_admission2"),

    url(r'^upload-csv1/', views.univ_data_upload1, name='univ_data_upload1'),
    url(r'^upload-csv2/', views.univ_data_upload2, name='univ_data_upload2'),
    url(r'^upload-csv3/', views.univ_data_upload3, name='univ_data_upload3'),
    url(r'^upload-csv4/', views.univ_data_upload4, name='univ_data_upload4'),
    url(r'^upload-csv5/', views.univ_data_upload5, name='univ_data_upload5'),
    url(r'^upload-csv6/', views.univ_data_upload6, name='univ_data_upload6'),
    url(r'^upload-csv7/', views.univ_data_upload7, name='univ_data_upload7'),
    url(r'^upload-csv8/', views.univ_data_upload8, name='univ_data_upload8'),
]
