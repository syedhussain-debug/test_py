import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InitializeByAlert:

    # Ensure self, driver, and wait are all defined here
    def intilize_setup(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
        time.sleep(2)
        try:
            # Handle the system permission alert
            self.driver.switch_to.alert.accept()
            print("Alert accepted.")
        except Exception:
            print("No system alert was present")
    
        try:
            # Handle the app-specific location selection
            location = self.wait.until(EC.element_to_be_clickable((By.NAME, "Jeddah")))
            location.click()

            location2 = self.wait.until(EC.element_to_be_clickable((By.NAME, "Jeddah")))
            location2.click()
            
            location_submit = self.wait.until(EC.element_to_be_clickable((By.NAME, "Next")))
            location_submit.click()
            print("Location 'Jeddah' selected and submitted.")
        except Exception:
            print("Location selection screen not displayed")