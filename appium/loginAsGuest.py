import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.ios import XCUITestOptions
from logout import LogoutFunction

class TestLoginAsGuest(unittest.TestCase):

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
        self.wait = WebDriverWait(self.driver, 30)


    def test_login_as_guest(self):
        """Verify user can continue as guest"""

        # 🔁 Step 1: Check login state
        logout = LogoutFunction()
        logout.driver = self.driver
        logout.wait = self.wait
        logout.logoutFunction()

        # 🔘 Step 2: Click Continue as Guest
        continue_button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Continue as Guest")
            )
        )
        continue_button.click()

        # ✅ Step 3: Verify Home screen
        home_tab = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "Home\nTab 1 of 5")
            )
        )

        self.assertTrue(
            home_tab.is_displayed(),
            "Guest login failed: Home screen not displayed"
        )

    def is_user_logged_in(self):
        """Quick check if Home tab exists"""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.NAME, "Home\nTab 1 of 5")
                )
            )
            return True
        except TimeoutException:
            return False

    def logout(self):
        """Logout user if already logged in"""

        profile_tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.NAME, "Me\nTab 5 of 5")
            )
        )
        profile_tab.click()

        logout_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.NAME, "Logout")
            )
        )
        logout_button.click()

        

    def clear_cache_soft(self):
        """Terminate and relaunch app to clear in-memory cache"""
        self.driver.terminate_app("com.yumealz.uat")
        self.driver.activate_app("com.yumealz.uat")

    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
