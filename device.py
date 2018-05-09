import os
import re


def device_id():
    device_list = os.popen('adb devices').readlines()
    if device_list:
        return device_list[1].split('\t')[0]
    else:
        raise Exception('no equipment available')


def device_version():
    device_version_list = os.popen('adb shell getprop ro.build.version.release').readlines()
    if device_version_list:
        return device_version_list[0].split('\n')[0]
    else:
        raise Exception('no equipment available')


def get_package_name(path):
    apk_info = os.popen('aapt dump badging ' + path).readlines()
    if apk_info:
        return re.findall(r"(com.*?)'", apk_info[0])[0]
    else:
        raise Exception('apk not exist or path error')
