import json
import logging
import xml.etree.ElementTree as ET


import xmltodict


logger = logging.getLogger(__name__)


class XmlParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        # open the xml file
        # load the xml file and save it to self.data
        try:
            tree = ET.parse(file_path)
            data = tree.getroot()
            xml_string = ET.tostring(data, encoding="utf-8", method="xml")
            self.data = dict(xmltodict.parse(xml_string))

        except (Exception) as err:
            logger.exception(err)
            raise err

