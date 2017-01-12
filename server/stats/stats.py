from datetime import timedelta

from toilet.models import ToiletLecture, Toilet
from .utils import get_local_hour


def get_chart_values(hourly_values):
    values = {'hour_values': [], 'visit_values': [], 'time_values': []}
    for hourly_value in hourly_values:
        values['hour_values'].append(get_local_hour(int(hourly_value['hour'])))
        values['visit_values'].append(hourly_value['total_visits'])
        values['time_values'].append(round(hourly_value['total_time'].total_seconds() / 3600, 2))
    return values


def get_toilet_stats(days):
    # Remove lectures with a duration of less of 10 seconds
    tl = ToiletLecture.objects.filter(total_time__gte=timedelta(seconds=10))

    # Filter by days
    if days:
        tl = tl.by_days(days)

    # Get the summary and the hourly values of all the toilets
    stats = [{'name': 'All', 'summary': tl.get_summary(), 'chart_values': get_chart_values(tl.group_by_hours())}]

    # Get the summary and the hourly values of each toilet
    for toilet in Toilet.objects.all():
        tl_by_toilet = tl.filter(toilet=toilet)
        stats.append({'name': toilet.name, 'summary': tl_by_toilet.get_summary(),
                      'chart_values': get_chart_values(tl_by_toilet.group_by_hours())})
    return stats
