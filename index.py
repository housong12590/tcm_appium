from appium import webdriver
from appium.webdriver.webdriver import By
import time
import os
import unittest
import HtmlTestRunner

apk_path = os.path.join(os.path.dirname(__file__), 'tcmlive.apk')

desired_caps = {'platformName': 'Android',
                'platformVersion': '7.1.1',
                'deviceName': 'c35ec84e',
                'app': apk_path,
                'appPackage': 'com.kexinbao100.tcmlive',
                'appActivity': '.project.activity.SplashActivity',
                'noReset': True
                }


class AndroidTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

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

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='测试报告'))
