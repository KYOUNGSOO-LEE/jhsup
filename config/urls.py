from django.conf.urls import include, url
from django.contrib import admin
from config.views import HomeView
from analysis.views import student_data_upload

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^analysis/', include('analysis.urls')),
    url(r'^upload-csv/', student_data_upload, name='student_data_upload'),
]
