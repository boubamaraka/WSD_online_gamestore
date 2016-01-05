"""wsdgame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from gameshop import views
import gameshop
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$/',gameshop.views.index, name="index"),
    url(r'^home/$', gameshop.views.home),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
    #url(r'^registeruser/$', views.regist),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
