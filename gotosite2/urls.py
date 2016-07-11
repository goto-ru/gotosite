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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^about-us/$', views.about_us, name='about_us'),
    url(r'^contacts/$', views.about_us, name='contacts'),
    url(r'^page/(?P<slug>[A-Za-z-]+)$', views.page, name='index'),

    # Auth
    url(r'^signup/$', login_views.sign_up, name='sign_up'),
    url(r'^signin/$', login_views.sign_in, name='sign_in'),
    url(r'^signout/$', login_views.sign_out, name='sign_out'),
    # url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),

    # Events
    url(r'^upcoming/$', views.upcoming, name='upcoming_events'),
    url(r'^archive/$', views.archive, name='archive_events'),
    url(r'^event/(?P<id>\d+)/$', views.event_by_id, name='event_detail'),
    url(r'^application/fill/(?P<event_id>\d+)/$', views.application_fill, name='application_fill'),
    url(r'^application/(?P<id>\d+)/$', views.application, name='application'),
    # Users
    url(r'^participants/$', views.participants, name='participants'),
    url(r'^experts/$', views.experts, name='experts'),
    url(r'^user/(?P<id>\d+)/$', views.user_by_id, name='user_detail'),
    # Projects
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^project/(?P<id>\d+)/$', views.project_by_id, name='project_detail'),
    # Assignments
    url(r'^assignment/(?P<id>\d+)/$', views.assignment, name='assignment'),
    url(r'^assignment/apply/(?P<id>\d+)/$', views.apply_solution, name='apply_solution'),
    url(r'^solution/(?P<id>\d+)/$', views.view_solution, name='solution'),

    # url(r'^actions/apply/$', views.apply, name='apply'),
    # url(r'^actions/subscribe/$', views.subscribe, name='subscribe_action'),
    # url(r'^actions/edit_profile/$', views.edit_profile_action, name='edit_profile_action'),
    # url(r'^actions/apply/$', views.apply, name='apply'),
    # url(r'^actions/refuse/$', views.refuse, name='refuse'),
    # url(r'^actions/write_comment_action/$', views.write_comment_action, name='write_comment_action'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
