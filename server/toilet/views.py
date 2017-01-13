import json

from django.conf import settings
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from channels import Group
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ToiletLectureSerializer
from .models import ToiletLecture, Toilet


class ToiletsStatusView(TemplateView):
    template_name = 'toilet_status.html'

    def get_context_data(self, **kwargs):
        context = super(ToiletsStatusView, self).get_context_data(**kwargs)
        context['toilets'] = Toilet.objects.all()
        context['ws_host'] = settings.WEB_SOCKET_HOST
        return context


class ToiletsLastEventView(View):

    def get(self, request, *args, **kwargs):
        Group("stream").send({"text": json.dumps(ToiletLecture.last_lectures())})
        return HttpResponse()


class ToiletsLectureAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ToiletLectureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(None, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ToiletsLastLectureView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return Response(ToiletLecture.last_lectures())


class ToiletLastUsageTimeView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return Response({'usage_time': ToiletLecture.last_usage_time(toilet_id=self.kwargs['pk'])})
