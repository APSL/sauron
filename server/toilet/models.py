import json
from datetime import timedelta

from django.db import models
from django.utils import timezone
from channels import Group

from .managers import ToiletLectureQuerySet


class Toilet(models.Model):
    name = models.CharField(max_length=180)

    def __str__(self):
        return self.name


class ToiletLecture(models.Model):
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(null=True, blank=True)
    total_time = models.DurationField(default=timedelta(seconds=0))
    toilet = models.ForeignKey(Toilet)

    objects = ToiletLectureQuerySet.as_manager()

    def __str__(self):
        return '{} - {}'.format(self.toilet, self.start_at)

    @classmethod
    def last_active_lecture(cls, toilet):
        return ToiletLecture.objects.filter(toilet=toilet, end_at__isnull=True).last()

    @classmethod
    def last_lectures(cls):
        lecture = []
        for toilet in Toilet.objects.all():
            toilet_lecture = ToiletLecture.objects.filter(toilet=toilet).last()
            if toilet_lecture:
                end_date = None
                if toilet_lecture.end_at:
                    end_date = toilet_lecture.end_at.isoformat()
                lecture.append({'toilet_id': toilet.id, 'in_use': not bool(toilet_lecture.end_at),
                                'start_at': toilet_lecture.start_at.isoformat(), 'end_at': end_date})
        return lecture

    @classmethod
    def last_usage_time(cls, toilet_id):
        last_toilet_lecture = ToiletLecture.objects.filter(toilet_id=toilet_id, end_at__isnull=False).last()
        if last_toilet_lecture:
            return last_toilet_lecture.total_time
        return

    def end_lecture(self):
        self.end_at = timezone.now()
        self.total_time = self.end_at - self.start_at
        self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Group("stream").send({"text": json.dumps(self.last_lectures())})
