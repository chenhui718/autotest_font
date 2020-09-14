from selenium.webdriver.common.by import By


class PageElements:

    click_display_xpath = (By.XPATH, '//*[contains(@text,"显示")]')
    click_font_xpath = (By.XPATH, '//*[contains(@text,"字体大小")]')
    click_common_xpath = (By.XPATH, '//*[contains(@text,"普通")]')
    common_exist_xpath = (By.ID, 'android:id/summary')
