from page.pageElements import PageElements
from base.base import Base


class SettingPage(Base):
    # 初始化父类
    def __init__(self):
        super().__init__()

    def click_display_perform(self):
        # 点击设置按钮
        self.click_perform(PageElements.click_display_xpath)
