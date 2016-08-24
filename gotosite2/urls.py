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
from django.conf.urls import url, include
from django.contrib import admin
from goto import views, login_views, subscribe_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^export/', views.export, name='export'),
    url(r'^admin-shortcuts/$', views.admin_shortcuts, name='admin_shortcuts'),

    url(r'^$', views.index, name='index'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^about-us/$', views.about_us, name='about_us'),
    url(r'^info/$', views.info, name='info'),
    url(r'^mm-about/$', views.mm_about, name='mm_about'),
    url(r'^page/(?P<slug>[A-Za-z-]+)$', views.page, name='page'),

    # Auth
    url(r'^signup/$', login_views.sign_up, name='sign_up'),
    url(r'^login/$', login_views.sign_in, name='sign_in'),
    url(r'^logout/$', login_views.sign_out, name='sign_out'),
    # url(r'^profile/$', views.profile, name='profile'),

    # Events
    url(r'^upcoming/$', views.upcoming, name='upcoming_events'),
    url(r'^schools/$', views.schools, name='schools'),
    url(r'^hackathons/$', views.hackathons, name='hackathons'),
    url(r'^lectures/$', views.lectures, name='lectures'),

    url(r'^archive/$', views.archive, name='archive_events'),
    url(r'^event/(?P<slug>[\w-]+)/$', views.event_by_id, name='event_detail'),
    url(r'^event/(?P<slug>[\w-]+)/participants$', views.event_participants, name='event_participants'),

    url(r'^application/fill/(?P<event_id>\d+)/$', views.application_fill,
        name='application_fill'),
    url(r'^application/(?P<id>\d+)/$', views.application, name='application'),
    url(r'^application/(?P<id>\d+)/(?P<method>\w*)$', views.application_change, name='application_change'),
    # Users
    url(r'^participants/$', views.participants, name='participants'),
    url(r'^experts/$', views.experts, name='experts'),
    url(r'^user/(?P<id>\d+)/$', views.user_by_id, name='user_detail'),
    # Projects
    url(r'^project/create$', views.project_create, name='project_create'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^project/(?P<id>\d+)/$', views.project_by_id, name='project_detail'),
    url(r'^project/edit/(?P<id>\d+)/$', views.project_edit, name='project_edit'),
    url(r'^project/delete/(?P<id>\d+)/$', views.project_delete, name='project_delete'),

    # Assignments
    url(r'^assignment/(?P<id>\d+)/$', views.assignment, name='assignment'),
    url(r'^assignment/apply/(?P<id>\d+)/$', views.apply_solution, name='apply_solution'),
    url(r'^solution/(?P<id>\d+)/$', views.view_solution, name='solution'),

    # Subscribe
    url(r'^subscribe/$', subscribe_views.subscribe, name='subscribe'),
    url(r'^unsubscribe/$', subscribe_views.unsubscribe, name='unsubscribe'),
    url(r'^askletter/(?P<emails>.+)/$', subscribe_views.ask_for_email, name='askletter')

    # url(r'^actions/apply/$', views.apply, name='apply'),
    # url(r'^actions/subscribe/$', views.subscribe, name='subscribe_action'),
    # url(r'^actions/edit_profile/$', views.edit_profile_action, name='edit_profile_action'),
    # url(r'^actions/apply/$', views.apply, name='apply'),
    # url(r'^actions/refuse/$', views.refuse, name='refuse'),
    # url(r'^actions/write_comment_action/$', views.write_comment_action, name='write_comment_action'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
