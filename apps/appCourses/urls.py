from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^add$',views.add),
    url(r'^remove/(?P<id>\d+)$',views.distroy),
    url(r'^confRem/(?P<id>\d+)$',views.confRem)
]
