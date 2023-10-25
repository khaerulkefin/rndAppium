import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    platformVersion='13',
    automationName='uiautomator2',
    deviceName='POCO X5 5G',
    appPackage='com.google.android.youtube',
    appActivity='com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity',
    noReset=True,
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url,options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_subs(self) -> None:
        channel = "berijalan"
        matchChannel = "berijalan official"

        sleep(3)
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.google.android.youtube:id/search_edit_text")
        el2.send_keys(channel)

        el2 = self.driver.press_keycode(66)

        channelName = self.driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"Subscribe to Berijalan Official.\"]").get_attribute("content-desc").lower()

        if matchChannel in channelName:
            print("Channel name: " + channelName)
            el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Subscribe to Berijalan Official.")
            el3.click()
            el4 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"Options\"]/android.widget.ImageView[2]")
            el4.click()
            el5 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"Unsubscribe from Berijalan Official.\"]")
            el5.click()

if __name__ == '__main__':
    unittest.main()