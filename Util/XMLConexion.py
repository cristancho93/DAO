from xml.etree import ElementTree

class XmlConexion:

    def __init__(self):
        self._mydoc = ElementTree.parse('sources/computador.xml')

    def get_conexion(self):
        self._mydoc = ElementTree.parse('sources/computador.xml')
        root = self._mydoc.getroot()
        result = root.findall('item')
        return root


