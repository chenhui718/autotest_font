from appium import webdriver
import time

# 启动设置
# 点击显示
# 修改字体大小为普通
# 判断“普通两个字”在当前页面内
# 要求封装在一个类里
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestFontSize(object):
    def __init__(self):
        self.driver = driver
        # 如果__app_driver 为空 声明driver对象并返回

    # 定义一个显式等待定位元素的方法
    def location_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        :param loc: loc是组数字，放在元组里loc=（by=By.ID,value）,
        :param timeout: 可以自定义，默认函数
        :param poll_frequency:可以自定义，默认函数
        :return: 返回定位对象
        """
        # 导入显式等待类
        # 定位元素的方法采用By类，可以不指定定位元素的方法，如下所示
        # self.driver.find_element(loc[0], loc[1]) = self.driver.find_element(*loc)
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))
        # WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element())

    def location_eles(self, loc, timeout=5, poll_frequency=1.0):
        """返回一个列表"""
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    # 定义一个点击类
    def click_perform(self, loc, timeout=5, poll_frequency=1.0):
        self.location_ele(loc, timeout, poll_frequency).click()

    def text_list(self, loc, timeout=5, poll_frequency=1.0):
        # 返回一个列表
        return self.location_eles(loc, timeout, poll_frequency)


if __name__ == '__main__':
    desired_caps = {
        'platformName': 'Android',  # 平台
        'platformVersion': '5.1',  # 平台所属版本
        'deviceName': '192.168.56.101:5555',  # 设备名字 随便写
        'appPackage': 'com.android.settings',  # app包名
        'appActivity': '.Settings'  # app启动名
    }
    # 声明驱动对象 创建session 打开启动参数中指定的app
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # 启动设置
    # 点击显示
    import time

    fontsize = TestFontSize(driver)
    click_display = (By.XPATH, '//*[contains(@text,"显示")]')
    fontsize.click_perform(click_display)
    # 修改字体大小为普通
    click_font = (By.XPATH, '//*[contains(@text,"字体大小")]')
    fontsize.click_perform(click_font)
    time.sleep(2)
    click_common = (By.XPATH, '//*[contains(@text,"普通")]')
    fontsize.click_perform(click_common)
    time.sleep(2)
    # 判断“普通两个字”在当前页面内
    common_exist = (By.ID, 'android:id/summary')
    res = fontsize.text_list(common_exist)
    for i in res:
        if i.text == '普通':
            print('存在')
    # 要求封装在一个类里
