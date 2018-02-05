import sys
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import tests.iotest.simpleTest

def suite():
    result = unittest.TestSuite()
    result.addTests(unittest.makeSuite(tests.iotest.simpleTest.MainTestCase))
    return result


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
    sys.exit(not result.wasSuccessful())