from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Index.as_view()),
    url(r'^subd_postgresql$', Subd_postgres.as_view()),
    url(r'^subd_mysql$', Subd_mysql.as_view()),
]
