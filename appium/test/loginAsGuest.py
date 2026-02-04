# loginAsGuest.py
import unittest
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from functions.setupFile import SetupFile
from functions.logout import LogoutFunction
from test.initializeByAlert import InitializeByAlert
from test.profileStatus import ProfileStatus


class TestLoginAsGuest(SetupFile):

    def test_login_as_guest(self):
        """Verify user can continue as guest"""
        print("🚀 Starting guest login test...")
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

        locationAndAlert = InitializeByAlert()
        locationAndAlert.intilize_setup(self.driver, self.wait)        
        profileStatus = ProfileStatus()
        profileStatus.assertionCondition(self.driver, self.wait, self)
        

        
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