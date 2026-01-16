from django.conf.urls import url
from main_app import views

app_name = 'main_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^postlist/$', views.post_list, name='post_list'),
    url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^profile/$', views.profile, name='profile'),  # for logged-in users
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^profile_preview/(?P<user_id>\d+)/$', views.profile_preview, name='profile_preview'),  # optional
]
