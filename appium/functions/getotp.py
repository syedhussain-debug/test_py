import time
import jwt
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class OTPService():

    LOGIN_URL = "https://dev-portal.techrar.com/login"
    OTP_API_URL = "https://dev-api.techrar.com/api/v1/dashboard/admin/otps/?page=1&page_size=100"

    MOBILE_UI = "534444900"
    OTP_UI = "0000"

    def __init__(self):
        self.driver = self._setup_driver()

    # ---------- PUBLIC METHOD ----------
    def get_otp_code(self, mobile_number):
        self._login()
        token = self._get_token()
        otp = self._fetch_otp(token, mobile_number)
        self.driver.quit()
        return otp

    # ---------- INTERNAL METHODS ----------
    def _setup_driver(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    def _login(self):
        self.driver.get(self.LOGIN_URL)
        wait = WebDriverWait(self.driver, 30)

        mobile = wait.until(EC.visibility_of_element_located((By.ID, "mat-input-0")))
        mobile.send_keys(self.MOBILE_UI)

        login_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//form/button")
            )
        )
        login_btn.click()

        otp_input = wait.until(EC.visibility_of_element_located((By.ID, "mat-input-1")))
        otp_input.send_keys(self.OTP_UI)

        time.sleep(3)

    def _get_token(self):
        token = self.driver.execute_script(
            "return window.localStorage.getItem('accessToken');"
        )
        if not token:
            raise Exception("❌ Token not found")
        return token

    def _fetch_otp(self, token, mobile_number):
        decoded = jwt.decode(token, options={"verify_signature": False})
        org_id = decoded.get("org_id", "54")

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "org-id": str(org_id),
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(self.OTP_API_URL, headers=headers)
        response.raise_for_status()

        final_mobile = "0" + mobile_number

        for item in response.json()["results"]:
            if item["mobile_number"] == final_mobile:
                return item["otp"]

        raise Exception(f"❌ OTP not found for {mobile_number}")
