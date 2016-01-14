from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.mountain_range_list, name='mountain_range_list'),
    url(r'^mountain/(?P<pk>[0-9]+)/$', views.mountain_detail, name='mountain_detail'),
    url(r'^mountain/new_mountain/$', views.mountain_new, name='mountain_new'),
    url(r'^mountain/(?P<pk>[0-9]+)/edit/$', views.mountain_edit, name='mountain_edit'),
    url(r'^mountainrange/$', views.mountain_range_list, name='mountain_range_list'),
    url(r'^mountainrange/(?P<pk>[0-9]+)/$', views.mountain_range_detail, name='mountain_range_detail'),
    url(r'^mountainrange/new_mountain_range/$', views.mountain_range_new, name='mountain_range_new'),
    url(r'^mountain/$', views.mountain_list, name='mountain_list'),
    url(r'^mountain/advanced_search/$', views.mountain_advanced_search, name="mountain_advanced_search"),
    url(r'^mountain/results/$', views.mountain_results, name="mountain_results"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^mountain/see_marmot/$', views.see_marmot, name='see_marmot'),
]

