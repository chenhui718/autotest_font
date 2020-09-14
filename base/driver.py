from appium import webdriver


class Driver:
    __app_driver = None

    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            # 如果__app_driver 为空 声明driver对象并返回
            desired_caps = {
                'platformName': 'Android',  # 平台
                'platformVersion': '5.1',  # 平台所属版本
                'deviceName': '192.168.56.101:5555',  # 设备名字 随便写
                'appPackage': 'com.android.settings',  # app包名
                'appActivity': '.Settings'  # app启动名
            }

            # 声明驱动对象 创建session 打开启动参数中指定的app
            cls.__app_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            return cls.__app_driver
        else:
            return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            # 退出
            cls.__app_driver.quit()  # 执行完退出后 __app_driver仍然为webelement对象
            # 手动重置为None
            cls.__app_driver = None
