"""gotosite2 URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from goto import views, login_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^page/(?P<slug>[A-Za-z-]+)$', views.page, name='index'),
    # Auth
    url(r'^signup/$', login_views.sign_up, name='sign_up'),
    url(r'^signin/$', login_views.sign_in, name='sign_in'),
    url(r'^signout/$', login_views.sign_out, name='sign_out'),

    # Events
    url(r'^upcoming/$', views.upcoming, name='upcoming_events'),
    url(r'^archive/$', views.archive, name='archive_events'),
    url(r'^event/(?P<id>\d+)/$', views.event_by_id, name='event_detail'),

    url(r'^user/(?P<id>\d+)/$', views.user_by_id, name='user_detail'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
    # Participant
    url(r'^participants/$', views.participants, name='participants'),
    url(r'^experts/$', views.experts, name='experts'),
    url(r'^staff/', views.staff, name='staff'),

    url(r'^about-us/$', views.about_us, name='about_us'),

    # url(r'^actions/apply/$', views.apply, name='apply'),
    # url(r'^actions/subscribe/$', views.subscribe, name='subscribe_action'),
    # url(r'^actions/edit_profile/$', views.edit_profile_action, name='edit_profile_action'),
    # url(r'^actions/apply/$', views.apply, name='apply'),
    # url(r'^actions/refuse/$', views.refuse, name='refuse'),
    # url(r'^actions/write_comment_action/$', views.write_comment_action, name='write_comment_action'),
]
