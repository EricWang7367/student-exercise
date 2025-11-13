from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Driver:

    def __init__(self, base_url):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--ignore-certificate-errors")
        self.browser = webdriver.Chrome(options=options)
        self.base_url = base_url

    def setup(self):
        self.browser.get(self.base_url)
        assert self.browser.title.endswith("GOV.UK")

    def tear_down(self):
        self.browser.quit()

    def create_new_register(self, name):
        registers_link = self.browser.find_element(By.LINK_TEXT, "Registers")

        self._follow_link(registers_link)

        register_heading = self.browser.find_element(By.TAG_NAME, "h1")
        assert register_heading.text == "Registers"

        create_link = self.browser.find_element(By.LINK_TEXT, "Create new register")
        self._follow_link(create_link)

        heading = self.browser.find_element(By.TAG_NAME, "h1")
        assert heading.text == "Create new register"

        name_field = self.browser.find_element(By.NAME, "name")
        name_field.send_keys(name)

        self.browser.find_element(By.NAME, "submit").click()

    def confirm_name_required_validation_error(self):
        self._confirm_errors_displayed()

        error_message = self.browser.find_element(By.XPATH, "//a[text()='Enter a name']")
        assert error_message is not None, "Error message not found"

    def confirm_name_already_exists_validation_error(self):
        self._confirm_errors_displayed()

        error_message = self.browser.find_element(By.XPATH, "//a[text()='Name already in use']")
        assert error_message is not None, "Error message not found"

    def _confirm_errors_displayed(self):
        assert self.browser.title.startswith("Error: ")

        error_heading = self.browser.find_element(By.XPATH, "//h2[contains(text(),'There is a problem')]")
        assert error_heading is not None, "Error heading not found"

    def confirm_register_created(self, name):
        success_message = self.browser.find_element(By.XPATH, "//*[contains(text(),'Successfully created register')]")
        assert success_message is not None, "Success message not found"

        registers_link = self.browser.find_element(By.LINK_TEXT, "Registers")
        self._follow_link(registers_link)

        existing_register = self.browser.find_element(By.XPATH, f"//*[contains(text(),'{name}')]")
        assert existing_register is not None, "Register not found"

    def _follow_link(self, link):
        link.click()
        WebDriverWait(self.browser, 5).until(EC.staleness_of(link))
