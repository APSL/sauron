import json

from django.db import models
from channels import Group


class Toilet(models.Model):
    name = models.CharField(max_length=180)

    def __str__(self):
        return self.name


class ToiletLecture(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    in_use = models.BooleanField()
    toilet = models.ForeignKey(Toilet)

    def __str__(self):
        return '{} - {}'.format(self.toilet, self.created_at)

    @classmethod
    def last_lecture(cls):
        lecture = []
        for toilet in Toilet.objects.all():
            toilet_lecture = ToiletLecture.objects.filter(toilet=toilet).last()
            if toilet_lecture:
                lecture.append({'toilet_id': toilet.id, 'in_use': toilet_lecture.in_use,
                                'date': toilet_lecture.created_at.isoformat()})
        return lecture

    @classmethod
    def last_usage_time(cls, toilet_id):
        toilet_lecture_in_use = ToiletLecture.objects.filter(toilet_id=toilet_id, in_use=True).last()
        toilet_lecture_free = ToiletLecture.objects.filter(toilet_id=toilet_id, in_use=False).last()
        if toilet_lecture_in_use and toilet_lecture_free:
            return int((toilet_lecture_free.created_at - toilet_lecture_in_use.created_at).total_seconds())
        return

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Group("stream").send({"text": json.dumps(self.last_lecture())})
