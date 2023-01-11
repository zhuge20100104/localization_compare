import os
import xml.etree.ElementTree as ET

from androguard.core.bytecodes import apk, axml
from androguard.core.bytecodes.apk import APK

spec_lan = '\x00\x00'
spec_lan_map = {'\x00\x00': "en"}

def parse_xml(source_):
    e_tree = ET.parse(source_)
    root = e_tree.getroot()
    children = root.getchildren()
    data_list = list()
    
    for child in children:
        if child.text is not None:
            data_list.append([child.get('name'), child.text])
        else:
            it = child.itertext()
            value = ""
           
            if len(child.getchildren()) == 0:
                data_list.append([child.get('name'), value])
                continue
            tag_name = child.getchildren()[0].tag
            i = 0
            for text_piece in it:
                if i==0:
                    value += "<" + tag_name + ">"
                value += text_piece
                if i==0:
                    value += "</" + tag_name + ">"
                i+=1
            data_list.append([child.get('name'), value])
    return data_list

def test_arsc():
    a = apk.APK("pangu.apk")
    arsc = a.get_android_resources()
    p = arsc.get_packages_names()[0]
    locales = arsc.get_locales(p)
    print(p)
    print(locales)  

    if not os.path.exists("xml_res"):
        os.makedirs("xml_res")

    for lan in locales:
        resources = arsc.get_string_resources(p, lan)
        prefix = lan 
        if lan == spec_lan:
            prefix = spec_lan_map[lan]
        xml_tmp_file_path = os.path.join("xml_res", prefix + "_result.xml")
        with open(xml_tmp_file_path, "wb") as f:
            f.write(resources)
        f.close()
        res = parse_xml(xml_tmp_file_path)

    # print("Result==================================: ")
    # print(res)
