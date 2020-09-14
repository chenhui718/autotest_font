from base.base import Base
from page.pageElements import PageElements


class DispalyPage(Base):
    # 初始化父类
    def __init__(self):
        super().__init__()

    def click_font_perform(self):
        self.click_perform(PageElements.click_font_xpath)

    def click_common_perform(self):
        self.click_perform(PageElements.click_common_xpath)

    def common_exist_xpath(self):
        res = self.location_eles(PageElements.common_exist_xpath)
        return [i.text for i in res]
