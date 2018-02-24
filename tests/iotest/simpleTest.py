import sys
try:
    import unittest2 as unittest
except ImportError:
    import unittest
from unittest import SkipTest, TestCase
import functools
import types
import os
import sys
import fileinput
import io

from subprocess import call

class MainTestCase(TestCase):
	def test_main(self):
		# import codecs
		# utf8reader = codecs.getreader('utf-8')
		# utf8writer = codecs.getwriter('utf-8')
		# utf8error = codecs.getwriter('utf-8')

		# sys.stdin = utf8reader(sys.stdin)
		# sys.stdout = utf8writer(sys.stdout)
		# sys.stderr = utf8error(sys.stderr)

		# print(os.getcwd())
		print()
		os.chdir(os.path.relpath('./psptools/'))
		os.system('python main.py')
		pass

	def xtest_edxin_readString(self):
		# print(os.getcwd())
		os.chdir(os.path.relpath('./psptools/'))
		os.system('python processor.py')
		pass