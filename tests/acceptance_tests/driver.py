from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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
        self._navigate_to_registers()

        create_link = self.browser.find_element(By.LINK_TEXT, "Create new register")
        create_link.click()

        heading = self.browser.find_element(By.TAG_NAME, "h1")
        assert heading.text == "Create new register"

        name_field = self.browser.find_element(By.NAME, "name")
        name_field.send_keys(name)

        self.browser.find_element(By.NAME, "submit").click()

    def confirm_name_required_validation_error(self):
        self._confirm_page_has_errors()

        error_message = self.browser.find_element(By.XPATH, "//a[text()='Enter a name']")
        assert error_message is not None, "Error message not found"

    def confirm_name_already_exists_validation_error(self):
        self._confirm_page_has_errors()

        error_message = self.browser.find_element(By.XPATH, "//a[text()='Name already in use']")
        assert error_message is not None, "Error message not found"

    def confirm_register_created(self, name):
        success_message = self.browser.find_element(By.XPATH, "//*[contains(text(),'Successfully created register')]")
        assert success_message is not None, "Success message not found"

        self._navigate_to_registers()

        existing_register = self.browser.find_element(By.XPATH, f"//*[contains(text(),'{name}')]")
        assert existing_register is not None, "Register not found"

    def confirm_can_view_register(self, name):
        self._navigate_to_registers()
        self._view_register(name)

    def update_existing_register(self, name, new_name):
        self._navigate_to_registers()
        self._view_register(name)

        edit_link = self.browser.find_element(By.LINK_TEXT, "Edit register")
        edit_link.click()

        name_field = self.browser.find_element(By.NAME, "name")
        assert name_field.get_attribute("value") == name

        name_field.clear()
        name_field.send_keys(new_name)

        self.browser.find_element(By.NAME, "submit").click()


    def confirm_register_updated(self, old_name, new_name):
        updated_message = self.browser.find_element(By.XPATH, "//*[contains(text(),'Successfully updated register')]")
        assert updated_message is not None, "Updated message not found"

        self._navigate_to_registers()

        try:
            self.browser.find_element(By.XPATH, f"//*[contains(text(), '{old_name}')]")
            raise AssertionError("Register with old name still exists")
        except NoSuchElementException:
            pass

        new_register = self.browser.find_element(By.XPATH, f"//*[contains(text(), '{new_name}')]")
        assert new_register is not None, "Register with new name not found"

    def _navigate_to_registers(self):
        registers_link = self.browser.find_element(By.LINK_TEXT, "Registers")
        registers_link.click()

        register_heading = self.browser.find_element(By.TAG_NAME, "h1")
        assert register_heading.text == "Registers"

    def _view_register(self, name):
        register_link = self.browser.find_element(By.LINK_TEXT, name)
        register_link.click()

        page_heading = self.browser.find_element(By.TAG_NAME, "h1")
        assert page_heading.text == name

    def _confirm_page_has_errors(self):
        assert self.browser.title.startswith("Error: ")

        error_heading = self.browser.find_element(By.XPATH, "//h2[contains(text(),'There is a problem')]")
        assert error_heading is not None, "Error heading not found"

