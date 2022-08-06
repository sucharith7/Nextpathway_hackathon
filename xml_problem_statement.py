import xml.etree.ElementTree as ET
mytree = ET.parse('wf_src_idw_cntry_multi_def_cd.xml')
myroot = mytree.getroot()

print(myroot.tag)
print(myroot.attrib)
for child in myroot:
    print(child.tag, child.attrib)

for transfromation in myroot.iter('TRANSFORMATION'):
    print(transfromation.attrib)

for TRANSFORMFIELD in myroot.iter('TRANSFORMFIELD'):
    print(TRANSFORMFIELD.attrib)

for task in myroot.iter('TASK'):
    print(task.attrib)

for INSTANCE in myroot.iter('INSTANCE'):
    print(INSTANCE.attrib)

for TABLEATTRIBUTE in myroot.iter('TABLEATTRIBUTE'):
    print(TABLEATTRIBUTE.attrib)


for CONNECTOR in myroot.iter('CONNECTOR'):
    print(CONNECTOR.attrib)

for mappings in myroot.iter('MAPPING'):
    print(mappings.attrib)

