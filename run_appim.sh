#!/usr/bin/env bash

docker run -d --name appium -p 4723:4723 --privileged -v /dev/bus/usb:/dev/bus/usb appium/appium