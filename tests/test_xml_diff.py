import tempfile
import os
from xml_diff import xml_difference


def get_fixture_path(name):
    return os.path.join('tests/fixtures', name)


def make_set_from_lines(result):
    required_set = set()
    for line in result:
        line_corr = line.strip('\n')
        required_set.add(line_corr)
    return required_set


def test_xml_diff():
    temp_dir = tempfile.TemporaryDirectory(dir=os.getcwd())
    file_path = os.path.join(temp_dir.name, 'file_result')
    xml_difference(get_fixture_path('fixture1.xml'), get_fixture_path('fixture2.xml'), file_path)
    with open(get_fixture_path('result_min.json')) as expected:
        with open(file_path) as read_file:
            assert make_set_from_lines(expected.read()) == make_set_from_lines(read_file.read())
