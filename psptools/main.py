#[Preprocess]#ifdef python2
# -*- coding:utf-8 -*-
from __future__ import print_function
#[Preprocess]#endif
#!/usr/bin/env python

#NYAN NYAN
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
#░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
#░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
#░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░
#░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░
#░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░
#░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░
#░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░
#░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░
#░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░
#░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░
#░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

#[Preprocess]#exclude
import sys
import processor
#[Preprocess]#endexclude

import sys
#[Preprocess]#ifdef boj

#[Preprocess]#else
import logging
import logging.handlers
#[Preprocess]#endif

#[Preprocess]#ifdef debug
IO_Dir = '.'
import io
import os
import time
from datetime import datetime
#[Preprocess]#endif

#[Preprocess]#ifdef UseFileIO
import mmap
InputFileName = 'input.txt'
OutputFileName = 'output.txt'
ReadTarget = os.path.join(IO_Dir, InputFileName)
WriteTarget = os.path.join(IO_Dir, OutputFileName)
#[Preprocess]#else
ReadTarget = None
WriteTarget = None
#[Preprocess]#endif

def convert_to_bytes(arg):
	if isinstance(arg, bytes):
		if(sys.version_info[0] >= 3):
			return str(arg)
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
		return str(arg)

# Copyright (c) 2018 Maxim Buzdalov
class edx_in:
	def __init__(self, target = None):
		self.target = target
	def create_lineTokenizer(self):
		if(self.mm):
			for line in iter(self.mm.readline, ''):
				yield line
		else:
			for line in iter(self.stream.readline, ''):
				yield line

	def __enter__(self):
#[Preprocess]#ifdef UseFileIO
		if(self.target):
			if(os.path.exists(self.target)):
				self.isFileEmpty = os.stat(self.target).st_size == 0
				if(self.isFileEmpty):
					return self
			else:
				with open(self.target, 'w', encoding='utf-8') as newf:
					newf.write('')
				return self
			# if(sys.version_info[0] > 3):
			# 	self.stream = open(self.target, 'r', encoding='utf-8')
			# else:
			# 	self.stream = open(self.target, 'rb', 1)
			self.stream = open(self.target, 'r', 1, encoding='utf-8')
			self.mm = mmap.mmap(self.stream.fileno(), 0, access=mmap.ACCESS_READ)
		else:
			self.mm = None
			self.isFileEmpty = True
			self.stream = sys.stdin
#[Preprocess]#else
		self.mm = None
		self.isFileEmpty = True
		self.stream = sys.stdin
#[Preprocess]#endif

		self.lines = self.create_lineTokenizer()

		self.lineTokens = None
		return self

	def __exit__(self, type, value, traceback):
		if(not self.isFileEmpty):
			if(self.mm):
				self.mm.close()
			self.stream.close()
	def next_line(self):
		ret = None
		try:
			if(sys.version_info[0]<3):
				ret = b' '.join(self.lineTokens)
			else:
				ret = ' '.join(self.lineTokens)
			self.lineTokens.close()
			if(ret == ''):
				raise ValueError()
			return ret
		except:
			pass

		if(hasattr(self.lines, 'next')):
			ret = self.lines.next()
		if(hasattr(self.lines, '__next__')):
			ret = self.lines.__next__()
		return ret
	def next_int(self):
		return int(self.next_token())

	def next_float(self):
		return float(self.next_token())
	def next_str(self,encoding = sys.stdin.encoding):
		if(encoding):
			return self.next_token().decode(encoding)
		else:
			return self.next_token()
		#return self.next_token().decode('utf-8')
	def getLineTokens(self, line):
		for token in iter(line.split()):
			yield token
	def nextNToken(self, rep = 0):

		ans = []
		while(rep > 0):
			ans.append(self.next_token())
			rep -= 1
		#TODO : Determine return value : iterator? or joined string? or array?
		return ans
	def next_token(self):
		try:
			if(hasattr(self.lineTokens, 'next')):
				ret = self.lineTokens.next()
			if(hasattr(self.lineTokens, '__next__')):
				ret = self.lineTokens.__next__()
			
			return ret
		except:
			self.lineTokens = self.getLineTokens(self.next_line())

			return self.next_token()

	#def all_tokens(self):
	#	return self.tokens

class edx_out:
	def __init__(self, target = None):
		self.target = target

	def __enter__(self):
		import platform
		self.is_cpython = (platform.python_implementation() == 'CPython')
#[Preprocess]#ifdef UseFileIO
		if(self.target):
			if self.is_cpython:
				# if(sys.version_info[0] > 3):
				# 	self.stream = open(self.target, 'w', encoding='utf-8')
				# else:
				# 	self.stream = open(self.target, 'wb', 1)
				self.stream = open(self.target, 'w', 1, encoding='utf-8')
			else:
				if(sys.version_info[0] >= 3):
					self.stream = open(self.target, 'w', 1, encoding='utf-8')
				else:
					self.stream = io.BytesIO()
