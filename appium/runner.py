import unittest

# Import your test classes
from loginAsGuest import TestLoginAsGuest
from signUp import TestSignupWithOTP
from Login import LoginFunction


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add test classes using loader
    suite.addTests(loader.loadTestsFromTestCase(TestLoginAsGuest))
    suite.addTests(loader.loadTestsFromTestCase(TestSignupWithOTP))
    suite.addTests(loader.loadTestsFromTestCase(LoginFunction))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)