# -*- coding:utf-8 -*-
from __future__ import print_function
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


import sys
ReadEncoding = sys.stdin.encoding
WriteEncoding = sys.stdout.encoding
LogEncoding = sys.stderr.encoding
ReadEncoding = 'utf-8'
WriteEncoding = 'utf-8'
LogEncoding = 'utf-8'
PythonVersion = sys.version_info[0]
ReadEncoding = 'bytes'
import logging
import logging.handlers


import mmap
import os
IO_Dir = '.'
InputFileName = 'input.txt'
OutputFileName = 'output.txt'
ReadTarget = os.path.join(IO_Dir, InputFileName)
WriteTarget = os.path.join(IO_Dir, OutputFileName)

def convert_to_bytes(arg):
	if(PythonVersion < 3):

		if isinstance(arg, bytes):
			return arg
		elif isinstance(arg, str):
			return arg.encode()
		elif hasattr(arg, '__iter__'):
			return b' '.join(map(convert_to_bytes, arg))
		else:
			return bytes(arg)
	else:
		if isinstance(arg, bytes):
			return arg.decode(WriteEncoding)
		elif isinstance(arg, str):
			return arg
		elif hasattr(arg, '__iter__'):
			return ' '.join(map(convert_to_bytes, arg))
		else:
			return str(arg)

		pass

	# if(WriteEncoding == 'bytes'):
	# 	if isinstance(arg, bytes):
	# 		return arg
	# 	elif isinstance(arg, str):
	# 		return arg.encode()
	# 	elif hasattr(arg, '__iter__'):
	# 		return b' '.join(map(convert_to_bytes, arg))
	# 	else:
	# 		return bytes(arg)
	# elif(WriteEncoding != 'bytes'):
	# 	if isinstance(arg, bytes):
	# 		return arg.decode(WriteEncoding)
	# 	elif isinstance(arg, str):
	# 		return arg
	# 	elif hasattr(arg, '__iter__'):
	# 		return ' '.join(map(convert_to_bytes, arg))
	# 	else:
	# 		return str(arg)
	# else:
	# 	raise ValueError

	if isinstance(arg, bytes):
		return arg.decode(WriteEncoding)
	elif isinstance(arg, str):
		return arg
	elif hasattr(arg, '__iter__'):
		return ' '.join(map(convert_to_bytes, arg))
	else:
		return str(arg)

	# if isinstance(arg, bytes):
	# 	if(PythonVersion >= 3):
	# 		return str(arg)
	# 	return arg
	# elif isinstance(arg, str):
	# 	if(PythonVersion >= 3):
	# 		return arg
	# 	else:
	# 		return arg.encode('utf-8')
	# elif hasattr(arg, '__iter__'):
	# 	if(PythonVersion >= 3):
	# 		return ' '.join(list(map(convert_to_bytes, arg)))
	# 	else:
	# 		return b' '.join(map(convert_to_bytes, arg))
	# else:
	# 	return str(arg)

# Copyright (c) 2018 Maxim Buzdalov. Modified by Epikem
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
				with open(self.target, 'w') as newf:
					newf.write('')
				return self
			# if(PythonVersion > 3):
			# 	self.stream = open(self.target, 'r', encoding='utf-8')
			# else:
			# 	self.stream = open(self.target, 'rb', 1)
			if(ReadEncoding == 'bytes'):
				self.stream = open(self.target, 'rb')
			else:
				self.stream = open(self.target, 'r', 1, ReadEncoding)
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
			if(ReadEncoding == 'bytes'):
				ret = b' '.join(self.lineTokens)
				if(ret == b''):
					raise ValueError()
			else:
				ret = ' '.join(self.lineTokens)
				if(ret == ''):
					raise ValueError()
		except (ValueError, TypeError) as e:
			self.lineTokens.close()			
			if(hasattr(self.lines, 'next')):
				ret = self.lines.next()
			if(hasattr(self.lines, '__next__')):
				ret = self.lines.__next__()
			pass
		finally:
			if(ReadEncoding == 'bytes'):
				ret = ret
			else:
				ret = ret.decode(ReadEncoding)
			return ret

	def next_int(self):
		return int(self.next_token())

	def next_float(self):
		return float(self.next_token())
	def next_str(self):
		ret = self.next_token()
		if(isinstance(ret, bytes)):
			return ret.decode()
		return ret
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

# Copyright (c) 2018 Maxim Buzdalov. Modified by Epikem
class edx_out:
	def __init__(self, target = None):
		self.target = target

	def __enter__(self):
		import platform
		self.is_cpython = (platform.python_implementation() == 'CPython')
		if(self.target):
			if self.is_cpython:
				# self.stream = open(self.target, 'wb', 1)

				if(PythonVersion < 3):
					self.stream = open(self.target, 'wb', 1)
				else:
					self.stream = open(self.target, 'w', 1, WriteEncoding)
			else:
				# self.stream = io.BytesIO()

				if(PythonVersion < 3):
					self.stream = io.BytesIO()
				else:
					self.stream = open(self.target, 'w', 1, WriteEncoding)
		else:
			self.stream = sys.stdout
		return self

	def __exit__(self, type, value, traceback):
		if(self.target):
			if self.is_cpython:
				self.stream.close()
			else:

				# outf = open(self.target, 'wb', 1)
				if(PythonVersion < 3):
					outf = open(self.target, 'wb', 1)
				else:
					outf = open(self.target, 'w', 1, WriteEncoding)
				outf.write(self.stream.getvalue())
				outf.close()
				self.stream.close()
	def write(self, arg):
		self.stream.write(convert_to_bytes(arg))

	def writeln(self, arg):
		if(WriteEncoding == 'bytes'):
			self.write(b'\n')
		else:
			self.write('\n')

	def test(this, expression):
		frame = sys._getframe(1)
		exp = expression
		ans = repr(eval(exp, frame.f_globals, frame.f_locals))
		if(WriteEncoding == 'bytes'):
			this.debug(b'test : ' + exp.encode(WriteEncoding) + b' = ' + ans.encode(WriteEncoding))
		else:
			this.debug('test : ' + exp + ' = ' + ans)
		pass
	
#endregion Default IO Functions

sys.setrecursionlimit(100)

#region Helper Functions

















#endregion


def solve():
	val1 = ri()
	str1 = rs()
	debug(val1, str1)
	put(str1 + str(val1))
	debug(rl())
	pass

# logging


try:
	logger1 = logging.getLogger('log1')
	debug = lambda *x: logger1.log(logging.DEBUG,convert_to_bytes(x))
		
	PutLevel = 100
	logging.PUT = PutLevel
	logging.addLevelName(PutLevel, 'PUT')
	logger1.setLevel(logging.PUT)
	formatter = logging.Formatter()
except:
	pass

#WriteTarget = None
with edx_in(ReadTarget) as Reader, edx_out(WriteTarget) as Writer:

	try:
		outHandler = logging.StreamHandler(Writer.stream)
		outHandler.setFormatter(formatter)
		logger1.addHandler(outHandler)
		if(PythonVersion >= 3):
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


