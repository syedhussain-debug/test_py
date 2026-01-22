import unittest
import random
import requests
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from faker import Faker


class TestSignupWithOTP(unittest.TestCase):

    def setUp(self):
        options = XCUITestOptions()
        options.platform_name = "iOS"
        options.platform_version = "17.0"
        options.device_name = "iPhone 11"
        options.udid = "00008030-000621290C39802E"
        options.automation_name = "XCUITest"
        options.bundle_id = "com.yumealz.uat"
        options.no_reset = True

        self.driver = webdriver.Remote(
            "http://127.0.0.1:4723",
            options=options
        )

        self.wait = WebDriverWait(self.driver, 30)
        self.fake = Faker("ar_SA")

    # 🔢 Saudi phone generator
    def generate_saudi_number(self):
        prefixes = ['50', '53', '55', '54', '56', '57', '58', '59']
        prefix = random.choice(prefixes)
        rest = ''.join(str(random.randint(0, 9)) for _ in range(7))
        return f"0{prefix}{rest}"

    # 🔐 OTP API (UAT only)
    def get_otp_from_api(self, phone_number):
        response = requests.get(
            f"https://api-uat.yumealz.com/get-otp?phone={phone_number}",
            timeout=10
        )
        response.raise_for_status()
        return response.json()["otp"]

    def test_signup_with_otp(self):
        # 1️⃣ Generate phone number
        phone_number = self.generate_saudi_number()
        print(f"Using phone number: {phone_number}")

        # 2️⃣ Enter phone number
        phone_field = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Phone Number")
            )
        )
        phone_field.send_keys(phone_number)

        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "Send OTP"
        ).click()

        # OPTION A: Static OTP (most UATs)
        #otp_code = "123456"

        # OPTION B: API OTP
        otp_code = self.get_otp_from_api(phone_number)

        # 5️⃣ Enter OTP
        otp_inputs = self.wait.until(
            EC.presence_of_all_elements_located(
                (AppiumBy.CLASS_NAME, "XCUIElementTypeTextField")
            )
        )

        if len(otp_inputs) > 1:
            for i, digit in enumerate(otp_code):
                otp_inputs[i].send_keys(digit)
        else:
            otp_inputs[0].send_keys(otp_code)

        # 6️⃣ Assertion → verify successful login
        home_tab = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "Home\nTab 1 of 5")
            )
        )

        self.assertTrue(
            home_tab.is_displayed(),
            "Signup with OTP failed"
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
