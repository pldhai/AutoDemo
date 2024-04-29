import pytest
import os
import pytest_html
from selenium import webdriver
from components.basic_actions import MainDirectories
from components.basic_actions import BasicActions
from datetime import datetime

report_name = '~/Downloads/' + 'TestReport_' + BasicActions.convert_datetime(
    datetime.now())
report = report_name + ".html"
report_pdf = report_name + ".pdf"

@pytest.fixture(autouse=True, scope="session")
def setup_fixture():
    print('Setup App')
    # driver = webdriver.Chrome()
    # driver.implicitly_wait(10)
    # driver.maximize_window()
    # yield driver
    yield
    # driver.save_screenshot("todo-mvc.png")
    print('Close App')
    # driver.close()
    # driver.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # to remove environment section
    config._metadata = None
    config.option.htmlpath = report



@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == call:
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extras