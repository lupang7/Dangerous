# coding:utf-8
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from appium import webdriver
from time import sleep
import time
import imageCmp
from PIL import Image

class SimpleIOSTests(unittest.TestCase):
    def setUp(self):
        # set up appium
        app = os.path.abspath('app/loanmarket.zip')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            # 真机的配置
            # desired_capabilities={
            #     'app': app,
            #     'platformName': 'iOS',
            #     'platformVersion': '10.3.2',
            #     'deviceName': 'Test的 iPhone',
            #     'udid':'24d5b977a1811d8eaaeece32b0338161544003dd',
            #     'bundleId':'com.lingyue.loanmarketT'
            # })
            # 虚拟机的配置
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '11.1',
                'deviceName': 'iPhone 6s',
            })
    sleep(5)

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def test_leftScroll(self):
        self.driver.tap([(250, 398)])
        location = self.getSize()
        for i in range(2):
            #截图对比
            img = "/Users/panglu/pytest/image/img" + str(int(time.time())) + ".png"
            self.driver.get_screenshot_as_file(img)
            image1 = Image.open("/Users/panglu/pytest/image/引导页" + str(i) + ".png")
            image2 = Image.open(img)
            imageCmp.classfiy_histogram_with_split(image1, image2)
            self.driver.swipe(int(location[0]), int(location[1]/2), int(-location[0]*2),0, 200)
            sleep(3)
        self.driver.find_element_by_accessibility_id("立即使用").click()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
