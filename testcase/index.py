from appium.webdriver.webdriver import By
import time
import unittest
import HtmlTestRunner
from testcase import BaseCase


class AndroidTest(BaseCase):

    def test_mine(self):
        time.sleep(5)
        nav_views = self.driver.find_elements(By.ID, 'com.kexinbao100.tcmlive:id/ll_tab')
        self.driver.swipe(300, 1500, 300, 800)
        self.driver.swipe(300, 1500, 300, 800)
        time.sleep(2)
        for view in nav_views:
            time.sleep(1)
            view.click()
        time.sleep(5)

    def logout(self):
        pass


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='测试报告'))
