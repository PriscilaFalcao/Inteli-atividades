import unittest
import requests
from ..data_pipeline.api import get_dog_facts

class TestAPI(unittest.TestCase):
    def test_get_dog_facts(self):
        response = get_dog_facts(5)
        self.assertIsInstance(response, list)

        with self.assertRaises(requests.exceptions.RequestException):
            get_dog_facts(0)

if __name__ == '__main__':
    unittest.main()