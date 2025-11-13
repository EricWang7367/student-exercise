from unittest import TestCase

from tests.acceptance_tests.driver import Driver
from tests.acceptance_tests.dsl import Dsl


class RegisterTests(TestCase):

    def __init__(self, *args, **kwargs):
        super(RegisterTests, self).__init__(*args, **kwargs)
        self.dsl = Dsl(Driver(base_url="https://localhost/"))

    def setUp(self):
        self.dsl.open_system()

    def tearDown(self):
        self.dsl.close_system()

    def test_register_name_required(self):
        self.dsl.create_new_register(name="")
        self.dsl.confirm_name_required_validation_error()

    def test_register_name_must_be_unique(self):
        self.dsl.create_new_register(name="Existing register")
        self.dsl.create_new_register(name="Existing register")
        self.dsl.confirm_name_already_exists_validation_error()

    def test_can_create_new_register(self):
        self.dsl.create_new_register(name="A new register")
        self.dsl.confirm_register_created(name="A new register")
