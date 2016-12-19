from django.conf.urls import url

from .views import ToiletStatusView, ToiletLastEventView, ToiletLectureCreateAPIView, ToiletLastLectureView

urlpatterns = [
    url(r'^$', ToiletStatusView.as_view(), name='toilet_status'),
    url(r'^toilet_last_event', ToiletLastEventView.as_view(), name='toilet_last_event'),
    url(r'^toilet_lecture', ToiletLectureCreateAPIView.as_view(), name='toilet_lecture'),
    url(r'^toilet_last_lecture', ToiletLastLectureView.as_view(), name='toilet_last_lecture'),
]
