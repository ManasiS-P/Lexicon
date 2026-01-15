from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$',views.register,name= 'register'),
    # url(r'^preview/(?P<user_id>\d+)/$', views.profile_preview, name='profile_preview'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    # url(r'^book/$',views.book,name= 'book'),
    # url(r'^about/$',views.about,name= 'about'),
]