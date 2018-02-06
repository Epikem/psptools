import os
#[Preprocess]#exclude
import sys

from pypreprocessor import pypreprocessor

#region Defines

if sys.version[:3].split('.')[0] == '2':
	pypreprocessor.defines.append('python2')
	pass
if sys.version[:3].split('.')[0] == '3':
	pypreprocessor.defines.append('python3')
	pass
if 'boj' in sys.argv:
	pypreprocessor.defines.append('boj')
if 'debug' in sys.argv:
	pypreprocessor.defines.append('debug')

# run the script in 'postprocessed' mode
elif 'postprocessed' in sys.argv:
	pypreprocessor.defines.append('postprocessed')
else:
	sys.argv.append('production')
	if 'production' in sys.argv:
		pypreprocessor.defines.append('production')
		pypreprocessor.removeMeta = True
def TryAppend(moduleName):
	if(not moduleName in pypreprocessor.defines):
		pypreprocessor.defines.append(moduleName)
def TryRemove(moduleName):
	try:
		pypreprocessor.defines.remove(moduleName)
		pass
	except:
		pass


li = []
li.append('it')
li.append('useless')
li.append('modmul')
li.append('memoized')
li.append('ToSpaceSeperatedString')
li.append('combination')
li.append('sumdigit')
li.append('digitListToInt')
li.append('listByDigit')
li.append('Fibonacci')
li.append('keyOfMaxValue')
li.append('checkProperIrreducible')
li.append('MultiArray')
li.append('longDivisionDigits')
for name in li:
	TryAppend(name)

def registerUsedFunctions():
	# li.append('it')

	#region Pre Build
	pypreprocessor.readEncoding = 'utf-8'
	pypreprocessor.input = 'main.py'
	pypreprocessor.output = 'tmp.py' # run mode
	pypreprocessor.run = True
	pypreprocessor.resume = True
	pypreprocessor.save = False

	TryAppend('PreBuild')
	# TryAppend('readSequence')
	TryAppend('debug')
	TryAppend('UseFileIO')
	TryRemove('boj')


	pypreprocessor.parse()

	
	TryRemove('PreBuild')
	#endregion Pre Build

	pass
# registerUsedFunctions()


# # #region Publish Build
# pypreprocessor.continueExecution = False
# pypreprocessor.output = 'solution.py'
# # pypreprocessor.run = False
# TryRemove('debug')
# TryRemove('UseFileIO')
# TryAppend('boj')
# pypreprocessor.parse()
# # #endregion Publish Build

#[Preprocess]#endexclude

#[Preprocess]#ifdef PreBuild
from functools import wraps

def counted(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		wrapper.count += 1
		return func(*args, **kwargs)
	wrapper.count = 0
	return wrapper

# def counted(f):
#     def wrapped(*args, **kwargs):
#         wrapped.calls += 1
#         return f(*args, **kwargs)
#     wrapped.calls = 0
#     return wrapped

#[Preprocess]#endif

# #[Preprocess]#ifdef it
# #[Preprocess]#ifdef PreBuild
# @counted
# #[Preprocess]#endif
# def it():
# 	put('it')
# 	pass
# #[Preprocess]#endif

#[Preprocess]#exclude

#region Debug Build
pypreprocessor.escapeChar = '#[Preprocess]#'
pypreprocessor.encoding = 'utf-8'

pypreprocessor.input = 'main.py'
pypreprocessor.output = 'debug.py' # run mode
pypreprocessor.resume = True
pypreprocessor.run = False
pypreprocessor.save = True
pypreprocessor.removeMeta = True
TryAppend('PreBuild')
TryAppend('readSequence')
TryAppend('debug')
TryAppend('UseFileIO')
TryAppend('it')
TryAppend('datetime')
TryRemove('boj')
pypreprocessor.parse()
	# except:
	# 	pass
		
import importlib
from debug import *
def str_to_class(str):
	from functools import reduce
	
	return reduce(getattr, str.split("."), sys.modules[__name__])
for name in li:
	# try:
	if(str_to_class(name).count == 0):
		TryRemove(name)

#endregion Debug Build

#region Solution Build

pypreprocessor.input = 'main.py'
pypreprocessor.output = 'solution.py' # run mode
pypreprocessor.resume = False
pypreprocessor.run = False
pypreprocessor.save = True
# pypreprocessor.run = True
TryRemove('PreBuild')
# TryAppend('readSequence')
TryRemove('debug')
TryAppend('UseFileIO')
TryRemove('boj')
pypreprocessor.parse()

#endregion


#[Preprocess]#endexclude