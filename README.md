# cv-builder
you can build your own resume with this we app.

POST `localhost:8000/cv/`

Body:

```
{
    "name": [
        "This field is required."
    ],
    "surname": [
        "This field is required."
    ],
    "occupation": [
        "This field is required."
    ],
    "myphone": [
        "This field is required."
    ],
    "myemail": [
        "This field is required."
    ],
    "mytelegram": [
        "This field is required."
    ],
    "mygithub": [
        "This field is required."
    ],
    "mylinkedin": [
        "This field is required."
    ],
    "myaddress": [
        "This field is required."
    ],
    "start_job": [
        "This field is required."
    ],
    "end_job": [
        "This field is required."
    ],
    "workplace": [
        "This field is required."
    ],
    "work_description": [
        "This field is required."
    ],
    "about_me": [
        "This field is required."
    ],
    "job_role": [
        "This field is required."
    ],
    "project_1": [
        "This field is required."
    ],
    "project_1_description": [
        "This field is required."
    ],
    "project_2": [
        "This field is required."
    ],
    "project_2_description": [
        "This field is required."
    ],
    "project_3": [
        "This field is required."
    ],
    "project_3_description": [
        "This field is required."
    ],
    "project_4": [
        "This field is required."
    ],
    "project_4_description": [
        "This field is required."
    ],
    "skill_1": [
        "This field is required."
    ],
    "skill_2": [
        "This field is required."
    ],
    "skill_3": [
        "This field is required."
    ],
    "edu_place_1": [
        "This field is required."
    ],
    "course_and_duration": [
        "This field is required."
    ],
    "edu_place_2": [
        "This field is required."
    ],
    "course_and_duration_2": [
        "This field is required."
    ],
    "language_1": [
        "This field is required."
    ],
    "level_1": [
        "This field is required."
    ],
    "language_2": [
        "This field is required."
    ],
    "level_2": [
        "This field is required."
    ],
    "hobby_1": [
        "This field is required."
    ],
    "hobby_2": [
        "This field is required."
    ],
    "photo": [
        "No file was submitted."
    ]
}
```

Response:

```
"file":"{name}_CV.docx"
```
