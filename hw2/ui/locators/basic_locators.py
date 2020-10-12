from selenium.webdriver.common.by import By


class MainPageLocators:
    GOTO_LOGIN_BUTTON = (By.CLASS_NAME, "responseHead-module-button-1BMAy4")
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.CLASS_NAME, "authForm-module-button-2G6lZu")


class CabinetPageLocators:
    TITLE_EMAIL = (By.CLASS_NAME, "right-module-userNameWrap-34ibLS")
    NEW_COMPANY_BUTTON = (By.CLASS_NAME, "button-module-textWrapper-3LNyYP")
    CREATE_CAMPAIGN_STATUS = (By.CLASS_NAME, "notify-module-wrapper-3vtOr_")
    NEW_SEGMENT_BUTTON = (By.XPATH, "//a[contains(@class, 'center-module-segments-3y1hDo')]")


class CampaignPageLocators:
    TRAFFIC = (By.XPATH, "//div[@cid='view567']")
    SITE_FIELD = (By.XPATH, "//input[@data-gtm-id='ad_url_text']")
    BANNER = (By.XPATH, "//div[@id='patterns_4']")
    UPLOAD_FILE = (By.XPATH, "//input[@data-test='image_240x400']")
    SAVE_IMAGE = (By.XPATH, "//input[@data-translated-lit='Save image']")
    LOAD_STATUS = (By.XPATH, "//div[contains(@class, 'patternTabs-module-green-2gBr1Y')]")
    CREATE_CAMPAIGN = (By.XPATH, "//button[@cid='view515']/div")


class SegmentPageLocators:
    CREATE_SEGMENT = (By.XPATH, "//a[@href='/segments/segments_list/new/']")
    CHOOSE_FLAG = (By.XPATH, "//input[contains(@class, 'js-main-source-checkbox')]")
    ADD_SEGMENT_BUTTON = (By.XPATH, "//div[contains(@class, 'js-add-button')]/button/div")
    ANOTHER_ADD_SEGMENT_BUTTON = (By.XPATH, "//button[contains(@class, 'button_submit')]/div")
    ADDING_SEGMENT_ITEM = (By.XPATH, "//div[@class='adding-segments-item']")
    CONFIRM_SEGMENT_BUTTON = (By.XPATH, "//div[contains(@class, 'js-create-segment-button-wrap')]/button/div")
    DELETE_SEGMENT = (By.XPATH, "//span[@class='icon-cross cells-module-removeCell-2tweYp']")
    CONFIRM_DELETE = (By.XPATH, "//button[@class='button button_confirm-remove button_general']/div")
    CREATE_SEGMENT_FORM = (By.XPATH, "//div[@class='input input_create-segment-form']/div/input")
