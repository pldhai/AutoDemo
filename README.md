# DEMO AUTOMATION TESTSUITE

## 1. Setup
### Setup Python & Environment
- Setup [Python 3.11](https://www.python.org/downloads/)
- Install [VSCode](https://code.visualstudio.com/)
- Or [PyCharm](https://www.jetbrains.com/pycharm/download/)
- Create virtual env (https://docs.python.org/3/library/venv.html):
```commandline
    python3 -m pip install --user --upgrade pip
    python3 -m pip --version
    python3 -m pip install --user virtualenv
    python3 -m venv env
    source env/bin/activate
    which python
```
- Install required packages:
```commandline
    cd watchface-automation-testsuite
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
```
- To generate a requirements.txt file that lists all the packages and their versions installed in your virtual environment, you can use the following command:

```pip freeze > requirements.txt```

### install pytest package
```pip install pytest```

### install selenium
```pip install selenium```

### install requests library
```pip install requests```
```pip install jsonpath-ng```
```pip install jsonschema```

### instal pytest-html
```pip install pytest-html```

## 2. Pytest tutorial
### How to run `pytest` from `commandline`
```
pytest <path_to_file/folder>
pytest -k <contains_test_name/test_file>
pytest <path_to_file/folder> -s -v
```

### Adding ChromeDriver
- See [Instruction](https://webscraping.blog/chromedriver-executable-needs-to-be-in-path/)