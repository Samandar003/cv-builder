from django.shortcuts import render
from .serializers import CvPhotoSerializer, ResumeSerializer
from rest_framework.views import APIView
from .models import CvPhotoModel
from .models import ResumeModel

# Create your views here.
from . import utils
from rest_framework.response import Response

class ResumeAPIView(APIView):
    def post(self, request):
        serializer = CvPhotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        obj = CvPhotoModel.objects.get(id=serializer.data.get('id'))

        cv = utils.cv_build(serializer.data, obj.photo)
        fserializer = ResumeSerializer(cv)
        return Response(fserializer.data)

