from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


RETRY_COUNT = 5


class NewTabException(Exception):
    pass


class BasePage:

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

    def select_to_hidden(self, start_loc, finish_loc):
        main = self.driver.find_element(*start_loc)
        hide = self.driver.find_element(*finish_loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(main)
        actions.click(hide)
        actions.perform()
    
    def _switch_to_second_tab(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
        except IndexError:
            raise NewTabException('Новая вкладка не найдена')
