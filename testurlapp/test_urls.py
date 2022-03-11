from django.urls import path, re_path
from testurlapp import views

urlpatterns = [
    # re_path(r'^user/(\d+)/$', views.home, name='home'),
    #site.com/user/12
    # re_path(r'^user/(\d{2})/(\d{4})/$', views.home, name='home'),
    #site.com/user/12/2000/

    re_path(r'^user/(?P<month>\d{2})/(?P<year>\d{4})/$', views.home, name='home'),
]