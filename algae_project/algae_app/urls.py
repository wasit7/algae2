from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^blank/$', views.blank, name='blank'),
	url(r'^images/$', views.images, name='images'),
	url(r'^water/$', views.water, name='water'),
	url(r'^prediction/$', views.prediction, name='prediction'),
	url(r'^recalls/$', views.RecallListView.as_view(), name='recall-list'),
]





