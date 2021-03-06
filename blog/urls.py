from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^authors/$', views.authors, name='authors'),
    # url(r'^post/(?P<pk>[0-9a-fA-F]*)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    # url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    # url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    # url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^about/$', views.about, name='about'),
    url(r'^home/$', views.home, name='home'),
    # url(r'^search/$', views.search, name='search'),
]
