from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.full_list, name='full_list'),
	url(r'^page/(?P<pk>\d+)/$', views.standard_detail, name='page_detail'),
	url(r'^page/new/$', views.standard_new, name='page_new'),
	url(r'^page/(?P<pk>\d+)/edit/$', views.standard_edit, name='page_edit'),
	]