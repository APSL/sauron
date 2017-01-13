from rest_framework import serializers

from .models import ToiletLecture, Toilet


class ToiletLectureSerializer(serializers.Serializer):
    in_use = serializers.BooleanField()
    toilet = serializers.PrimaryKeyRelatedField(queryset=Toilet.objects.all())

    def save(self, **kwargs):
        toilet = self.validated_data['toilet']
        last_lecture = ToiletLecture.last_active_lecture(toilet)
        if self.validated_data['in_use']:
            if not last_lecture:
                ToiletLecture.objects.create(toilet=toilet)
        else:
            if last_lecture:
                last_lecture.end_lecture()
