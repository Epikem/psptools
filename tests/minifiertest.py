import sys
try:
	import unittest2 as unittest
except ImportError:
	import unittest

import tests.utils as utils
import psptools.minifier

class SimpleProcessTest(unittest.TestCase):

	def setUp(self):
		super(SimpleProcessTest, self).setUp()
		utils.make_folder()

	def tearDown(self):
		utils.remove_recursively()
		super(SimpleProcessTest, self).tearDown()

	def test1CheckFolderExistance(self):
		import os
		v = os.path.exists('testfolder')
		
		assert(v == True)
		pass

	def test2ReadTargetProgramData(self):
		# import psptools.minifier
		# program = 'print(1 + 2)'
		# minifier = minifier()
		# res = minifier.minify(program)
		
		# assert(program==res)

		pass
	def test3AssureSameOutputWithNoExplicitSettings(self):
		assert(1==2)
		pass
		
	# @unittest.skip('what')
	def test4LoggingTest(self):
		def convert_to_bytes(arg):
			if isinstance(arg, bytes):
				if(sys.version_info[0] >= 3):
					return arg.decode('utf-8')
				return arg
			elif isinstance(arg, str):
				if(sys.version_info[0] >= 3):
					return arg
				else:
					return arg.encode('utf-8')
			elif hasattr(arg, '__iter__'):
				if(sys.version_info[0] >= 3):
					return ' '.join(list(map(convert_to_bytes, arg)))
				else:
					return b' '.join(map(convert_to_bytes, arg))
			else:
				return str(arg).encode('utf-8')
		import logging
		logging.basicConfig(level = 10000)
		logger1 = logging.getLogger(name = 'What')
		logger1.setLevel(-1)
		print('dsdd')
		logger1.log(logging.CRITICAL, logging.DEBUG)
		logger1.log(logging.DEBUG, 'asddsadasds')
		logger1.log(logging.CRITICAL, logging.CRITICAL)
		def lam(*x):
			logger1.log(logging.DEBUG,convert_to_bytes(x))

		debug = lam
		debug = lambda *x: logger1.log(logging.DEBUG,convert_to_bytes(x))
		debug('debug1', 'debug 2')
		debug(b'what')
		pass

	pass

	def test5IsolatedPypreprocessorLoggingTest(self):
		
		
		def convert_to_bytes(arg):
			if isinstance(arg, bytes):
				if(sys.version_info[0] >= 3):
					return arg.decode('utf-8')
				return arg
			elif isinstance(arg, str):
				if(sys.version_info[0] >= 3):
					return arg
				else:
					return arg.encode('utf-8')
			elif hasattr(arg, '__iter__'):
				if(sys.version_info[0] >= 3):
					return ' '.join(list(map(convert_to_bytes, arg)))
				else:
					return b' '.join(map(convert_to_bytes, arg))
			else:
				return str(arg).encode('utf-8')
		import logging
		logging.basicConfig(level = 10000)
		logger1 = logging.getLogger(name = 'What')
		logger1.setLevel(-1)
		print('dsdd')
		logger1.log(logging.CRITICAL, logging.DEBUG)
		logger1.log(logging.DEBUG, 'asddsadasds')
		logger1.log(logging.CRITICAL, logging.CRITICAL)
		def lam(*x):
			logger1.log(logging.DEBUG,convert_to_bytes(x))

		debug = lam
		debug = lambda *x: logger1.log(logging.DEBUG,convert_to_bytes(x))
		debug('debug1', 'debug 2')
		debug(b'what')
		pass


class InterpolateVariableTest(unittest.TestCase):

	def setUp(self):
		super(InterpolateVariableTest, self).setUp()
		utils.make_folder()


	def tearDown(self):
		utils.remove_recursively()
		super(InterpolateVariableTest, self).tearDown()

	def test1(self):
		pass

	pass

class InheritAndOverrideTest(unittest.TestCase):

	def setUp(self):
		super(InheritAndOverrideTest, self).setUp()
		utils.make_folder()


	def tearDown(self):
		utils.remove_recursively()
		super(InheritAndOverrideTest, self).tearDown()



	pass
class AutoInheritByPatternMatchingTest(unittest.TestCase):

	def setUp(self):
		super(AutoInheritByPatternMatchingTest, self).setUp()
		utils.make_folder()


	def tearDown(self):
		utils.remove_recursively()
		super(AutoInheritByPatternMatchingTest, self).tearDown()



	pass
def suite():
	result = unittest.TestSuite()
	result.addTests(unittest.makeSuite(SimpleProcessTest))
	result.addTests(unittest.makeSuite(InterpolateVariableTest))
	result.addTests(unittest.makeSuite(InheritAndOverrideTest))
	result.addTests(unittest.makeSuite(AutoInheritByPatternMatchingTest))
	return result

if __name__ == '__main__':
	unittest.main()
