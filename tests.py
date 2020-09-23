# Basic template for Python unit tests
# NOTE: Use Python 3

# Import the unittest module to use the Python unit test framework
import unittest

# Import the modules and/or classes that are being tested
from hello import Hello

# A test case consists of individual steps, represented as methods.
# These methods MUST start with "test". Some special methods exist
# to initialise and finalise the test case run.

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.hello = Hello()

    def testHelloString(self):
        """Check that the default hello world string is present."""
        assert(str(self.hello) == "Hello, World!")

    def testChangeHelloString(self):
        """Check that the hello world string changes when the name is changed."""
        self.hello.name = "Planet"
        assert(str(self.hello) == "Hello, Planet!")

    def testEmptyName(self):
        """Check that the greeting is just "Hello!" if the name is an empty string."""
        if not self.hello.name:
            assert(str(self.hello) == "Hello!")

    def testAdd(self):
        self.hello.add("Zozo")
        assert("Zozo" in self.hello.name_list())

    def testPickRandom(self):
        self.hello.pick_random()
        assert(self.hello.name in self.hello.name_list())

# This is what gets run when Python is started on this file.
if __name__ == '__main__':
    # The unittest framework will discover all test cases in the file
    # and run the test methods in them.
    unittest.main()
