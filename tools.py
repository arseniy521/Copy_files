import os
from xml.dom import minidom
import shutil
from pathlib import Path, PureWindowsPath
import lxml
from lxml import etree


def validate_config_file(config_file):
    try:
        xml_file = etree.parse(config_file)
        xml_validator = etree.XMLSchema(file="Schema.xsd")
        is_valid = xml_validator.validate(xml_file)
        if is_valid:
            print('- xml file is valid!')
            return True
        print('Error: xml file is not valid')
        return False
    except lxml.etree.XMLSyntaxError:
        print('Error: xml file is not valid')
        return False
    except OSError:
        print('Error: File ' + config_file + ' is not found or can not be accessed')
        return False


def parse_config_file(config_file):
    config_path = minidom.parse(config_file)
    file_tags = config_path.getElementsByTagName('file')
    return file_tags


def copy_files(file_path, destination_path):
    if not os.path.isdir(destination_path):
        print("Error: Destination path is not valid")
        return
    try:
        shutil.copy(file_path, destination_path)
        print("File Copied Successfully.")

    except FileNotFoundError:
        print("Error: Source path or file name is not valid.")
    except shutil.SameFileError:
        print('Error: Source and Target directories are the same.')
    except PermissionError:
        print("Error: You do not have permission for copy operation on the file.")


def fix_path(file, source_path):
    if '/' in source_path:
        # Create path object from linux os path type
        source_path = Path(file.attributes['source_path'].value + '/' + file.attributes['file_name'].value)
    else:
        # Create path object from windows os path type
        source_path = PureWindowsPath(file.attributes['source_path'].value + '\\' + file.attributes['file_name'].value)
    # Convert path type to the used system type
    return Path(source_path)
