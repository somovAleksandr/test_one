from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorAboutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_work_section_images(self):
        work_section = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div[4]'))
        )
        images = work_section.find_elements(By.TAG_NAME, "img")
        first_image_size = images[0].size
        for image in images:
            assert image.size == first_image_size