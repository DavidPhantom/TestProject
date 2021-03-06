"""TestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from authapp import views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='index'),
    re_path(r'^$', views.home, name='home'),
    re_path(r'authapp/login/$', auth_views.LoginView.as_view(template_name='authapp/login.html'),
            name='authapp-login'),
    re_path(r'authapp/logout/$', auth_views.LogoutView.as_view(next_page='/'),
            name='authapp-logout'),
    re_path(r'authapp/$', views.authapp_home, name='authapp-home'),

    re_path(r'^authapp/sign-up', views.authapp_sign_up, name='authapp-sign-up'),

    # re_path(r'^(?P<pizza_id>\d+)/$', views.pizza_detail, name='pizza_detail'),
    # path('test_app/', include('testurlapp.test_urls')),
    # re_path(r'formpage/', views.form_page, name='form_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
