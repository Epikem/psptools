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
		try:
			print(os.getcwd())
			os.chdir(os.path.relpath('./psptools/'))
			os.system('python processor.py')
			
			
		except:
			assert(1==2)
			pass
		pass

	def xtest_edxin_readString(self):
		print(os.getcwd())
		os.chdir(os.path.relpath('./psptools/'))
		os.system('python processor.py')
		pass