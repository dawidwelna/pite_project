from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^search_form/$', views.search_form),
    url(r'^searched/$', views.search),
    url(r'^searched/$', views.send_email),
]
