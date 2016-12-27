import json

from django.db import models
from channels import Group


class Toilet(models.Model):
    name = models.CharField(max_length=180)

    def __str__(self):
        return self.name


class ToiletLecture(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.CharField(choices=(('si', 'si'), ('no', 'no')), max_length=10)
    toilet = models.ForeignKey(Toilet)

    def __str__(self):
        return '{} - {}'.format(self.toilet, self.created_at)

    @classmethod
    def last_lecture(cls):
        lecture = []
        for toilet in Toilet.objects.all():
            toilet_lecture = ToiletLecture.objects.filter(toilet=toilet).last()
            if toilet_lecture:
                lecture.append({'toilet_id': toilet.id, 'value': toilet_lecture.value,
                                'date': toilet_lecture.created_at.isoformat()})
        return lecture

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Group("stream").send({"text": json.dumps(self.last_lecture())})
