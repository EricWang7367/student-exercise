import time
from typing import Dict

from tests.acceptance_tests.driver import Driver


class Dsl:

    def __init__(self, driver: Driver):
        self.driver = driver
        self.aliases: Dict[str, str] = {}

    def setup(self):
        self.driver.setup()

    def tear_down(self):
        self.driver.tear_down()

    def create_new_register(self, name="Register of Things"):
        self.driver.create_new_register(self._encode_alias(name))

    def confirm_register_created(self, name="Register of Things"):
        self.driver.confirm_register_created(self._decode_alias(name))

    def confirm_name_required_validation_error(self):
        self.driver.confirm_name_required_validation_error()

    def confirm_name_already_exists_validation_error(self):
        self.driver.confirm_name_already_exists_validation_error()

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
