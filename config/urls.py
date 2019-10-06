from django.conf.urls import include, url
from django.contrib import admin
from config.views import HomeView
from analysis.views import univ_data_upload1
from analysis.views import univ_data_upload2
from analysis.views import univ_data_upload3
from analysis.views import univ_data_upload4
from analysis.views import univ_data_upload5
from analysis.views import univ_data_upload6
from analysis.views import univ_data_upload7
from analysis.views import univ_data_upload8

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^analysis/', include('analysis.urls')),
    url(r'^upload-csv1/', univ_data_upload1, name='univ_data_upload1'),
    url(r'^upload-csv2/', univ_data_upload2, name='univ_data_upload2'),
    url(r'^upload-csv3/', univ_data_upload3, name='univ_data_upload3'),
    url(r'^upload-csv4/', univ_data_upload4, name='univ_data_upload4'),
    url(r'^upload-csv5/', univ_data_upload5, name='univ_data_upload5'),
    url(r'^upload-csv6/', univ_data_upload6, name='univ_data_upload6'),
    url(r'^upload-csv7/', univ_data_upload7, name='univ_data_upload7'),
    url(r'^upload-csv8/', univ_data_upload8, name='univ_data_upload8'),
]
