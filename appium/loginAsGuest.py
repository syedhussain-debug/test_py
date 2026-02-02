# loginAsGuest.py
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from setupFile import SetupFile
from logout import LogoutFunction


class TestLoginAsGuest(SetupFile):

    def test_login_as_guest(self):
        """Verify user can continue as guest"""

        logout = LogoutFunction()
        logout.driver = self.driver
        logout.wait = self.wait
        logout.logoutFunction()

        continue_button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Continue as Guest")
            )
        )
        continue_button.click()

        home_tab = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "Home\nTab 1 of 5")
            )
        )

        self.assertTrue(home_tab.is_displayed(), "Guest login failed")

    def is_user_logged_in(self):
        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (By.NAME, "Home\nTab 1 of 5")
                )
            )
            return True
        except TimeoutException:
            return False

    def clear_cache_soft(self):
        self.driver.terminate_app("com.yumealz.uat")
        self.driver.activate_app("com.yumealz.uat")

if __name__ == "__main__":
    unittest.main()