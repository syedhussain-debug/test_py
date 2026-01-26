from appium.options.ios import XCUITestOptions
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class SetupFile:
    def setUp(self):
        options = XCUITestOptions()
        options.platform_name = "iOS"
        options.platform_version = "17.0"
        options.device_name = "iPhone 11"
        options.udid = "00008030-000621290C39802E"
        options.automation_name = "XCUITest"
        options.bundle_id = "com.yumealz.uat"
        options.no_reset = True
        options.show_xcode_log = True
        options.wda_startup_retries = 1

        self.driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            options=options
        )

        self.wait = WebDriverWait(self.driver, 20)
        return self.driver, self.wait