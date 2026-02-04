# setupFile.py
import unittest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.support.ui import WebDriverWait
from functions.config_reader import ConfigReader

config = ConfigReader.read_config()

class SetupFile(unittest.TestCase):

    def setUp(self):

        options = XCUITestOptions()
        options.platform_name = config["platform_name"]
        options.platform_version = config["platform_version"]
        options.device_name = config["device_name"]
        options.udid = config["udid"]
        options.automation_name = config["automation_name"]
        options.bundle_id = config["bundle_id"]
        options.no_reset = config["no_reset"] == "True"
        options.show_xcode_log = config["show_xcode_log"] == "True"
        options.wda_startup_retries = int(config["wda_startup_retries"])
        options.auto_accept_alerts = True
        self.driver = webdriver.Remote(
            command_executor=config["appium_server"],
            options=options
        )


        self.wait = WebDriverWait(
            self.driver,
            int(config.get("explicit_wait"))
        )

    def tearDown(self):
        if self.driver:
            self.driver.quit()