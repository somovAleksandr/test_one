from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisContactsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://sbis.ru/")

    def go_to_contacts(self):
        contacts_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Контакты"))
        )
        contacts_link.click()

    def click_tensor_banner(self):
        tensor_banner = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor"))
        )
        tensor_banner.click()