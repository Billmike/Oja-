from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
 

from .views import (post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	view_profile,
    send_quotes,
    farmer_dashboard,
    sign_up,
    farmer_sign,
    ChartData,
    ChartView,
    temp_view,)
urlpatterns = [
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/edit/$', post_update, name="update"),
    url(r'^delete/$', post_delete),
    url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
    url(r'^profile/$', view_profile, name="profile"),
    url(r'^send_quotes/$', send_quotes),
    url(r'^dashboard/$', farmer_dashboard),
    url(r'^sign_up/$', sign_up),
    url(r'^real_sign_up/$', farmer_sign),
    url(r'^login/$', login, {'template_name': 'farmer_login.html/'}),
    url(r'^logout/$', logout, {'template_name': 'farmer_logout.html/'}),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^sales_chart/$', ChartView.as_view()),
    url(r'^tempdb/$', temp_view),
]
