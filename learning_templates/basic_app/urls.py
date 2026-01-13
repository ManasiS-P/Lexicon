from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^home/$',views.home,name= 'home'),
    url(r'^book/$',views.book,name= 'book'),
    url(r'^about/$',views.about,name= 'about'),
]