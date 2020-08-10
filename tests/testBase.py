import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from tests.testCancelRequest import CancelChangeRequest
from tests.testCloseRequest import CloseChangeRequests
from tests.testCreateRequest import CreateChangeRequest
from utilities.static_data import StaticData


class Test_Base_Case(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get(StaticData.BASE_URL)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


class Test_CancelChangeRequest(Test_Base_Case):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    def test_cancel_change(self):
        self.cancel_change = CancelChangeRequest(self.driver)
        self.cancel_change.test_cancel_change()


class Test_CloseChangeRequests(Test_Base_Case):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    def test_close_request(self):
        self.closeRequest = CloseChangeRequests(self.driver)
        self.closeRequest.test_close_requests()


class Test_CreateChangeRequest(Test_Base_Case):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    def test_create_change(self):
        self.createChange = CreateChangeRequest(self.driver)
        self.createChange.test_create_change()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
