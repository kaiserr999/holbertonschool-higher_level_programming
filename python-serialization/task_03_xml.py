import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to the given filename.
    """
    if dictionary is None:
        return
        
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Reads XML data from a file, and returns a deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}
    except Exception:
        return None
