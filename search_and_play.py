import unittest
from time import sleep
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

    def test_search(self) -> None:
        title = "Acc Tetap Jaya"
        matchTitle = "acc"

        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.google.android.youtube:id/search_edit_text")
        el2.send_keys(title)
        
        self.driver.press_keycode(66)

        el3 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"ACC Tetap Jaya (Virtual Version) - 2 minutes, 17 seconds - Go to channel - ACC Career - 10K views - 1 year ago - play video\"]/android.view.ViewGroup[1]")
        el4 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"ACC Tetap Jaya (Virtual Version) - 2 minutes, 17 seconds - Go to channel - ACC Career - 10K views - 1 year ago - play video\"]").get_attribute("content-desc")
        titleText = el4.split('-')[0].lower()

        if matchTitle in titleText:
            print("judul video: " + titleText)
            el3.click()


if __name__ == '__main__':
    unittest.main()