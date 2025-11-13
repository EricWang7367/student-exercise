from tests.acceptance_tests.driver import Driver


class Dsl:

    def __init__(self, driver: Driver):
        self.driver = driver

    def open_system(self):
        self.driver.open_system()

    def close_system(self):
        self.driver.close_system()

    def create_new_register(self, name="Register of Things"):
        self.driver.create_new_register(name)

    def confirm_register_created(self, name="Register of Things"):
        self.driver.confirm_register_created(name)

    def confirm_name_required_validation_error(self):
        self.driver.confirm_name_required_validation_error()

    def confirm_name_already_exists_validation_error(self):
        self.driver.confirm_name_already_exists_validation_error()
