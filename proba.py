import zipfile
import xml.etree.ElementTree as ET
import re
from lxml import etree

filepath = "/home/legion/Documents/RESUME_SAMANDAR_HH.docx"
with zipfile.ZipFile(filepath) as docx:
        # Read the XML content of the document.xml file
        xml_content = docx.read('word/document.xml')
        print(xml_content)
        # new_content = re.match(rb"<w:t(?P<attrs>[^>]*)>(?P<text>[^<]+)<\/w:t>", xml_content)

        root = etree.fromstring(xml_content)
        text_data = []
        for paragraph in root.xpath('//w:p', namespaces=root.nsmap):
            paragraph_text = ''.join(run.text for run in paragraph.xpath('.//w:t', namespaces=paragraph.nsmap) if run.text)
            text_data.append(paragraph_text)
        print(text_data)




