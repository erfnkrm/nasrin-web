from django.conf.urls import url
from django.http.request import MediaType
from basic_app import views

app_name = 'nasrin'

urlpatterns = [
    url(r'^education/$',views.education,name='education'),
    url(r'^experience/$',views.experience,name='experience'),
    url(r'media/$',views.media,name='media'),
]

