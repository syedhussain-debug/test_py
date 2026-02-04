import unittest

# Import your test classes
from test.loginAsGuest import TestLoginAsGuest
from test.signUp import TestSignupWithOTP
from test.Login import LoginFunction
from test.scheduledSubscriptionFlow import ScheduledSubscriptionFlow


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add test classes using loader
    suite.addTests(loader.loadTestsFromTestCase(TestLoginAsGuest))
    suite.addTests(loader.loadTestsFromTestCase(TestSignupWithOTP))
    suite.addTests(loader.loadTestsFromTestCase(LoginFunction))
    #suite.addTests(loader.loadTestsFromTestCase(ScheduledSubscriptionFlow))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)