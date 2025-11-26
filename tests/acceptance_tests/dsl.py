import time
from typing import Dict

from tests.acceptance_tests.driver import Driver


class Dsl:

    DEFAULT_REGISTER_NAME = "Register of Things"
    DEFAULT_ENTRY_NAME = "An entry"

    def __init__(self, driver: Driver):
        self.driver = driver
        self.aliases: Dict[str, str] = {}

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
        self.driver.confirm_can_view_register(self._decode_alias(name))

    def update_existing_register(self, current_name=DEFAULT_REGISTER_NAME, new_name=""):
        current_name_alias = self._encode_alias(current_name)
        new_name_alias = self._encode_alias(new_name)
        self.driver.update_existing_register(current_name_alias, new_name_alias)

    def confirm_register_updated(self, old_name=DEFAULT_REGISTER_NAME, new_name=""):
        old_name_alias = self._decode_alias(old_name)
        new_name_alias = self._decode_alias(new_name)
        self.driver.confirm_register_updated(old_name_alias, new_name_alias)

    def delete_existing_register(self, name=DEFAULT_REGISTER_NAME):
        alias = self._encode_alias(name)
        self.driver.delete_existing_register(alias)

    def confirm_deletion_requires_confirmation(self, name=DEFAULT_REGISTER_NAME):
        alias = self._decode_alias(name)
        self.driver.confirm_deletion_requires_confirmation(alias)

    def cancel_register_deletion(self, name=DEFAULT_REGISTER_NAME):
        alias = self._decode_alias(name)
        self.driver.cancel_register_deletion(alias)

    def confirm_register_deletion(self, name=DEFAULT_REGISTER_NAME):
        alias = self._decode_alias(name)
        self.driver.confirm_register_deletion(alias)

    def confirm_register_deleted(self, name=DEFAULT_REGISTER_NAME):
        alias = self._decode_alias(name)
        self.driver.confirm_register_deleted(alias)

    def confirm_register_exists(self, name=DEFAULT_REGISTER_NAME):
        alias = self._decode_alias(name)
        self.driver.confirm_register_exists(alias)

    def ensure_existing_entry(self, register=DEFAULT_REGISTER_NAME, entry_name=DEFAULT_ENTRY_NAME):
        self.add_entry_to_register(register=register, entry_name=entry_name)
        self.confirm_entry_added(register=register, entry_name=entry_name)

    def add_entry_to_register(self, register=DEFAULT_REGISTER_NAME, entry_name=DEFAULT_ENTRY_NAME):
        self.driver.add_entry_to_register(
            register=self._encode_alias(register), entry_name=self._encode_alias(entry_name)
        )

    def confirm_entry_added(self, register=DEFAULT_REGISTER_NAME, entry_name=DEFAULT_ENTRY_NAME):
        self.driver.confirm_entry_added(
            register=self._decode_alias(register), entry_name=self._decode_alias(entry_name)
        )

    def confirm_can_view_entry(self, register=DEFAULT_REGISTER_NAME, entry_name=DEFAULT_ENTRY_NAME):
        self.driver.confirm_can_view_entry(
            register=self._encode_alias(register), entry_name=self._encode_alias(entry_name)
        )

    # mine

    # update
    def update_existing_entry(self, register=DEFAULT_REGISTER_NAME, current_name=DEFAULT_ENTRY_NAME, new_name=""):
        reg_alias = self._encode_alias(register)
        current_alias = self._encode_alias(current_name)
        new_alias = self._encode_alias(new_name)
        self.driver.update_existing_entry(register=reg_alias, entry_name=current_alias, new_name=new_alias)

    def confirm_entry_updated(self, register=DEFAULT_REGISTER_NAME, old_name=DEFAULT_ENTRY_NAME, new_name=""):
        register_alias = self._decode_alias(register)
        old_alias = self._decode_alias(old_name)
        new_alias = self._decode_alias(new_name)
        self.driver.confirm_entry_updated(register=register_alias, old_name=old_alias, new_name=new_alias)

    # delete
    def delete_existing_entry(self,register=DEFAULT_REGISTER_NAME, name=DEFAULT_ENTRY_NAME):
        register_alias=self._encode_alias(register)
        alias = self._encode_alias(name)
        self.driver.delete_existing_entry(register_alias,alias)

    def confirm_deletion_requires_confirmation_entry(self, name=DEFAULT_ENTRY_NAME):
        alias = self._decode_alias(name)
        self.driver.confirm_deletion_requires_confirmation_entry(alias)

    def confirm_entry_deletion(self, name=DEFAULT_ENTRY_NAME):
        alias = self._decode_alias(name)
        self.driver.confirm_entry_deletion(alias)

    def confirm_entry_deleted(self,register=DEFAULT_REGISTER_NAME, entry_name=DEFAULT_ENTRY_NAME):
        entry_name_alias = self._decode_alias(entry_name)
        register_alias = self._decode_alias(register)
        self.driver.confirm_entry_deleted(register_alias, entry_name_alias)

    def cancel_entry_deletion(self, name=DEFAULT_ENTRY_NAME):
        alias = self._decode_alias(name)
        self.driver.cancel_entry_deletion(alias)

    def confirm_entry_exists(self, reg=DEFAULT_REGISTER_NAME, name=DEFAULT_ENTRY_NAME):
        reg_alias = self._decode_alias(reg)
        alias = self._decode_alias(name)
        self.driver.confirm_entry_exists(reg_alias, alias)
