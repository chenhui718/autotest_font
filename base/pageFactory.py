from page.settingPage import SettingPage
from page.displayPage import DispalyPage


class PageFactory:
    # 定义方法类
    @classmethod
    def get_setting(cls):
        return SettingPage()

    @classmethod
    # 定义方法类
    def get_displaypage(cls):
        return DispalyPage()
