import xml.etree.ElementTree as ET

root = ET.parse('datei.xml').getroot()
print(root)
for type_tag in root.findall('klasse/name'):
    value = type_tag.get('I3A')
    print(value)