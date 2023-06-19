from rest_framework import serializers
from .models import CvPhotoModel

class ResumeSerializer(serializers.ModelSerializer):
    image = serializers.FileField(
        max_length = 10000000,
        allow_empty_file = False,
        use_url = True,)
  
from .models import CvPhotoModel, ResumeModel

class CvPhotoSerializer(serializers.ModelSerializer):
    # photo = serializers.ImageField()

    # Personal details
    name = serializers.CharField()
    surname = serializers.CharField()
    
    occupation = serializers.CharField()
    myphone = serializers.CharField()
    myemail = serializers.CharField()
    mytelegram = serializers.CharField()
    mygithub = serializers.CharField()
    mylinkedin = serializers.CharField()
    myaddress = serializers.CharField()
    
    start_job = serializers.CharField()
    end_job = serializers.CharField()
    job_role = serializers.CharField()
    workplace = serializers.CharField()
    work_description = serializers.CharField()
    about_me = serializers.CharField()
    job_role = serializers.CharField()
    project_1 = serializers.CharField()
    project_1_description = serializers.CharField()
    project_2 = serializers.CharField()
    project_2_description = serializers.CharField()
    project_3 = serializers.CharField()
    project_3_description = serializers.CharField()
    project_4 = serializers.CharField()
    project_4_description = serializers.CharField()
    
    skill_1 = serializers.CharField()
    skill_2 = serializers.CharField()
    skill_3 = serializers.CharField()
    edu_place_1 = serializers.CharField()
    course_and_duration = serializers.CharField()
    edu_place_2 = serializers.CharField()
    course_and_duration_2 = serializers.CharField()
    language_1 = serializers.CharField()
    level_1 = serializers.CharField()
    language_2 = serializers.CharField()
    level_2 = serializers.CharField()
    hobby_1 = serializers.CharField()
    hobby_2 = serializers.CharField()      
          
    # Add Links
    class Meta:
        model = CvPhotoModel
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = ResumeModel
        fields = ['file']

