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
from apiAll import ApiRes
import json
import logging

ApiRes =ApiRes()


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
                'platformVersion': '11.2',
                'deviceName': 'iPhone 6s',
                'noReset': 'true'

            })
    sleep(5)

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    #测试欢迎页
    def test_a_welcome(self):
        self.driver.tap([(250, 398)])
        location = self.getSize()
        for i in range(2):
            #截图对比
            img = "/Users/panglu/mist/Dangerous/images/img" + str(int(time.time())) + ".png"
            self.driver.get_screenshot_as_file(img)
            image1 = Image.open("/Users/panglu/mist/Dangerous/images/引导页" + str(i) + ".png")
            image2 = Image.open(img)
            Similarity = imageCmp.classfiy_histogram_with_split(image1, image2)
            self.driver.swipe(int(location[0]), int(location[1]/2), int(-location[0]*2),0, 200)
            sleep(3)
        self.driver.find_element_by_accessibility_id("立即使用").click()

    # 登录失败获取不到元素，放弃
    # def test_b_login(self):
    #     self.driver.find_element_by_accessibility_id("userCenter").click()
    #     self.driver.find_element_
    #     self.driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="六六钱庄"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[1]/XCUIElementTypeTextField').click()
    #     list = ('130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '144', '147',
    #             '150', '151', '152', '153', '155', '156', '157', '158', '159', '176', '177', '178',
    #             '180', '181', '182', '1823', '184', '185', '186', '187', '188', '189',)
    #     telNum = random.choice(list) + "".join(random.choice('0123456789') for i in range(8))
    #     for j in telNum :
    #         self.driver.find_element_by_accessibility_id("j").click()
    #
    #     self.driver.find_element_by_accessibility_id('获取验证码').click()
    #     sleep(3)
    #     self.driver.find_element_by_xpath('').send_keys('141212')
    #     self.driver.find_element_by_ios_uiautomation()
    #     sleep(3)
    #     self.driver.find_element_by_accessibility_id('登录').click()
    #     self.driver.find_element_by_accessibility_id('userCenter').click()
    #     sleep(3)
    #     self.driver.find_element_by_accessibility_id('ic fh').click()


    #测试首页的各个模块
    def test_c_homePage(self):
        resbanner = json.loads(ApiRes.getBanner())
        if len(resbanner['body']) >= 1:
            pass
        else:
            print("没有设置轮播图")
        rescard = json.loads(ApiRes.getCard())
        print(len(rescard['body']))
        if len(rescard['body']) >= 2:
            self.driver.find_element_by_xpath ("//XCUIElementTypeApplication[@name=\"六六钱庄\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[1]").click()
            self.driver.find_element_by_accessibility_id("返回").click()
        else:
            print("没有配置卡片")
        resscroll = json.loads(ApiRes.getScroll())
        if len(resscroll['body']) >=1:
            pass
        else:
            print("没有设置滚动条")

        self.driver.find_element_by_accessibility_id("换一批").click()

    #测试webview


    def test_d_allProduct(self):
        self.driver.find_element_by_accessibility_id("全部贷款").click()


    def test_e_Activity(self):
        self.driver.find_element_by_accessibility_id("更多活动").click()

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
