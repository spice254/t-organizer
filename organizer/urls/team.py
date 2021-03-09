from django.conf.urls import url

from ..views import (
    TeamCreate, TeamDelete, TeamUpdate,
    team_detail, team_list)

urlpatterns = [
    url(r'^$',
        team_list,
        name='organizer_team_list'),
    url(r'^create/$',
        TeamCreate.as_view(),
        name='organizer_team_create'),
    url(r'^(?P<slug>[\w\-]+)/$',
        team_detail,
        name='organizer_team_detail'),
    url(r'^(?P<slug>[\w\-]+)/delete/$',
        TeamDelete.as_view(),
        name='organizer_team_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$',
        TeamUpdate.as_view(),
        name='organizer_team_update'),
]