# Xml-parse
Xml-parse is a Python library that shows the difference between two files in xml-format, which contain information about itineraries and flights.

____

### CI:
[![Python CI](https://github.com/Dddarknight/project-xml-parse/actions/workflows/pyci.yml/badge.svg)](https://github.com/Dddarknight/project-xml-parse/actions)

### CodeClimate:
<a href="https://codeclimate.com/github/Dddarknight/project-xml-parse/maintainability"><img src="https://api.codeclimate.com/v1/badges/9003028ed64f6523c34e/maintainability" /></a>

<a href="https://codeclimate.com/github/Dddarknight/project-xml-parse/test_coverage"><img src="https://api.codeclimate.com/v1/badges/9003028ed64f6523c34e/test_coverage" /></a>

## Links
This project was built using these tools:
| Tool | Description |
|----------|---------|
| [poetry](https://python-poetry.org/) |  "Python dependency management and packaging made easy" |
| [Py.Test](https://pytest.org) | "A mature full-featured Python testing tool" |

## Description
Xml-parse is a CLI utility.
The result of compairing two files is written to output file, where you can see if itineraries were added, removed, the price difference, changes in flights' departure and arrival time.

## Installation
```
$ git clone git@github.com:Dddarknight/project-xml-parse.git
$ cd project-xml-parse
$ python3 -m pip install dist/hexlet_code-0.1.0-py3-none-any.whl
```

## Usage
```
$ xml-diff `file_path1` `file_path2` -o `output_file_path`

```

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)