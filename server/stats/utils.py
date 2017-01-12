from django.utils import timezone


def get_local_hour(hour):
    now = timezone.now()
    now = now.replace(hour=hour)
    tz = timezone.get_current_timezone()
    return now.astimezone(tz).hour
