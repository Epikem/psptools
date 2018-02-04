import sys
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import tests.iotest
# import tests.minifiertest

def suite():
    result = unittest.TestSuite()
    result.addTests(tests.iotest.suite())
    # result.addTests(tests.minifiertest.suite())

    return result


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
    sys.exit(not result.wasSuccessful())