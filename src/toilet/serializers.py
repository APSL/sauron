from rest_framework import serializers

from .models import ToiletLecture


class ToiletLectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToiletLecture
