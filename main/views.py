from django.shortcuts import render
from rest_framework import views
from .serializers import ResumeSerializer
from rest_framework.views import APIView
from .models import CvPhotoModel
from .models import ResumeModel, PhotoModel

# Create your views here.
from . import utils
from rest_framework.response import Response

class ResumeAPIView(APIView):
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # obj = PhotoModel.objects.create(image=serializer.data['image'])
        # obj.save()
        serializer.save()
        # print(obj.image)

        print(serializer.data)
        # cv = utils.cv_build(serializer.data, obj.photo)
        return Response(serializer.data)

