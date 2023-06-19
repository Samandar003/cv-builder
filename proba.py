import zipfile
import xml.etree.ElementTree as ET
import re
from lxml import etree
from zipfile import ZipFile, ZIP_DEFLATED


file_path1 = "/home/samandar/Documents/RESUME_SAMANDAR_HH.docx"
file_path2 = "/home/samandar/Documents/crill.docx"
# with zipfile.ZipFile(filepath) as docx:
        # Read the XML content of the document.xml file
        # xml_content = docx.read('word/document.xml')
        
def set_resume_data(s_data):
    def change_data(data):
        new_data = re.sub(r"^name$", "Samandar", data)
        new_data = re.sub(r"^surname$", "Shoyimov", new_data)
        new_data = re.sub(r"^occupation$", "Web Python Back-end developer", new_data)
        new_data = re.sub(r"^myphone$", "+998942677005", new_data)
        new_data = re.sub(r"^myemail$", "samandar200527@gmail.com", new_data)
        new_data = re.sub(r"^mytelegram$", "t.me/SamandarShoyimov", new_data)
        new_data = re.sub(r"^mygithub$", "https://github.com/Samandar003", new_data)
        new_data = re.sub(r"^mylinkedin$", "https://www.linkedin.com/", new_data)
        new_data = re.sub(r"^myaddress$", "Tashkent city, yashnabod", new_data)
        new_data = re.sub(r"^start_job$", "02.08.2022", new_data)
        new_data = re.sub(r"^end_job$", "currently working", new_data)
        new_data = re.sub(r"^job_role$", "Back-End engineer", new_data)
        new_data = re.sub(r"^workplace$", "Digitial technologies and artificial intelligence research institute", new_data)
        new_data = re.sub(r"^work_description$", """I have been working here for almost 9 months. I built back-end side of tilim.uz, which is a functional web and mobile application. You can convert both text and documents(.docx, xlsx, .txt, .pptx) into either latin or cyrillic""", new_data)
        new_data = re.sub(r"^about_me$", """Currently, I am graduating high school, I intend to master my programming skills by studying at a prestigious university. Still, there is a room for improvement in my core skills, I hope higher education pave the way to a prospective career.""", new_data)
        new_data = re.sub(r"^job_role$", "Back-End engineer", new_data)
        new_data = re.sub(r"^project_1$", "tilim.uz", new_data)
        new_data = re.sub(r"^project_1_description$", "portfolio website for a journalist. ", new_data)
    
        new_data = re.sub(r"^project_2$", "http://34.31.99.198/docs/", new_data)
        new_data = re.sub(r"^project_2_description$", "Spotify api with comments, like, dislike and listen functions", new_data)
        
        new_data = re.sub(r"^project_3$", "http://34.72.245.120/", new_data)
        new_data = re.sub(r"^project_3_description$", "cv vuilder. Fill required fields, a download word file", new_data)
        
        new_data = re.sub(r"^project_4$", "http://34.121.251.33/", new_data)
        new_data = re.sub(r"^project_4_description$", "Ybky42 task", new_data)
        
        new_data = re.sub(r"^skill_1$", """Python, Django
        Django Rest Framework, OOP, 
        Java, HTML,""", new_data)
        
        
        new_data = re.sub(r"^skill_2$", """ REST  , Linux
        SQLite, PostgreSQL, TestCase, JWT,
        Postman, Unit Testing
    """, new_data)
        
        new_data = re.sub(r"^skill_3$", """ Team-work, Deployment
    Digital ocean, Ubuntu server
    Nginx/Gunicorn, 
    Google Cloud Console
    """, new_data)
        
        new_data = re.sub(r"^edu_place_1$", "PDP Academy", new_data)
        new_data = re.sub(r"^course_and_duration$", "Python Backend 07.07.2021 - 2022", new_data)
        new_data = re.sub(r"^edu_place_2$", "Vocational School No. 1, Computer technologies degree", new_data)
        new_data = re.sub(r"^course_and_duration_2$", "05.08.2021 - 02.07.2023", new_data)
        
        new_data = re.sub(r"^language_1$", "English", new_data)
        new_data = re.sub(r"^level_1$", "C1", new_data)
        new_data = re.sub(r"^language$", "Russian", new_data)
        new_data = re.sub(r"^level$", "A2", new_data)
        
        new_data = re.sub(r"^hobby_1$", "Footbal, Volleyball", new_data)
        new_data = re.sub(r"^hobby_2$", "Reading and algorithm", new_data)
        return new_data
                
    def convert(match_obj):
                    data = match_obj.groupdict()
                    string_data = data['text'].decode()
                    result = change_data(string_data)
                    print(result)
                    return b"<w:t " + data['attrs'] + b">" + result.encode() + b"</w:t>"


    with ZipFile(file_path1, 'r') as inzip, ZipFile(file_path2, 'w', ZIP_DEFLATED) as outzip:
                for inzipinfo in inzip.infolist():
                    with inzip.open(inzipinfo) as infile:
                        if inzipinfo.filename == "word/document.xml":
                            new_content = re.sub(rb"<w:t(?P<attrs>[^>]*)>(?P<text>[^<]+)<\/w:t>", convert, infile.read())
                            outzip.writestr(inzipinfo.filename, new_content)
                        else:
                            outzip.writestr(inzipinfo.filename, infile.read())
                            