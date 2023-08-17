from pytest import fixture

from selenium import webdriver as wd


@fixture(scope='function')
def chrome_browser():
    browser_meta = wd.Chrome  # type 'abc.ABCMeta' (abstract base class)
    browser = browser_meta()  # type 'selenium.webdriver.chrome.webdriver.WebDriver'
    yield browser


@fixture(params=[wd.Chrome, wd.Firefox], scope='session')
def some_browser(request):
    browser = request.param()
    yield browser
    browser.quit()
