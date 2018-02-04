# -*- coding:utf-8 -*-
import unittest
from unittest import SkipTest, TestCase
import functools
import types
import os
import psptools
import sys
import fileinput
import io

def _id(obj):
    return obj


def skip(reason):
    """Unconditionally skip a test."""
    def decorator(test_item):
        if not isinstance(test_item, (type, types.ClassType)):
            @functools.wraps(test_item)
            def skip_wrapper(*args, **kwargs):
                raise SkipTest(reason)
            test_item = skip_wrapper
        elif issubclass(test_item, TestCase):
            @classmethod
            @functools.wraps(test_item.setUpClass)
            def skip_wrapper(*args, **kwargs):
                raise SkipTest(reason)
            test_item.setUpClass = skip_wrapper
        test_item.__unittest_skip__ = True
        test_item.__unittest_skip_why__ = reason
        return test_item
    return decorator


def skipIf(condition, reason):
    """Skip a test if the condition is true."""
    if condition:
        return skip(reason)
    return _id


readModule = psptools.main.edx_in
readModule.rl = readModule.next_line
readModule.rt = readModule.next_token
readModule.rnt = readModule.nextNToken
readModule.ri = readModule.next_int
readModule.rf = readModule.next_float
readModule.rs = readModule.next_str
writeModule = psptools.main.edx_out

class SimpleTest(unittest.TestCase):

    def setUp(self):
        super(SimpleTest, self).setUp()

    def tearDown(self):
        super(SimpleTest, self).tearDown()

    def test_simple_case(self):
        pass




def TemplateTest1(testcase, readTarget=None):
    with readModule(readTarget) as r:
        l1 = r.rl()
        l2 = r.rl()
        l3 = r.rl()
        testcase.assertEqual(l1, 'line1 this is line1\r\n')
        testcase.assertEqual(l2, ' line2 this is line2 \n')
        testcase.assertEqual(l3, 'what this line')
        pass
    pass


def TemplateTest2(testcase, readTarget=None):
    with readModule(readTarget) as r:
        l1 = r.rl()
        l2 = r.rl()
        l3 = r.rl()
        l4 = r.rl()
        testcase.assertEqual(
            l1, 'line1 this is line1\r line2 this is line2 \n')
        testcase.assertEqual(l2, 'what this line\n')
        testcase.assertEqual(l3, '\n')
        testcase.assertEqual(l4, 'line after double nl')
        pass
    pass


def TemplateTest3(testcase, readTarget=None):
    with readModule(readTarget) as r:
        t1 = r.rt()
        t2 = r.rt()
        t3 = r.rt()
        t4 = r.rt()
        t5 = r.rt()
        t6 = r.rt()
        testcase.assertEqual(t1, 'token1')
        testcase.assertEqual(t2, 'token2')
        testcase.assertEqual(t3, 'token3')
        testcase.assertEqual(t4, 't')
        testcase.assertEqual(t5, 'o')
        testcase.assertEqual(t6, 'ken')
        pass
    pass


def TemplateTest4(testcase, readTarget=None):
    with readModule(readTarget) as r:
        ans = [r.rt(), r.rl(), r.rl(), r.rt(), r.rt(), r.rt(), r.rl()]
        testcase.assertEqual(ans, ['token1', 'this is line after token', ' next line \r\n',
                                   'token', 'after', 'line', 'line after read all token of tokenline'])
        pass
    pass


def TemplateTest5(testcase, readTarget=None):
    with readModule(readTarget) as r:
        ans = [r.ri(), r.ri(), r.ri(), r.ri(), r.rf(), r.rs('utf-8'), r.rs()]
        testcase.assertEqual(ans, [12, 3, 42, 452, 4.324, u'hello', u'world!'])
        pass
    pass

def TemplateTest6(testcase, readTarget=None):
    with readModule() as r:
        ans = r.rnt(6)
        testcase.assertEqual(ans, ['2','3','23','3.24', 'asdv','dd'])
        pass
    pass

# TestData1 = io.BytesIO('line1 this is line1\r\n line2 this is line2 \nwhat this line')
TestData1 = 'line1 this is line1\r\n line2 this is line2 \nwhat this line'
TestData2 = 'line1 this is line1\r line2 this is line2 \nwhat this line\n\nline after double nl'
TestData3 = 'token1 token2 \r\n token3 \n\n t o\rken'
TestData4 = 'token1 this is line after token \r\n next line \r\n\n token after line \nline after read all token of tokenline'
TestData5 = '12 3 42\r\n 452 4.324 hello\nworld!'
TestData6 = '2 3 23\n 3.24 asdv\tdd'

