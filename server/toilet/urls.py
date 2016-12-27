from django.conf.urls import url

from .views import ToiletsStatusView, ToiletsLastEventView, ToiletsLectureCreateAPIView, ToiletsLastLectureView, \
    ToiletLastUsageTimeView

urlpatterns = [
    url(r'^$', ToiletsStatusView.as_view(), name='toilets_status'),
    url(r'^toilets/last_event', ToiletsLastEventView.as_view(), name='toilets_last_event'),
    url(r'^toilets/last_lecture', ToiletsLastLectureView.as_view(), name='toilets_last_lecture'),
    url(r'^toilets', ToiletsLectureCreateAPIView.as_view(), name='toilets_lecture'),
    url(r'^toilet/(?P<pk>[0-9]+)/last_usage_time', ToiletLastUsageTimeView.as_view(), name='toilet_last_usage_time'),
]
