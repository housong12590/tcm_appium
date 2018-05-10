import device
import os
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = {'platformName': 'Android',
                'platformVersion': device.device_version(),
                'deviceName': device.device_id(),
                'app': PATH('../apks/tcmlive.apk'),
                'appPackage': 'com.kexinbao100.tcmlive',
                'appActivity': '.project.activity.SplashActivity',
                'noReset': True
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
