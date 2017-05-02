from django.conf.urls import url

from .views import ToiletStatsView

urlpatterns = [
    url(r'^$', ToiletStatsView.as_view(), name='toilets_stats'),
]
