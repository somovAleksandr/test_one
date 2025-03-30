import pytest
from selenium import webdriver
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def sbis_contacts_page(driver):
    return SbisContactsPage(driver)

@pytest.fixture(scope="function")
def tensor_main_page(driver):
    return TensorMainPage(driver)

@pytest.fixture(scope="function")
def tensor_about_page(driver):
    return TensorAboutPage(driver)