@unittest.skip('BytesIOAsInputStdinTestcase disable')
class BytesIOAsInputStdinTestcase(unittest.TestCase):

    @patch('sys.stdin', new=io.BytesIO(TestData1), create=True)
    def test1SimpleLineRead1(self):
        TemplateTest1(self)

    @patch('sys.stdin', new=io.BytesIO(TestData2), create=True)
    def test2SimpleLineRead2(self):
        TemplateTest2(self)
        pass

    @patch('sys.stdin', new=io.BytesIO(TestData3), create=True)
    def test3SimpleTokenRead1(self):
        TemplateTest3(self)
        pass

    @patch('sys.stdin', new=io.BytesIO(TestData4), create=True)
    def test4MixedRead1(self):
        TemplateTest4(self)
        pass

    @patch('sys.stdin', new=io.BytesIO(TestData5), create=True)
    def test5DataRead1(self):
        TemplateTest5(self)
        pass

    @patch('sys.stdin', new=io.BytesIO(TestData6), create=True)
    def test6DataRead2(self):
        TemplateTest6(self)
        pass

@patch('os.stat')
@patch('Pypy2app.open', new_callable=mock.mock_open, create=True)
@unittest.skip('BytesIOAsInputFileTestcase disable')
class BytesIOAsInputFileTestcase(unittest.TestCase):
    def setUp(self):
        return super(BytesIOAsInputFileTestcase, self).setUp()
    # @skip('reassson')

    @patch('mmap.mmap')
    def test1SimpleLineRead1(self, f, popen, pstat):
        pstat.return_value.return_value = 23244
        f.return_value = io.BytesIO(TestData1)
        TemplateTest1(self, defs.InputFileName)
        pass

    @patch('mmap.mmap')
    def test2SimpleLineRead2(self, f, popen, pstat):
        pstat.return_value.return_value = 23244
        f.return_value = io.BytesIO(TestData2)
        TemplateTest2(self, defs.InputFileName)
        pass
        
    @patch('mmap.mmap')
    def test3SimpleTokenRead1(self, f, popen, pstat):
        pstat.return_value.return_value = 23244
        f.return_value = io.BytesIO(TestData3)
        TemplateTest3(self, defs.InputFileName)
        pass

    @patch('mmap.mmap')
    def test4MixedRead1(self, f, popen, pstat):
        pstat.return_value.return_value = 23244
        f.return_value = io.BytesIO(TestData4)
        TemplateTest4(self, defs.InputFileName)
        pass

    @patch('mmap.mmap')
    def test5DataRead1(self, f, popen, pstat):
        pstat.return_value.return_value = 23244
        f.return_value = io.BytesIO(TestData5)
        TemplateTest5(self, defs.InputFileName)
        pass

    # @skip('reassson')

    # @patch('mmap.mmap', new = io.BytesIO(TestData2))
    # def test2SimpleLineRead2(self, popen, pstat):
    #     pstat.return_value.return_value = 23244
    #     TemplateTest2(self, defs.InputFileName)
    #     pass

        
    # @patch('mmap.mmap', new = io.BytesIO(TestData3))
    # def test3SimpleTokenRead1(self, popen, pstat):
    #     pstat.return_value.return_value = 23244
    #     TemplateTest3(self)
    #     pass

    # @patch('mmap.mmap', new = io.BytesIO(TestData4))
    # def test4MixedRead1(self, popen, pstat):
    #     pstat.return_value.return_value = 23244
    #     TemplateTest4(self)
    #     pass

    # @patch('mmap.mmap', new = io.BytesIO(TestData5))
    # def test5DataRead1(self, popen, pstat):
    #     pstat.return_value.return_value = 23244
    #     TemplateTest5(self)
    #     pass


@unittest.skip('StringIOAsInputStdinTestcase disable')
class StringIOAsInputStdinTestcase(unittest.TestCase):
    def test1StringSimpleLineRead1(self):
        stringioasstdin1 = io.StringIO(
            u'line1 this is line1\r\n line2 this is line2 \nwhat this line')
        with patch('sys.stdin', stringioasstdin1, create=True):
            with readModule() as r:
                l1 = r.rl()
                l2 = r.rl()
                l3 = r.rl()
                self.assertEqual(l1, 'line1 this is line1\r\n')
                self.assertEqual(l2, ' line2 this is line2 \n')
                self.assertEqual(l3, 'what this line')
                pass
            pass
        pass

    def test2StringSimpleLineRead2(self):
        stringioasstdin2 = io.StringIO(
            u'line1 this is line1\r line2 this is line2 \nwhat this line')
        with patch('sys.stdin', stringioasstdin2, create=True):
            with readModule() as r:
                l1 = r.rl()
                l3 = r.rl()
                self.assertEqual(
                    l1, 'line1 this is line1\r line2 this is line2 \n')
                self.assertEqual(l3, 'what this line')
                pass
            pass
        pass

    pass



def suite():
    result = unittest.TestSuite()
    result.addTests(unittest.makeSuite(SimpleTest))
    result.addTests(unittest.makeSuite(BytesIOAsInputStdinTestcase))
    result.addTests(unittest.makeSuite(StringIOAsInputStdinTestcase))
    result.addTests(unittest.makeSuite(BytesIOAsInputFileTestcase))
    return result


if __name__ == '__main__':
    unittest.main()