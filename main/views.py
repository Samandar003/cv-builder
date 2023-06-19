from django.shortcuts import render
from rest_framework import views
from .serializers import ResumeSerializer
from .serializers import CvPhotoSerializer, ResumeSerializer
from rest_framework.views import APIView
from .models import CvPhotoModel
from .models import ResumeModel, SampleResumeModel
from django.shortcuts import render
# Create your views here.
from .. import proba
from django.http import HttpResponse
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

class CreateResumeAPIView(APIView):
    def post(self, request):
        serializer = CvPhotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        # obj = CvPhotoModel.objects.get(id=serializer.data.get('id'))
        sample = SampleResumeModel.objects.all().first()

        cv = proba.set_resume_data(serializer.data, sample.file)
        fserializer = ResumeSerializer(cv)
        return Response(fserializer.data)

def my_view(request):
    data = {}
    if request.method == "POST":
        # data['photo'] = request.FILES.get('photo')
        data['name'] = request.POST.get("name")
        data['address'] = request.POST.get('address')
        data['phone'] = request.POST.get('phone')
        data['email'] = request.POST.get('email')
        data['telegram'] = request.POST.get('telegram')
        data['github'] = request.POST.get('github')
        data['linkedin'] = request.POST.get('linkedin')
        data['website'] = request.POST.get('website')
        data['edu_place'] = request.POST.get('edu_place')
        data['course'] = request.POST.get('course')
        data['starting_date'] = request.POST.get('starting_date')
        data['ending_date'] = request.POST.get('ending_date')
        data['job_role'] = request.POST.get('job_role')
        data['work_place'] = request.POST.get('work_place')
        data['start_date'] = request.POST.get('start_date')
        data['end_date'] = request.POST.get('end_date')
        data['job_desc'] = request.POST.get('job_desc')
        data['skills'] = request.POST.get('skills')
        data['project1'] = request.POST.get('project1')
        data['project2'] = request.POST.get('project2')
        data['project3'] = request.POST.get('project3', '')
        data['project4'] = request.POST.get('project4', '')
        data['certificate1'] = request.POST.get('certificate1')
        data['certificate2'] = request.POST.get('certificate2', '')
        obj = CvPhotoModel.objects.create(photo=request.FILES.get("photo"))
        obj.save()
        cv = utils.cv_build(data, obj.photo)
        
        return render(request, 'view.html', {'cv':cv})
    return render(request, 'home.html')



