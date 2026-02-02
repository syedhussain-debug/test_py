# setupFile.py
import unittest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.support.ui import WebDriverWait


class SetupFile(unittest.TestCase):

    def setUp(self):
        options = XCUITestOptions()
        options.platform_name = "iOS"
        options.platform_version = "17.0"
        options.device_name = "iPhone 17"
        options.udid = "BF288222-4428-4E67-8878-2DAC2732FE3A"
        options.automation_name = "XCUITest"
        options.bundle_id = "com.yumealz.uat"
        options.no_reset = True
        options.show_xcode_log = True
        options.wda_startup_retries = 1

        self.driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            options=options
        )
        self.wait = WebDriverWait(self.driver, 30)

    def tearDown(self):
        if self.driver:
            self.driver.quit()
