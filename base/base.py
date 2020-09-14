from base.driver import Driver
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self):
        self.driver = Driver.get_app_driver()
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

# 启动设置
# 点击显示
# 修改字体大小为普通
# 判断“普通两个字”在当前页面内
# 要求封装在一个类里
