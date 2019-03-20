from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from apps.bids.views import BidViewSet

urlpatterns = [
    url(r'^api/bid/(?P<pk>\d+)/$', BidViewSet.as_view({
        'get': 'retrieve',   
        'delete': 'destroy',
        'patch': 'partial_update',
    })),
    url(r'^api/request/(?P<pk>\d+)/bids/$', BidViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
