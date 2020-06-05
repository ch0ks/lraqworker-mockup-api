from django.conf.urls import url
from .views import BlogPostRudView, BlogPostAPIView
from .views import LRAQWorkerRudView,LRAQWorkerAPIView

urlpatterns = [
    # url(r'^$', BlogPostAPIView.as_view(), name='post-listcreate'),
    # url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name='post-rud')
    url(r'^$', LRAQWorkerAPIView.as_view(), name='lraqworker-listcreate'),
    url(r'^(?P<pk>\d+)/$', LRAQWorkerRudView.as_view(), name='lraqworker-rud')
]
