from datetime import date, timedelta

from django.db import models
from django.db.models import Count, Avg, Max, Sum, DurationField
from postgres_stats import Percentile


class ToiletLectureQuerySet(models.QuerySet):
    metrics = {'total_time': Sum('total_time'), 'max_time': Max('total_time'), 'avg_time': Avg('total_time'),
               'total_visits': Count('id'), 'median_time': Percentile('total_time', 0.5, output_field=DurationField())}

    def by_days(self, days):
        today = date.today()
        return self.filter(start_at__date__lte=today, start_at__date__gte=today-timedelta(days=int(days)))

    def group_by_hours(self):
        return self.extra({'hour': "extract(hour from start_at)"}).order_by('hour').values('hour').annotate(
            total_visits=Count('id'), total_time=Sum('total_time'))

    def get_summary(self):
        return self.aggregate(**self.metrics)
