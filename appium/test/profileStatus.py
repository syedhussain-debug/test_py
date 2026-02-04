
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProfileStatus:    
    def assertionCondition(self, driver, wait, test_case):        
        self.driver = driver
        self.wait = wait
        time.sleep(2)

        home_tab = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "Me\nTab 5 of 5")
            )
        )
        
        test_case.assertTrue(home_tab.is_displayed(), "Guest login failed")