from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorMainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def verify_url(self):
        self.wait.until(EC.url_to_be("https://tensor.ru/"))

    def find_strength_block(self):
        strength_block = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Сила в людях']"))
        )
        return strength_block.is_displayed()

    def click_more_details(self):
        more_details_link = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'
        )
        more_details_link.click()