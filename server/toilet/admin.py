from django.contrib import admin

from .models import ToiletLecture, Toilet


@admin.register(Toilet)
class ToiletAdmin(admin.ModelAdmin):
    pass


@admin.register(ToiletLecture)
class ToiletLectureAdmin(admin.ModelAdmin):
    list_display = ('toilet', 'start_at', 'end_at', 'total_time', )
