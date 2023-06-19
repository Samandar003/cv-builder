import zipfile
import xml.etree.ElementTree as ET
import re
from lxml import etree
from zipfile import ZipFile, ZIP_DEFLATED
from main.models import ResumeModel, SampleResumeModel
from docx import Document

# file_path1 = "/home/samandar/Documents/RESUME_SAMANDAR_HH.docx"
# file_path2 = "/home/samandar/Documents/crill.docx"
# with zipfile.ZipFile(filepath) as docx:
        # Read the XML content of the document.xml file
        # xml_content = docx.read('word/document.xml')
        
def set_resume_data(s_data, sample):
    def change_data(data):
        new_data = re.sub(r"^name$", s_data.get("name"), data)
        new_data = re.sub(r"^surname$", s_data.get("surname"), new_data)
        new_data = re.sub(r"^occupation$", s_data.get("occupation"), new_data)
        new_data = re.sub(r"^myphone$", s_data.get("myphone"), new_data)
        new_data = re.sub(r"^myemail$", s_data.get("myemail"), new_data)
        new_data = re.sub(r"^mytelegram$", s_data.get("mytelegram"), new_data)
        new_data = re.sub(r"^mygithub$", s_data.get("mygithub"), new_data)
        new_data = re.sub(r"^mylinkedin$", s_data.get("mylinkedin"), new_data)
        new_data = re.sub(r"^myaddress$", s_data.get("myaddress"), new_data)
        new_data = re.sub(r"^start_job$", s_data.get("start_job"), new_data)
        new_data = re.sub(r"^end_job$", s_data.get("end_job"), new_data)
        new_data = re.sub(r"^job_role$", s_data.get("job_role"), new_data)
        new_data = re.sub(r"^workplace$", s_data.get("workplace"), new_data)
        new_data = re.sub(r"^work_description$", s_data.get("work_description"), new_data)
        new_data = re.sub(r"^about_me$", s_data.get("about_me"), new_data)
        new_data = re.sub(r"^job_role$", s_data.get("job_role"), new_data)
        new_data = re.sub(r"^project_1$", s_data.get("project_1"), new_data)
        new_data = re.sub(r"^project_1_description$", s_data.get("project_1_description"), new_data)
    
        new_data = re.sub(r"^project_2$", s_data.get("project_1"), new_data)
        new_data = re.sub(r"^project_2_description$", s_data.get("project_2_description"), new_data)
        
        new_data = re.sub(r"^project_3$", s_data.get("project_3"), new_data)
        new_data = re.sub(r"^project_3_description$", s_data.get("project_3_description"), new_data)
        
        new_data = re.sub(r"^project_4$", s_data.get("project_4"), new_data)
        new_data = re.sub(r"^project_4_description$", s_data.get("project_4_description"), new_data)
        
        new_data = re.sub(r"^skill_1$", s_data.get("skill_1"), new_data)
        new_data = re.sub(r"^skill_2$", s_data.get("skill_2"), new_data)
        
        new_data = re.sub(r"^skill_3$", s_data.get("skill_3"), new_data)
        
        new_data = re.sub(r"^edu_place_1$", s_data.get("edu_place_1"), new_data)
        new_data = re.sub(r"^course_and_duration$", s_data.get("course_and_duration"), new_data)
        new_data = re.sub(r"^edu_place_2$", s_data.get("edu_place_2"), new_data)
        new_data = re.sub(r"^course_and_duration_2$", s_data.get("course_and_duration_2"), new_data)
        
        new_data = re.sub(r"^language_1$", s_data.get("language_1"), new_data)
        new_data = re.sub(r"^level_1$", s_data.get("level_1"), new_data)
        new_data = re.sub(r"^language$", s_data.get("language_2"), new_data)
        new_data = re.sub(r"^level$", s_data.get("level_2"), new_data)
        
        new_data = re.sub(r"^hobby_1$", s_data.get("hobby_1"), new_data)
        new_data = re.sub(r"^hobby_2$", s_data.get("hobby_2"), new_data)
        return new_data
                
    def convert(match_obj):
                    data = match_obj.groupdict()
                    string_data = data['text'].decode()
                    result = change_data(string_data)
                    print(result)
                    return b"<w:t " + data['attrs'] + b">" + result.encode() + b"</w:t>"

    docfile = Document()
    docfile.save(f"media/files/{s_data['name'].title()}_CV.docx")
    outfile = ResumeModel.objects.create(file=f"files/{s_data['name'].title()}_CV.docx")
    outfile.save()
    with ZipFile(sample, 'r') as inzip, ZipFile(outfile, 'w', ZIP_DEFLATED) as outzip:
                for inzipinfo in inzip.infolist():
                    with inzip.open(inzipinfo) as infile:
                        if inzipinfo.filename == "word/document.xml":
                            new_content = re.sub(rb"<w:t(?P<attrs>[^>]*)>(?P<text>[^<]+)<\/w:t>", convert, infile.read())
                            outzip.writestr(inzipinfo.filename, new_content)
                        else:
                            outzip.writestr(inzipinfo.filename, infile.read())
                            