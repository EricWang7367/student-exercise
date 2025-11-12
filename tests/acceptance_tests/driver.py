from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Driver:

    def __init__(self, base_url):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--ignore-certificate-errors")
        self.browser = webdriver.Chrome(options=options)
        self.base_url = base_url

    def open_system(self):
        self.browser.get(self.base_url)
        assert self.browser.title.endswith("GOV.UK")

    def close_system(self):
        self.browser.quit()

    def create_new_register(self, name):
        register_link = self.browser.find_element(By.LINK_TEXT, "Registers")
        register_link.click()

        register_heading = self.browser.find_element(By.TAG_NAME, "h1")
        assert register_heading.text == "Registers"

        create_link = self.browser.find_element(By.LINK_TEXT, "Create new register")
        create_link.click()

        heading = self.browser.find_element(By.TAG_NAME, "h1")
        assert heading.text == "Create new register"

        name_field = self.browser.find_element(By.NAME, "name")
        # TODO assert that field is empty?
        name_field.send_keys(name)

        self.browser.find_element(By.NAME, "submit").click()

    def confirm_name_required_validation_error(self):
        assert self.browser.title.startswith("Error: ")

        error_heading = self.browser.find_element(By.XPATH, "//h2[text()='There is a problem']")
        assert error_heading is not None, "Error heading not found"

        error_message = self.browser.find_element(By.XPATH, "//p[text()='Enter a register name']")
        assert error_message is not None, "Error message not found"

    def confirm_name_already_exists_validation_error(self):
        assert self.browser.title.startswith("Error: ")

        error_heading = self.browser.find_element(By.XPATH, "//h2[text()='There is a problem']")
        assert error_heading is not None, "Error heading not found"

        error_message = self.browser.find_element(By.XPATH, "//p[text()='Name already in use']")
        assert error_message is not None, "Error message not found"
