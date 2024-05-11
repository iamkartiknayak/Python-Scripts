# script to convert svg to xml image assets of android studio

import os
import xml.etree.ElementTree as ET


def create_xml_dir() -> None:
    dir_name = "xmls"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def get_formatted_xml(pathData) -> str:
    return f"""<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="512dp"
    android:height="512dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
  <path
      android:fillColor="#FF000000"
      android:pathData="{pathData}"/>
</vector>  
"""


def convert_svg_to_xml(svg_file: str, xml_file: str):
    path_data: str = get_path_data(svg_file)
    formatted_xml: str = get_formatted_xml(path_data)

    print(formatted_xml)

    with open(xml_file, "w") as xml:
        xml.write(formatted_xml)


def get_path_data(svg_file) -> str:
    tree = ET.parse(svg_file)
    root = tree.getroot()

    for path in root.findall(".//{http://www.w3.org/2000/svg}path"):
        return path.get("d")


def move_xml_files_to_xmls_dir() -> None:
    for file in os.listdir():
        if file.endswith(".xml"):
            os.system(f"mv {file} xmls")


def main():
    create_xml_dir()
    for file in os.listdir():
        if file.endswith(".svg"):
            svg_file: str = file  # file_name.svg
            xml_file: str = file.split(".")[0] + ".xml"  # file_name.xml
            convert_svg_to_xml(svg_file, xml_file)

    move_xml_files_to_xmls_dir()


if __name__ == "__main__":
    main()
