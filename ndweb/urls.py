"""data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

from . import views
from data.views import dataHome
from people.views import peopleHome
from tools.views import toolsHome, toolPage

urlpatterns = [
  url(r'^data/', include('data.urls')),
  url(r'^people/', include('people.urls')),
  url(r'^tools/', include('tools.urls')),
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  url(r'^about/$', views.about, name='about'),
  url(r'^ui-kit.html$', views.uikit),

  # URL redirection for projects on old neurodata site.
  url(r'^array-tomography/?.*', RedirectView.as_view(url='/data/weiler14/', permanent=True)),
  url(r'^kasthuri11/?.*', RedirectView.as_view(url='/data/kasthuri15/', permanent=True)),
  url(r'^fly-medulla/?.*', RedirectView.as_view(url='/data/takemura13/', permanent=True)),
  url(r'^bhatla15/?.*', RedirectView.as_view(url='/data/bhatla15/', permanent=True)),
  url(r'^pristionchus-pacificus/?.*', RedirectView.as_view(url='/data/bumbarger13/', permanent=False)),
  url(r'^bock11/?.*', RedirectView.as_view(url='/data/bock11/', permanent=True)),

  # These are the expected paths but they are not populated?
  url(r'^hildebrand16/?.*', RedirectView.as_view(url='/data/hildebrand16/', permanent=True)),
  url(r'^wanner16/?.*', RedirectView.as_view(url='/data/wanner16/', permanent=True)),
  # lee16 is really tobin16
  url(r'^lee16/?.*', RedirectView.as_view(url='/data/tobin16/', permanent=True)),
  url(r'^tobin16/?.*', RedirectView.as_view(url='/data/tobin16/', permanent=True)),

  # These exist on the old site and may not have a new home yet
  url(r'^celegans/?.*', RedirectView.as_view(url='/data/', permanent=False)),
  url(r'^neural-behavior-maps/?.*', RedirectView.as_view(url='/data/', permanent=False)),
  url(r'^male-c-elegans/?.*', RedirectView.as_view(url='/data/', permanent=False)),


]
