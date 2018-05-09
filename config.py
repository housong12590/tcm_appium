import device
import os

apk_path = os.path.join(os.path.dirname(__file__), 'tcmlive.apk')

package_name = device.get_package_name(apk_path)

version = device.device_version()

device_name = device.device_id()

DESIRED_CAPS = {'platformName': 'Android',
                'platformVersion': version,
                'deviceName': device_name,
                'app': apk_path,
                'appPackage': package_name,
                'appActivity': '.project.activity.SplashActivity',
                'noReset': True
                }

print(DESIRED_CAPS)
