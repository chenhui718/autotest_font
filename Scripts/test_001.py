from base.driver import Driver
from base.pageFactory import PageFactory


class TestFont:

    def teardown_class(self):
        Driver.quit_app_driver()

    def test_font(self):
        # 点击设置
        PageFactory.get_setting().click_display_perform()
        # 修改字体大小为普通
        import time
        time.sleep(3)
        PageFactory.get_displaypage().click_font_perform()
        time.sleep(3)
        PageFactory.get_displaypage().click_common_perform()
        time.sleep(3)
        # 判断“普通两个字”在当前页面内
        assert '普通' in PageFactory.get_displaypage().common_exist_xpath()
