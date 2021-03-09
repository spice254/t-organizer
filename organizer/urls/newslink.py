from django.conf.urls import url

from ..views import (
    NewsLinkCreate, NewsLinkDelete, NewsLinkUpdate)

urlpatterns = [
    url(r'^newslink/create/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'),
    url(r'^newslink/delete/(?P<pk>\d+)/$',
        NewsLinkDelete.as_view(),
        name='organizer_newslink_delete'),
    url(r'^newslink/update/(?P<pk>\d+)/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'),
]