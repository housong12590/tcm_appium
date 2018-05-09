#!/usr/bin/env bash


docker run --privileged -d \
-p 6080:6080 -p 5554:5554 -p 5555:5555 -p 4723:4723 \
-e DEVICE = "Samsung Galaxy S6" \
-e APPIUM = True \
--name android-container \
butomo1989/docker-Android-x86-7.1.1