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
from goto import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    #Auth
    url(r'^signup/$', views.sign_up, name='sign_up'),
    url(r'^signin/$', views.sign_in, name='sign_in'),
    url(r'^signout/$', views.sign_out, name='sign_out'),

    #Events
    url(r'^upcoming/$', views.index, name='upcoming_events'),
    url(r'^archive/$', views.index, name='archive_events'),
    url(r'^event/?P<id>\d+/$', views.index, name='event_detail'),
    #Participant
    url(r'^participant/$', views.index, name='participants'),
    url(r'^participant/?P<id>\d+/$', views.index, name='participant_detail'),


    # url(r'^disconnect/$', views.disconnect, name='disconnect'),
    # url(r'^actions/sign_in/$', views.sign_in_action, name='sign_in_action'),
    # url(r'^actions/sign_up/$', views.sign_up_action, name='sign_up_action'),
    # url(r'^actions/sign_out/$', views.sign_out_action, name='sign_out_action'),
    # url(r'^profile/$', views.profile, name='profile'),
    # url(r'^about_us/$', views.about_us, name='about_us'),
    # url(r'^hack/$', views.hackathon, name='hakathon'),
    # url(r'^lecture/$', views.lecture, name='lecture'),
    # url(r'^camp/$', views.camp, name='camp'),
    # url(r'^actions/apply/$', views.apply, name='apply'),
    # url(r'^actions/subscribe/$', views.subscribe, name='subscribe_action'),
    # url(r'^actions/edit_profile/$', views.edit_profile_action, name='edit_profile_action'),
    # url(r'^actions/apply/$', views.apply, name='apply'),
    # url(r'^actions/refuse/$', views.refuse, name='refuse'),
    # url(r'^actions/write_comment_action/$', views.write_comment_action, name='write_comment_action'),
]
