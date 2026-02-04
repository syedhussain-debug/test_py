from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class LogoutFunction:
    def logoutFunction(self):
        if self.skip_welcome_tour():
            print("Skipped welcome tour if it was present.")
        else:        
            print("No welcome tour to skip.")
            
        if self.is_user_logged_in():

            print("User already logged in → logging out")
            self.logout()
        else:
            print("User not logged in")

    def skip_welcome_tour(self):
        """Skip welcome tour if it appears"""
        try:
            skip_button = self.wait.until(
                EC.element_to_be_clickable((By.NAME, "Skip"))
            )
            skip_button.click()
            print("Welcome tour skipped.")
        except Exception:
            print("Welcome tour not displayed")
       
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

        try:
            self.driver.execute_script("mobile: scroll", {"direction": "down"})
            logout_button = self.wait.until(
                EC.element_to_be_clickable((By.NAME, "Logout"))
                )
            logout_button.click()

        except Exception as e:
            e = print("🔍 Logout not visible, scrolling...")
            self.wait.until(
                EC.element_to_be_clickable((By.NAME, "Logout"))
                ).click()

    