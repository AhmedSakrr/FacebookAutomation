import unittest
from appium import webdriver
from time import sleep


class LoginFacebookTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '8.0.0',
                        'deviceName': 'in-blr.headspin.io:8162', 'appPackage': 'com.facebook.katana',
                        'appActivity': 'com.facebook.katana.platform.FacebookAuthenticationActivity',
                        'autoGrantPermissions': 'true'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)
        self.timeout = 30

    def test_login(self):
        print "started"
        login_username = self.driver.find_element_by_id("com.facebook.katana:id/login_username")
        login_username.click()
        login_username.send_keys("automationqa77@gmail.com")

        login_password = self.driver.find_element_by_id("com.facebook.katana:id/login_password")
        login_password.click()
        login_password.send_keys("asdfasdf#12")

        login_button = self.driver.find_element_by_id("com.facebook.katana:id/login_login")
        login_button.click()
        print "login successfully"

    def tearDown(self):
        self.driver.quit()
        print "driver.quit"


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginFacebookTest)
    unittest.TextTestRunner(verbosity=2).run(suite)