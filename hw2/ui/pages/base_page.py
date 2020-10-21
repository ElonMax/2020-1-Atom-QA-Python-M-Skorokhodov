from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

RETRY_COUNT = 3


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout):
        return WebDriverWait(self.driver, timeout=timeout)

    def click(self, locator, timeout):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator, timeout)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def entering(self, locator, message, timeout):
        field = self.wait(timeout).until(EC.presence_of_element_located(locator))
        try:
            field.clear()
        except ElementNotInteractableException:
            pass
        field.send_keys(message)

    def find(self, locator, timeout):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))
