import unittest
from main import working

class TestWorking(unittest.TestCase):
    def test_working(self):
        self.assertEqual(working(), "It's working!")

if __name__ == '__main__':  
    unittest.main()