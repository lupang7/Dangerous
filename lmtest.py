#coding:utf-8
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
import test
# from PIL import Image
# from imageCmp import Appium_Extend

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = os.path.abspath('app/loanmarket10000.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            #真机的配置
            # desired_capabilities={
            #     'app': app,
            #     'platformName': 'iOS',
            #     'platformVersion': '10.3.2',
            #     'deviceName': 'Test的 iPhone',
            #     'udid':'24d5b977a1811d8eaaeece32b0338161544003dd',
            #     'bundleId':'com.lingyue.loanmarketT'
            # })
            #虚拟机的配置
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '10.2',
                'deviceName': 'iPhone 6s',
            })
        # self.extend = Appium_Extend(self.driver)
    sleep(5)

    def test_get_screen_by_element(self):
        self.driver.get_screenshot_as_file("/Users/panglu/pytest/image/img1.jpg")
        # element = self.driver.find_element_by_id("welcome1")
        #
        # load = self.extend.load_image("/Users/panglu/pytest/image/引导页1.jpg")
        # # 要求百分百相似
        # result = self.extend.get_screenshot_by_element(element).same_as(load, 0)
        # self.assertTrue(result)





    # def getSize(self):
    #     x = self.driver.get_window_size()['width']
    #     y = self.driver.get_window_size()['height']
    #     return (x, y)
    #
    # def test_leftScroll(self):
    #     location = self.getSize()
    #     print("location is" ,location)
    #     self.driver.swipe(start_x=int(location[0]), start_y=int(location[1]), end_x=int(-location[0]), end_y=int(location[1]), duration=800)
    #     sleep(1)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)