from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Driver:

    def __init__(self, base_url):
        options = Options()
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)
        self.base_url = base_url

    def open_system(self):
        self.browser.get(self.base_url)
        title = self.browser.find_element(By.TAG_NAME, "title")
        assert title.text == "HMLR"

    def close_system(self):
        self.browser.quit()

    def create_new_register(self, name):
        link = self.browser.find_element(By.LINK_TEXT, "Create new register")
        link.click()

        title = self.browser.find_element(By.TAG_NAME, "title")
        assert title.text == "Create new register"

        name_field = self.browser.find_element(By.NAME, "name")
        #TODO asert that field is empty
        name_field.send_keys(name)

        self.browser.find_element(By.NAME, "submit").click()

    def confirm_name_required_validation_error(self):
        title = self.browser.find_element(By.TAG_NAME, "title")
        assert title.text.startswith("Error: ")
        assert title.text.endswith("Create new register")

        error_heading = self.browser.find_element(By.XPATH, "//h2[text()='There is a problem']")
        assert error_heading is not None, "Error heading not found"

        error_message = self.browser.find_element(By.XPATH, "//p[text()='Enter a register name']")
        assert error_message is not None, "Error message not found"


class Dsl:

    def __init__(self, driver: Driver):
        self.driver = driver

    def open_system(self):
        self.driver.open_system()

    def close_system(self):
        self.driver.close_system()

    def create_new_register(self, name="TestRegister"):
        self.driver.create_new_register(name)
        pass

    def confirm_register_exists(self, name="TestRegister"):
        pass

    def confirm_name_required_validation_error(self):
        self.driver.confirm_name_required_validation_error()
        pass

    def confirm_name_already_exists_validation_error(self):
        pass


class RegisterTests(TestCase):

    def __init__(self, *args, **kwargs):
        super(RegisterTests, self).__init__(*args, **kwargs)
        self.dsl = Dsl(Driver(base_url="http://localhost:5000"))

    def setup(self):
        self.dsl.open_system()

    def teardown(self):
        self.dsl.close_system()

    def test_register_name_required(self):
        self.dsl.create_new_register(name="")
        self.dsl.confirm_name_required_validation_error()

    def test_register_name_must_be_unique(self):
        self.dsl.create_new_register(name="TestRegister")
        self.dsl.create_new_register(name="TestRegister")
        self.dsl.confirm_name_already_exists_validation_error()

    def test_can_create_new_register(self):
        self.dsl.create_new_register(name="TestRegister")
        self.dsl.confirm_register_exists(name="TestRegister")

