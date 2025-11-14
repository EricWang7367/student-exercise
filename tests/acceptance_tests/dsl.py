import time
from typing import Dict

from tests.acceptance_tests.driver import Driver


class Dsl:

    DEFAULT_REGISTER_NAME = "Register of Things"

    def __init__(self, driver: Driver):
        self.driver = driver
        self.aliases: Dict[str, str] = {}

    def setup(self):
        self.driver.setup()

    def tear_down(self):
        self.driver.tear_down()

    def ensure_existing_register(self, name=DEFAULT_REGISTER_NAME):
        self.create_new_register(name)
        self.confirm_register_created(name)

    def create_new_register(self, name=DEFAULT_REGISTER_NAME):
        self.driver.create_new_register(self._encode_alias(name))

    def confirm_register_created(self, name=DEFAULT_REGISTER_NAME):
        self.driver.confirm_register_created(self._decode_alias(name))

    def confirm_name_required_validation_error(self):
        self.driver.confirm_name_required_validation_error()

    def confirm_name_already_exists_validation_error(self):
        self.driver.confirm_name_already_exists_validation_error()

    def confirm_can_view_register(self, name=DEFAULT_REGISTER_NAME):
        self.driver.confirm_can_view_register(self._encode_alias(name))

    def update_existing_register(self, name=DEFAULT_REGISTER_NAME):
        self.driver.update_existing_register(self._encode_alias(name), self._encode_alias("Updated" + name))

    def confirm_register_updated(self, name=DEFAULT_REGISTER_NAME):
        self.driver.confirm_register_updated(self._decode_alias("Updated " + name))

    def _encode_alias(self, name):
        if name == "":
            return ""
        if name not in self.aliases:
            self.aliases[name] = name + str(round(time.time() * 1000))
        return self.aliases[name]

    def _decode_alias(self, name):
        if name in self.aliases:
            return self.aliases[name]
        else:
            return ""
