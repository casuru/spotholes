"""spotholes URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from potholes.views import ListPotholeView, PotholeDetailView, PotholeVoteView, PotholeByUserListView, PotholeReportView, PotholeReportDetailView
from authentication.views import AccountListView, AccountDetailView, AccountStatusView, SignInView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/signin', SignInView.as_view()),
    url(r'^api/v1/accounts/$', AccountListView.as_view(), name = 'account-list'),
    url(r'^api/v1/accounts/(?P<username>\w+)/$', AccountDetailView.as_view(), name = 'account-detail'),
    url(r'^api/v1/accounts/(?P<username>\w+)/status/$', AccountStatusView.as_view(), name = 'account-status'),
    url(r'^api/v1/accounts/(?P<username>\w+)/potholes/$', PotholeByUserListView.as_view(), name = 'pothole-account-list'),
    url(r'^api/v1/potholes/$', ListPotholeView.as_view(), name = 'pothole-list'),
    url(r'^api/v1/potholes/(?P<pk>[0-9]+)/$', PotholeDetailView.as_view(), name = 'pothole-detail'),
    url(r'^api/v1/potholes/(?P<pk>[0-9]+)/votes/$', PotholeVoteView.as_view(), name = 'vote-list'),
    url(r'^api/v1/potholes/(?P<pk>[0-9]+)/reports/$', PotholeReportView.as_view(), name = 'report-list'),
    url(r'^api/v1/potholes/(?P<p_pk>[0-9]+)/reports/(?P<r_pk>[0-9]+)/$', PotholeReportDetailView.as_view(), name = 'report-detail')
    
]
