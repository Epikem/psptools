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



InputFileName = 'input.txt'
OutputFileName = 'output.txt'
ReadTarget = None
WriteTarget = None

#endregion Defines


import os
import sys
import codecs
IO_Dir = '.'

import fileinput
import codecs
import operator
import functools
import math
import io
import platform
import collections
import mmap
import logging
import logging.handlers


from datetime import datetime

def convertoToBytes(arg):
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
			return ' '.join(list(map(convertoToBytes, arg)))
		else:
			return b' '.join(map(convertoToBytes, arg))
	else:
		if(sys.version_info[0] >= 3):
			return str(arg)
		return str(arg).encode('utf-8')

#region Default IO Functions
# def convertoToBytes(arg):
# 	print('convertToBytes')
# 	# return str(arg)
# 	if isinstance(arg, bytes):
# 		# if(sys.version_info[0] >= 3):
# 		# 	return str(arg)
# 		return arg
# 	elif isinstance(arg, str):
# 		if(sys.version_info[0] >= 3):
# 			return arg.encode('utf-8')
# 		else:
# 			return arg.encode('utf-8')
# 	elif hasattr(arg, '__iter__'):
# 		print('convert')
# 		if(sys.version_info[0] >= 3):
# 			return b' '.join(map(convertoToBytes, arg))
# 		else:
# 			return b' '.join(map(convertoToBytes, arg))
# 	else:
# 		return str(arg).encode('utf-8')

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
			ret = b' '.join(self.lineTokens)
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
	def next_str(self,encoding = None):
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
		else:
			self.stream = sys.stdout
		return self

	def __exit__(self, type, value, traceback):
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
	def write(self, arg):
		self.stream.write(convertoToBytes(arg))

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


def it():
	put('it')
	pass








def combination(n, r):
	r = min(r, n - r)
	if(r == 0):
		return 1
	if(r < 0): 
		return 0
	
	numer = functools.reduce(operator.mul, range(n, n - r, -1))
	denom = functools.reduce(operator.mul, range(1, r + 1))
	return numer // denom










#endregion


def solve():
	in1 = ri()
	put(in1)
	debug(in1)
	put('@@@@@')
	debug('wwwww')
	put('asddssdsd')
	it()
	put(combination(6,2))
	pass




















#logging



reader = None
writer = None

ReadTarget = os.path.join(IO_Dir, InputFileName)
WriteTarget = os.path.join(IO_Dir, OutputFileName)




try:
	logger1 = logging.getLogger('log1')
	debug = lambda *x: logger1.log(logging.DEBUG,convertoToBytes(x))
		
	PutLevel = 100
	logging.PUT = PutLevel
	logging.addLevelName(PutLevel, 'PUT')
	logger1.setLevel(logging.PUT)
	formatter = logging.Formatter()
	#put = lambda x: logger1.log(100,x)
	#info = lambda x: logger1.log(logging.INFO,x)
	#critical = lambda x: logger1.log(logging.CRITICAL,x)
except:
	pass

#WriteTarget = None
with edx_in(ReadTarget) as Reader, edx_out(WriteTarget) as Writer:

	try:
		outHandler = logging.StreamHandler(Writer.stream)
		outHandler.setFormatter(formatter)
		logger1.addHandler(outHandler)
		if(sys.version_info[0] >= 3):
			put = lambda *args: logger1.log(logging.PUT,convertoToBytes(args))
			info = lambda *args: logger1.log(logging.INFO,convertoToBytes(args))
			critical = lambda *args: logger1.log(logging.CRITICAL,convertoToBytes(args))
		else:
			put = lambda *args: logger1.log(logging.PUT,convertoToBytes(args))
			info = lambda *args: logger1.log(logging.INFO,convertoToBytes(args))
			critical = lambda *args: logger1.log(logging.CRITICAL,convertoToBytes(args))
	except:
		debug = Writer.writeln
		put = Writer.writeln
		info = Writer.writeln
		critical = Writer.writeln
	def nop(*arg):
		pass
	debug = nop
	test = nop
	info = nop

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


