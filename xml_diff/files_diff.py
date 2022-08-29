import xml.etree.ElementTree as ET
import json
from xml_diff.tree import make_diff_tree
from xml_diff.itineraries import make_itineraries_tree


def xml_difference(file1_name, file2_name, output):
    itinenaries_data1 = ET.parse(file1_name).getroot()
    itinenaries_data2 = ET.parse(file2_name).getroot()
    itinenaries_tree1 = make_itineraries_tree(itinenaries_data1)
    itinenaries_tree2 = make_itineraries_tree(itinenaries_data2)
    difference_tree = make_diff_tree(itinenaries_tree1, itinenaries_tree2)
    with open(output, 'w') as write_file:
        write_file.write(json.dumps(difference_tree, indent=4))
