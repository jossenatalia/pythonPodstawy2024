import xml.etree.ElementTree as ET

def generateXML(filename):
    root = ET.Element('Catalog')

    m1 = ET.Element('mobile')
    root.append(m1)

    m2 = ET.Element('mobile')
    root.append(m2)

    b1 = ET.SubElement(m1, 'brand')
    b1.text = 'Apple'

    b2 = ET.SubElement(m1, 'price')
    b2.text = '6999'

    b3 = ET.SubElement(m2, 'brand')
    b3.text = 'Samsung'

    b4 = ET.SubElement(m2, 'price')
    b4.text = '3520'

    m2 = ET.Element('mobile')
    root.append(m2)

    tree = ET.ElementTree(root)

    with open(filename, 'wb') as f:
        tree.write(f)

generateXML("Catalog.xml")