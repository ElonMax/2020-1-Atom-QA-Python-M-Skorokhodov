from selenium.webdriver.common.by import By


class StartPageLocators:
    USERNAME = (By.XPATH, "//input[@id='username'][@required]")
    PASSWORD = (By.XPATH, "//input[@id='password'][@required]")
    LOGIN_BUTTON = (By.XPATH, "//input[@name='submit']")
    ERROR_MESSAGE = (By.XPATH, "//div[@id='flash']")
    REGISTER_BUTTON = (By.XPATH, "//a[@href='/reg']")
    BLOCK_MESSAGE = (By.XPATH, "//div[text()='Ваша учетная запись заблокирована']")


class RegistrationPageLocators:
    REGISTRATION_USERNAME = (By.XPATH, "//input[@id='username'][@required]")
    REGISTRATION_PASSWORD = (By.XPATH, "//input[@id='password'][@required]")
    TERM_BUTTON = (By.XPATH, "//input[@id='term'][@required]")
    USERNAME_ERROR = (By.XPATH, "//div[text()='Incorrect username length']")
    REGISTRATION_EMAIL = (By.XPATH, "//input[@name='email']")
    REGISTRATION_CONFIRM_PASSWORD = (By.XPATH, "//input[@name='confirm']")
    DO_REGISTRATION_BUTTON = (By.XPATH, "//input[@name='submit']")
    EMAIL_ERROR_INVALID = (By.XPATH, "//div[text()='Invalid email address']")
    EMAIL_ERROR_LENGTH = (By.XPATH, "//div[text()='Incorrect email length']")
    PASSWORD_ERROR = (By.XPATH, "//div[text()='Passwords must match']")
    GO_BACK_LOGIN_BUTTON = (By.XPATH, "//a[@href='/login']")
    REGISTRATION_EMAIL_VALID = (By.XPATH, "//input[@name='email'][@required]")
    REGISTRATION_CONFIRM_PASSWORD_VALID = (By.XPATH, "//input[@name='confirm'][@required]")
    SOMETHING_MESSAGE = (By.XPATH, "//div[text()='Something wrong']")


class CabinetPageLocators:
    LOGGED_AS = (By.XPATH, "//li[contains(text(), 'Logged as')]")
    LOGOUT_BUTTON = GO_BACK_LOGIN_BUTTON = (By.XPATH, "//a[@href='/logout']")
    CABINET_PAGE_BUTTON = (By.XPATH, "//a[contains(@class, 'uk-navbar-brand')]")
    HOME_BUTTON = (By.XPATH, "//a[text()='HOME']")
    PYTHON_BUTTON = (By.XPATH, "//a[text()='Python']")
    PYTHON_HISTORY_BUTTON = (By.XPATH, "//a[text()='Python history']")
    ABOUT_FLASK_BUTTON = (By.XPATH, "//a[text()='About Flask']")
    LINUX_BUTTON = (By.XPATH, "//a[text()='Linux']")
    DOWNLOAD_CENTOS_BUTTON = (By.XPATH, "//a[text()='Download Centos7']")
    NETWORK_BUTTON = (By.XPATH, "//a[text()='Network']")
    NEWS_BUTTON = (By.XPATH, "//a[text()='News']")
    DOWNLOAD_NET_BUTTON = (By.XPATH, "//a[text()='Download']")
    EXAMPLES_BUTTON = (By.XPATH, "//a[text()='Examples']")
    WHAT_IS_BUTTON = (By.XPATH, "//img[@src='/static/images/laptop.png']")
    FUTURE_BUTTON = (By.XPATH, "//img[@src='/static/images/loupe.png']")
    SMTP_BUTTON = (By.XPATH, "//img[@src='/static/images/analytics.png']")
    FACTS = (By.XPATH, "//div[@class='uk-text-center uk-text-large']")
    NONE_VK_ID = (By.XPATH, "//div[@id='login-name']//li[2][text()='']")
