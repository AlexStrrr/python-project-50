## "Difference Generator" is the second learning project on [Hexlet.io](https://ru.hexlet.io).
___

### Hexlet tests and linter status:
[![Actions Status](https://github.com/AlexStrrr/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/AlexStrrr/python-project-50/actions)

### Github Actions
[![Python CI](https://github.com/AlexStrrr/python-project-50/actions/workflows/PyCI.yml/badge.svg)](https://github.com/AlexStrrr/python-project-50/actions/workflows/PyCI.yml)

### Code Climate
<a href="https://codeclimate.com/github/AlexStrrr/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/336a6da224c307d81245/maintainability" /></a>

### Test coverage
<a href="https://codeclimate.com/github/AlexStrrr/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/336a6da224c307d81245/test_coverage" /></a>

___


### Difference Generator is a program to find differences between two files.

* Used file formats: YAML, JSON.
* Possible report formats: Plain text, 'Stylish' text, JSON file (you need to choose one of the options).
* You can use Difference Generator as CLI tool or external library.

### Download the repository to try:

```bash
git clone https://github.com/AlexStrrr/python-project-50.git
```

```bash
make
```

You can get help about the utility using the command:

```bash
poetry run gendiff --help
```

```bash
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output ("Plain" or "JSON" or default: "Stylish")
```

### Demonstra
