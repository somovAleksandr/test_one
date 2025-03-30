import pytest
from selenium import webdriver
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage

@pytest.mark.sbis
def test_scenario():
    driver = webdriver.Chrome()

    try:
        sbis_contacts_page = SbisContactsPage(driver)
        tensor_main_page = TensorMainPage(driver)
        tensor_about_page = TensorAboutPage(driver)

        # 1. Переходим на https://sbis.ru/ в раздел "Контакты"
        sbis_contacts_page.open()
        sbis_contacts_page.go_to_contacts()

        # 2. Находим баннер Тензор, кликнуть по нему
        sbis_contacts_page.click_tensor_banner()

        # 3. Проверка, что открылся сайт https://tensor.ru/
        tensor_main_page.switch_to_new_tab()
        tensor_main_page.verify_url()

        # 4. Находим блок "Сила в людях"
        assert tensor_main_page.find_strength_block()

        # 5. Переходим в этом блоке в "Подробнее" и проверить URL
        tensor_main_page.click_more_details()
        assert "https://tensor.ru/about" in driver.current_url

        # 6. Проверка размеров фотографий в разделе "Работаем"
        tensor_about_page.verify_work_section_images()

    finally:
        driver.quit()