#[Preprocess]#else
		if(False):
			pass
#[Preprocess]#endif
		else:
			self.stream = sys.stdout
		return self

	def __exit__(self, type, value, traceback):
#[Preprocess]#ifdef UseFileIO
		if(self.target):
			if self.is_cpython:
				self.stream.close()
			else:
				# if(sys.version_info[0] > 3):
				# 	outf = open(self.target, 'w', encoding='utf-8')
				# else:
				# 	outf = open(self.target, 'wb', 1)
				outf = open(self.target, 'w', 1, encoding='utf-8')
				outf.write(self.stream.getvalue())
				outf.close()
				self.stream.close()
#[Preprocess]#else
		pass
#[Preprocess]#endif
	def write(self, arg):
		self.stream.write(convert_to_bytes(arg))

	def writeln(self, arg):
		self.write(arg)
		self.write(b'\n')

	def test(this, expression):
		frame = sys._getframe(1)
		exp = expression
		ans = repr(eval(exp, frame.f_globals, frame.f_locals))
		this.debug('test : ' + exp + ' = ' + ans)
		pass
	
#endregion Default IO Functions

sys.setrecursionlimit(2000)

#region Helper Functions

#[Preprocess]#ifdef PreBuild
import functools
from functools import wraps

def counted(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		wrapper.count += 1
		return func(*args, **kwargs)
	wrapper.count = 0
	return wrapper

#[Preprocess]#endif

#[Preprocess]#ifdef it
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def it():
	put('it')
	pass
#[Preprocess]#endif

#[Preprocess]#ifdef useless
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def useless():
	# put(useless)
	pass
#[Preprocess]#endif

#[Preprocess]#ifdef modmul
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def modmul():
	return 0
#[Preprocess]#endif

#[Preprocess]#ifdef memoized
import collections
import functools
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
class memoized(object):
	'''Decorator. Caches a function's return value each time it is called.
	If called later with the same arguments, the cached value is returned
	(not reevaluated).
	'''
	#[Preprocess]#ifdef PreBuild
	#[Preprocess]#endif
	def __init__(self, func):
		self.func = func
		self.cache = {}
	def __call__(self, *args):
		if not isinstance(args, collections.Hashable):
			# uncacheable. a list, for instance.
			# better to not cache than blow up.
			return self.func(*args)
		if args in self.cache:
			return self.cache[args]
		else:
			value = self.func(*args)
			self.cache[args] = value
			return value
		def __repr__(self):
			'''Return the function's docstring.'''
			return self.func.__doc__
		def __get__(self, obj, objtype):
			'''Support instance methods.'''
			return functools.partial(self.__call__, obj)
#[Preprocess]#endif

#[Preprocess]#ifdef ToSpaceSeperatedString
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def ToSpaceSeperatedString(targetList):
	return " ".join(map(str, targetList))
#[Preprocess]#endif

#[Preprocess]#ifdef combination
import operator
import functools
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def combination(n, r):
	r = min(r, n - r)
	if(r == 0):
		return 1
	if(r < 0): 
		return 0
	
	numer = functools.reduce(operator.mul, range(n, n - r, -1))
	denom = functools.reduce(operator.mul, range(1, r + 1))
	return numer // denom
#[Preprocess]#endif

#[Preprocess]#ifdef sumdigit
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def sumdigit(num):
	num = str(num)
	r = 0
	for x in num:
		r = r + int(x)
		pass

	return r
#[Preprocess]#endif

#[Preprocess]#ifdef digitListToInt
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def digitListToInt(numList):
	return int(''.join(map(str, numList)))
#[Preprocess]#endif

#[Preprocess]#ifdef listByDigit
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def listByDigit(digitLen):
	return [0 for _ in range(digitLen)]
#[Preprocess]#endif

#[Preprocess]#ifdef Fibonacci
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def Fibonacci(n, k):
	ans = 0
	for x in range(1, n):
		ans = ans + x * C(n - x, k - 1)

		pass
	return ans
	pass
#[Preprocess]#endif

#[Preprocess]#ifdef keyOfMaxValue
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def keyOfMaxValue(d1):
	'''
	O(n)
	'''
	v = list(d1.values())
	return list(d1.keys())[v.index(max(v))]
#[Preprocess]#endif

#[Preprocess]#ifdef checkProperIrreducible
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def checkProperIrreducible(a, b):
	if(a == 1):
		return True
	if(a == b):
		return False
	if(a > b):
		return checkProperIrreducible(b, a)
	else:
		return checkProperIrreducible(a, b - a)
#[Preprocess]#endif

#[Preprocess]#ifdef MultiArray
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
class MultiArray(object):

	def MultiArray(defaultList, listCount):
		this.Lists[0] = defaultList
		for i in range(1,listCount):
			this.Lists[i] = list()
		pass

	def MultiArray(listCount):
		for i in range(listCount):
			this.Lists[i] = list()

		pass

	def MakeRankList(idx):
		input = this.Lists[0]
		output = [0] * len(input)
		for i, x in enumerate(sorted(range(len(input)), key=lambda y: input[y])):
			output[x] = i
		this.Lists[idx] = output
		pass
#[Preprocess]#endif

#[Preprocess]#ifdef longDivisionDigits
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def longDivisionDigits(dividend, divisor):    
	d = dividend
	while True:      
		yield d // divisor
		d = d % divisor * 10    
#[Preprocess]#endif


#endregion


def solve():
	val1 = ri()
	str1 = rs()
	debug(val1, str1)
	put(str1 + str(val1))
	pass

# logging

#[Preprocess]#ifdef debug

def gettime():
#[Preprocess]#ifdef datetime
	return str(datetime.now())
#[Preprocess]#else
	return 'no datetime'
#[Preprocess]#endif
def memory():
	pass

logf = io.open(os.path.join(IO_Dir, "log.txt"), "a", encoding='utf-8')

if(sys.version_info[0] < 3):
	content = (gettime() + " | Program started.\n").encode('utf-8')
	logf.write(unicode(content))
else:
	content = (gettime() + " | Program started.\n")
	logf.write(content)
def log(str1):
	if(sys.version_info[0] < 3):
		print(unicode(str1), file = logf)
	else:
		print(str1, file = logf)
	pass

pass
#[Preprocess]#else

#[Preprocess]#endif
try:
	logger1 = logging.getLogger('log1')
	debug = lambda *x: logger1.log(logging.DEBUG,convert_to_bytes(x))
		
	PutLevel = 100
	logging.PUT = PutLevel
	logging.addLevelName(PutLevel, 'PUT')
#[Preprocess]#ifdef debug
	logger1.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(levelname)-8s:%(message)s')
	debugHandler = logging.StreamHandler(sys.stdout)
	debugHandler.setFormatter(formatter)
	logger1.addHandler(debugHandler)
#[Preprocess]#else
	logger1.setLevel(logging.PUT)
	formatter = logging.Formatter()
#[Preprocess]#endif
except:
	pass

#WriteTarget = None
with edx_in(ReadTarget) as Reader, edx_out(WriteTarget) as Writer:

	try:
#[Preprocess]#ifdef debug
		if(Writer.stream == sys.stdout):
			logger1.removeHandler(debugHandler)
#[Preprocess]#endif
		outHandler = logging.StreamHandler(Writer.stream)
		outHandler.setFormatter(formatter)
		logger1.addHandler(outHandler)
		if(sys.version_info[0] >= 3):
			put = lambda *args: logger1.log(logging.PUT,convert_to_bytes(args))
			info = lambda *args: logger1.log(logging.INFO,convert_to_bytes(args))
			critical = lambda *args: logger1.log(logging.CRITICAL,convert_to_bytes(args))
		else:
			put = lambda *args: logger1.log(logging.PUT,convert_to_bytes(args))
			info = lambda *args: logger1.log(logging.INFO,convert_to_bytes(args))
			critical = lambda *args: logger1.log(logging.CRITICAL,convert_to_bytes(args))
	except ModuleNotFoundError: # judge does not have logging module.
		debug = Writer.writeln
		put = Writer.writeln
		info = Writer.writeln
		critical = Writer.writeln
#[Preprocess]#ifdef debug
	debug("Start------------------------")
	duration = time.time()
	pass
#[Preprocess]#else
	def nop(*arg):
		pass
	debug = nop
	test = nop
	info = nop
#[Preprocess]#endif

	reader = Reader
	writer = Writer
	ri = reader.next_int
	rs = reader.next_str
	rt = reader.next_token
	rf = reader.next_float
	rl = reader.next_line
	rnt = reader.nextNToken
	wl = writer.writeln

	solve()
#[Preprocess]#ifdef debug
	debug("End------------------------")
	duration = time.time() - duration
	debug("running time : " + str(duration))
	if(sys.version_info[0] >= 3):
		try:
			import psutil
			log("memory : " + str(psutil.Process().memory_info()[0]))
			pass
		except ModuleNotFoundError:
			print('psutil not installed. skipped memory log')
			pass
		pass
	logf.close()
	pass
#[Preprocess]#endif


