from rest_framework import serializers


class ResumeSerializer(serializers.Serializer):
    photo = serializers.FileField(
        max_length = 10000000,
        allow_empty_file = False,
        use_url = False,)
  
    # Personal details
    name = serializers.CharField()
    address = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()

    # Add Links
    telegram = serializers.CharField()
    github = serializers.CharField()
    linkedin = serializers.CharField()
    website = serializers.CharField()

    # Education details
    edu_place = serializers.CharField()
    course = serializers.CharField()
    # start_date = serializers.CharField(required=True)
    # end_date = serializers.CharField(required=True)
    starting_date = serializers.CharField()
    ending_date = serializers.CharField()


    # Work experience
    job_role = serializers.CharField()
    work_place = serializers.CharField()
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    job_desc = serializers.CharField()

    # Skills
    skills = serializers.CharField()

    project1 = serializers.CharField()
    project2 = serializers.CharField()
    project3 = serializers.CharField(required=False)
    project4 = serializers.CharField(required=False)


    # certificates
    certificate1 = serializers.CharField()
    certificate2 = serializers.CharField(required=False)
    


