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
sys.exit(0)


#[Preprocess]#endexclude


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
#[Preprocess]#ifdef boj

#[Preprocess]#else
import logging
import logging.handlers
#[Preprocess]#endif

#[Preprocess]#ifdef debug
import time
#[Preprocess]#endif

from datetime import datetime
def convert_to_bytes(arg):
	if isinstance(arg, bytes):
		if(sys.version_info[0] >= 3):
			return str(arg)
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
		return str(arg)
		return str(arg).encode('utf-8')
# def convert_to_bytes(arg):
# 	if isinstance(arg, bytes):
# 		if(sys.version_info[0] >= 3):
# 			return str(arg)
# 			return arg.decode('utf-8')
# 		return arg
# 	elif isinstance(arg, str):
# 		if(sys.version_info[0] >= 3):
# 			return arg
# 		else:
# 			return arg.encode('utf-8')
# 	elif hasattr(arg, '__iter__'):
# 		if(sys.version_info[0] >= 3):
# 			return ' '.join(list(map(convert_to_bytes, arg)))
# 		else:
# 			return b' '.join(map(convert_to_bytes, arg))
# 	else:
# 		if(sys.version_info[0] >= 3):
# 			return str(arg).encode('utf-8')
# 		return str(arg).encode('utf-8')

#region Default IO Functions
# def convert_to_bytes(arg):
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
# 			return b' '.join(map(convert_to_bytes, arg))
# 		else:
# 			return b' '.join(map(convert_to_bytes, arg))
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
			print('222222222222sdsdsddsd@@@s')
			self.mm = None
			self.isFileEmpty = True
			self.stream = sys.stdin
#[Preprocess]#else
		print('@@@@@sd@@@s')
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
@counted
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



#[Preprocess]#ifdef readSequence
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def readSequence(elementType=None, inputLine=None, seperator=None, strip=True):
	global readTarget
	if (inputLine == None):
		inputLine = readTarget.readline()
	if strip:
		inputLine = inputLine.strip()
	if(isinstance(inputLine, bytes)):
#[Preprocess]#ifdef UseFileIO
		return inputLine
#[Preprocess]#else
		inputLine = inputLine.decode('utf-8')
#[Preprocess]#endif
	if (elementType == None):
		return [x for x in inputLine.split(seperator)]
	return [elementType(x) for x in inputLine.split(seperator)]
rl = RobertsSpaceIndustries = readSequence
#[Preprocess]#endif

#[Preprocess]#ifdef ToSpaceSeperatedString
#[Preprocess]#ifdef PreBuild
@counted
#[Preprocess]#endif
def ToSpaceSeperatedString(targetList):
	return " ".join(map(str, targetList))
#[Preprocess]#endif

#[Preprocess]#ifdef combination
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





#[Preprocess]#ifdef ArchiveBOJ
if(ArchiveBOJ):


	def solve4344():
		T = ri()
		for _ in range(T):
			n = ri()
			s = 0
			arr = []
			for i in range(n):
				arr.append(ri())
				s += arr[i]
			avg = s / n
			debug(avg)
			ans = 0
			for i in range(n):
				if(arr[i] > avg):
					ans += 1
			put('%.3f%%' % round((float(ans) / float(n) * 100.0),3))
			

			pass

		pass
	def solve1002():
		T = ri()
		for t in range(T):
			x1,y1,r1,x2,y2,r2 = map(int,rl().split())
			debug(x1,y1,r1,x2,y2,r2)
			import math
			dist = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
			debug(dist)
			r1, r2 = max(r1,r2), min(r1,r2)
			# r1, r2 = float(r1), float(r2)
			if(dist < r1):
				if(r1 - r2 > dist):
					put(0)
				elif(r1 - r2 == dist):
					if(r1 == r2):
						put(-1)
					else:
						put(1)
				else:
					put(2)
			elif(r1 + r2 > dist):
				put(2)
			elif(r1 + r2 == dist):
				put(1)
			else:
				put(0)
			pass

		pass
	def solve1463():
		n = ri()
		arr = [0] * 11
		for i in range(1, 4):
			try:
				arr[2 ** i] = i
			except:
				pass
			try:
				arr[3 ** i * 2] = i + 1
			except:
				pass
			try:
				arr[3 ** i] = i
			except:
				pass
		debug(arr)
		# 1 2 3 4

		pass
	def solve1719():
		global useit
		useit = True
		n,m = ri(),ri()	
		dist = {}
		ans = {}
		for i in it(m):
			a,b,v = ri(),ri(),ri()
			ans[a-1,b-1] = b-1
			ans[b-1,a-1] = a-1
			dist[a-1,b-1]=v
			dist[b-1,a-1]=v
			dist[a-1,a-1] = 0
			dist[b-1,b-1] = 0

			ans[a-1,a-1] = '-'
			ans[b-1,b-1] = '-'
		for i in it(n):
			l = ''
			for j in it(n):
				try:
					l += str(dist[i,j])+' '
				except:
					l += 'x '
			put(l)
		for time in range(1):
			for k in it(n):
				for i in it(n):
					for j in it(n):
						try:
							debug(dist[i,j])
							pass
						except:
							dist[i,j] = 999999
							pass
						if dist[i,j] > dist[i,k] + dist[k,j]:
							ans[i,j] = k
							dist[i,j] = dist[i,k] + dist[k,j]


		# for i in it(n):
		# 	l = ''
		# 	for j in it(n):
		# 		l += str(dist[i,j])+' '
		# 	put(l)

		for i in it(n):
			l = ''
			for j in it(n):
				if(i == j):
					l += '- '
				else:
					l += str(ans[i,j] + 1)+' '
			put(l.strip())



		pass
	


	def solve11718():
		while(True):
			try:
				put(rl().strip())
			except:
				break
		pass

	def solve7576():
		xlen,ylen = ri(),ri()
		map1 = {}
		xs=[]
		ys=[]
		startingPoints = []
		for y in range(0, ylen+2):
			for x in range(0, xlen+2):
				if(x == 0 or x == xlen+1 or y == 0 or y == ylen+1):
					map1[x,y] = -1
					continue
				map1[x,y] = ri()
				if(map1[x,y] == 1):
					xs.append(x)
					ys.append(y)
		def bfs(x, y, val = 0):
			if(map1[x,y] != 1):
				debug('no')
				return 0
			map1[x,y] = 1
			debug(x,y,map1[x,y])
			if(map1[x-1,y] != 0 and map1[x+1,y] != 0 and map1[x,y-1] != 0 and map1[x,y+1] != 0):
				return 0
			nexts = []
			if(map1[x-1,y] == 0):
				nexts.append((x-1,y))
			if(map1[x+1,y] == 0):
				nexts.append((x+1,y))
			if(map1[x,y-1] == 0):
				nexts.append((x,y-1))
			if(map1[x,y+1] == 0):
				nexts.append((x,y+1))
			maxp = val

			for nextp in nexts:
				tmp = bfs(map1, nextp[0], nextp[1], val + 1)
				if(tmp > maxp):
					maxp = tmp
			return maxp

			pass

			# rows.append(rl().split())
		maxp = 0
		for x, y in zip(xs,ys):
			debug(x,y)
			tmp = bfs(map1, x, y)
			if(tmp > maxp):
				maxp = tmp
				pass
			pass
		
		pass

	def solve2579():
		step = [0] * 330
		n = ri()
		@memoized
		def getmax(pos, con):
			debug('called')
			'''sdsdds
			dsdsdsdss
			'''
			p = pos
			debug(pos)
			if(p<0):
				return 0
			ret = 0
			b = 0
			if(con < 2):
				b = getmax(p-1,con+1)
				debug(p-1, step[p-1], 'b', b)
			if(p == n):
				debug('asddsads')
				return b + step[p]
			ret = max(getmax(p-2,1),b)
			debug(p, p-2, step[p-2], ret)
			debug(pos, ret)
			return ret + step[p]
		vals = [[0 for i in range(3)] for j in range(n+30)]
		# vals = {}
		for i in range(n):
			step[i] = ri()
			pass
		debug(step)
		put(getmax(n+1,1)) 
		pass



	def solve1094():
		n = ri()
		ans = 0
		cur = 64
		while(True):
			if(n < cur):
				cur /= 2
			else:
				n -= cur
				ans += 1
			if(n == 0):
				break
		put(ans)

	def solve2455():
		ri()
		maxp = 0
		cur = ri()
		if(maxp < cur):
			maxp = cur
		cur -= ri()
		cur += ri()
		if(maxp < cur):
			maxp = cur
		cur -= ri()
		cur += ri()
		if(maxp < cur):
			maxp = cur
		cur -= ri()
		put(maxp)

	def solve10871():
		n, x = ri(), ri()
		for i in range(n):
			val = ri()
			if(val < x):
				writer.write(str(val) + ' ')


	def solve10718():
		put("강한친구 대한육군")
		put("강한친구 대한육군")

	def solve11720():
		n = ri()
		narr = rs()
		ans = 0
		for i in range(n):
			ans += int(narr[i])
		put(ans)

	def solve10871():
		n, x = ri(), ri()
		for i in range(n):
			val = ri()
			if(val < x):
				writer.write(str(val) + ' ')

	def solve2750():
		n = ri()
		arr = []
		for i in range(n):
			arr.append(ri())
		arr.sort()
		for i in range(n):
			wl(arr[i])


	def solve1932():
		#fail
		tri = []
		arr = []
		dp = []
		def search(level):
			while(level > 0):
				nl = level - 1
				for i in range(len(tri[nl])):
					left = tri[level][i]
					right = tri[level][i+1]
					if(left>right):
						tri[nl][i] += left
					else:
						tri[nl][i] += right
				level -= 1
			return tri[0][0]
		n = ri()
		for i in range(n):
			spl = rl().split()
			dp.append([-1]*len(spl))
			tri.append(map(lambda x: int(x), spl))
		ans = search(n - 1)
		put(ans)
		pass
	def solve1152():
		a = rl()
		put(len(a.split()))
	def solve2749():
		n = ri()
		fib = [0,1]
		i = 1
		a, b = 1,1
		ans = a + b
		la, lb = 0,0
		while(i < n):
			la,lb = a,b
			a,b = a*21 + b*34, a*34 + b*55
			i+=10
			ans = a+b
		i/=10
		a,b = la,lb
		ans = a+b
		while(i < n):
			i*=2
			a,b = b,a+b
			ans = a+b
		i/=10
		a,b = la,lb
		ans = a+b
		while(i < n):
			i+=1
			a,b = b,a+b
			ans = a+b
		put(ans%1000000)
		#for i in range(2, n+1):
		#	fib.append(fib[i-1] + fib[i-2])
		#put(fib[n-1])

		#fn = fn-1 + fn-2 = (fn-2 + fn-3) + (fn-3 + fn-4) = (fn-3 + fn-4) + (fn-4 + fn-5) + (fn-4 + fn-5) + (fn-5 + fn-6)
	def solve2292():
		n = ri()
		li = [1]
		for i in range(1, n+1):
			li.append(li[-1]+ 6*(i-1))
			if(n <= li[-1]):
				put(li.index(li[-1]))
				break
	

		#[0,6,12,18]

	def solve8393():
		n = ri()
		ans = 0
		for i in range(1, n+1):
			ans+=i
		put(ans)
	def solve1924():
	
		wds = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
		#x,y = ri(), ri()
		#d = datetime(2007, x, y)
		#put(wds[d.weekday()])

		x,y = ri(), ri()
		stacktarget = [31,28,31,30,31,30,31,31,30,31,30,31]
		days = y
		for i in reversed(range(0,x - 1)):
			days += stacktarget[i]
		ans = wds[(days + 6)%7]
		put(ans)
	def solve2441():
		n = ri()
		for i in reversed(range(1,n+1)):
			put(' ' * (n - i) + '*'*i)
	def solve2440():
		n = ri()
		for i in reversed(range(1,n+1)):
			put('*'*i)
			#put(' ' * (n - i) + '*'*i)
	def solve2439():
		n = ri()
		for i in range(1,n+1):
			put(' ' * (n - i) + '*'*i)
	def solve2438():
		n = ri()
		for i in range(1,n+1):
			put('*'*i)
	def solve2739():
		n = ri()
		for i in range(1,10):
			put(str(n) + ' * ' + str(i) + ' = ' + str(n*i))
	def solve2742():
		n = ri()
		for i in reversed(range(1,n+1)):
			put(i)

	def solve2741():
		n = ri()
		for i in range(1,n+1):
			put(i)

	def solve2839():
		n = ri()
		i = (n / 5 + 1)
		w = 5 * i
		j = 0
	
		while(i >= 0):
			if(w == n):
				i = w / 5
				break
			if((n - w) % 3 == 0 and (n-w) > 0):
				j = (n - w) / 3
				break
			w -= 5
			i -= 1
		put(i+j)

	def solve2558():
		a, b = ri(), ri()
		put(a+b)


	def solve10430():
		a, b, c = ri(), ri(), ri()
		put((a+b)%c)
		put((a%c + b%c)%c)
		put((a*b)%c)
		put((a%c * b%c)%c)

	def solve10869():
		n = rs()[0]
		p = rs()
		t = rs()
		ans = 0
		pdone = False
		tdone = False
		mingap = 99999
		mingapidx = -1
		for i in range(n):
			if(p[i] > t[i]):
				mingap = (p[i] - t[i]) if (p[i] - t[i]) < mingap else mingap
				ans += p[i]
				pdone = True
			else:
				mingap = (t[i] - p[i]) if (t[i] - p[i]) < mingap else mingap
				ans += t[i]
				tdone = True
		if(not pdone):
			ans -= mingap
		elif(not tdone):
			ans -= mingap
		put(ans)
		a = ri()
		b = ri()
		put(a+b)
		put(a-b)
		put(a*b)
		put(a/b)
		put(a%b)

	def solve10998():
		a = ri()
		b = ri()
		put(a * b)

	def solve1008():
		a = rf()
		b = rf()
		put(a/b)

	def solve10172():
		#fail
		put(repr('|\_/|'))
		put(repr("|q p|   /}'"))
		put(repr('( 0 )"""\\'))
		put(repr('|"^"`    |\''))
		put(repr('||_/=\\__|\''))
#[Preprocess]#endif





#[Preprocess]#ifdef Archive
if(Archive):


	def solve903a():
		small = 3
		large = 7
		tests = ri()
		cur = 0
		ans = 'NO'
		for t in range(tests):
			ans = 'NO'
			x = ri()
			while(cur * small <= x):
				if((x - cur * small) % large == 0):
					ans = 'YES'
					break
				else:
					cur += 1
			if(ans == 'NO'):
				put('NO')
			else:
				put('YES')
			cur = 0
			x = 0
		
		pass
	#s
	def solve903b():
		steplist = []
		h1, a1, c1 = ri(),ri(),ri()
		h2, a2 = ri(),ri()
		curhp = h1
		enemyhp = h2
		strikeTimes = (h2 // a1) if h2 % a1 == 0 else (h2 // a1) + 1
		# h1 + c1 * x > a2 * (strikeTimes + x - 1)
		# x > (a2 * (strikeTimes - 1) - h1) / c1
		healTimes = int(math.ceil(float(a2 * strikeTimes - a2 - h1 + 0.001) / float(c1 - a2)))
		# if(a2 * (strikeTimes - 1) - h1 == 0):
		# 	healTimes+=1
		debug(healTimes, strikeTimes)

		for i in range(healTimes):
			steplist.append('HEAL')
		for i in range(strikeTimes):
			steplist.append('STRIKE')
		
		put(len(steplist))
		for step in steplist:
			put(step)

		pass

	def solve903c():
		n = ri()
		li = {}
		boxes = map(int, rl().split())
		for box in boxes:
			if(box in li):
				li[box] += 1
			else:
				li[box] = 1
		boxes.sort()
		boxes.reverse()
		debug(boxes)
		curnum = 0
		for box in boxes:
			if(li[box] > curnum):
				curnum += 1
				continue
		put(curnum)


		pass



		pass




	
	def solve893a():
		n = ri()
		arr = []
		cannot = 3
		for x in range(n):
			winner = ri()
			if(winner == cannot):
				put("NO")
				return
			nextcannot = 1
			while(nextcannot == cannot or nextcannot == winner):
				nextcannot+=1
			cannot = nextcannot
		put("YES")
	def solve893b():
		n,m = ri(), ri()
		vs = [0]
		fs = {}
		ans = 0
		for i in range(n):
			vs.append(ri())
		for i in range(m):
			f1,f2 = ri(), ri()
			if(f1 in fs):
				fs[f1].add(f2)
				fs[f2] = fs[f1]
			elif(f2 in fs):
				fs[f2].add(f1)
				fs[f1] = fs[f2]
			else:
				fs[f1] = set()
				fs[f1].add(f1)
				fs[f1].add(f2)
				fs[f2] = fs[f1]
		done = [False]*(n+1)
		for i in range(1, n+1):
			if(done[i]):continue
			if(i in fs):
				min = 1000000009
				for x in fs[i]:
					done[x] = True
					if(vs[x] < min):
						min = vs[x]
					pass
				ans+= min
			else:
				ans+= vs[i]
		put(ans)
	def solvePostfixNotation():
		n = ri()
		stack = []
		ans = 0
		for i in range(n):
			t = rs()
			debug(t)
			try:
				val = int(t)
				stack.append(val)
			except:
				op = str(t)
				val2 = stack.pop()
				val1 = stack.pop()
				if(op == '-'):
					stack.append(val1 - val2)
				if(op == '+'):
					stack.append(val1 + val2)
				if(op == '*'):
					stack.append(val1 * val2)

			i+=1
		put(stack.pop())
		pass
	def solveBracketSequence():
		n = ri()
		for t in range(n):
			stack = []
			line = rs()
			i = 0
			linelen = len(line)
			while(i < linelen):
				if(line[i] == '('):
					stack.append(line[i])
				elif(line[i] == '['):
					stack.append(line[i])
				else:
					try:
						v = stack.pop()
					except:
						put('NO')
						break
					if((line[i] == ')' and v == '(') or (line[i] == ']' and v == '[')):
						i+=1
						continue
					else:
						put('NO')
						break
				i+=1
			if(i == linelen):
				if(len(stack) > 0):
					put('NO')
					continue
				put('YES')
			pass
		pass
	class PoleStack(object):
		def __init__(this):
			this.data = []
			this.lastMin = sys.maxsize - 1
			this.lastMax = -sys.maxsize + 1

		def Push(this, value):
			if(value < this.lastMin):
				this.lastMin = value
			if(value > this.lastMax):
				this.lastMax = value
			this.data.append((value, this.lastMin, this.lastMax))

		def Pop(this):
			v = this.data.pop()
			#this.data = this.data[:-1]
			try:
				k = this.data[0]
				this.lastMin = k[1]
				this.lastMax = k[2]
			except:
				this.lastMin = sys.maxsize - 1
				this.lastMax = -sys.maxsize + 1
			return v
		def GetMin(this):
			if(not this.IsEmpty()):
				return this.data[-1][1]
			return None
		def GetMax(this):
			if(not this.IsEmpty()):
				return this.data[-1][2]
			return None
		def IsEmpty(this):
			try:
				k = this.data[0][0]
				if(k is not None):
					return False
			except:
				return True
			return False
			pass
	class PoleQueue(object):
		def __init__(this, **kwargs):
			this.inbox = PoleStack()
			this.outbox = PoleStack()
		
			return super().__init__(**kwargs)

		def Enqueue(this, value):
			this.inbox.Push(value)

		def Dequeue(this):
			if(this.outbox.IsEmpty()):
				while(True):
					try:
						this.outbox.Push(this.inbox.Pop()[0])
					except:
						break
					pass
				pass
			return this.outbox.Pop()

		def GetMin(this):
			inmin = sys.maxsize - 1 if this.inbox.IsEmpty() else this.inbox.GetMin()
			outmin = sys.maxsize - 1 if this.outbox.IsEmpty() else this.outbox.GetMin()
			return inmin if inmin < outmin else outmin
		def GetMax(this):
			inmax = -sys.maxsize + 1 if this.inbox.IsEmpty() else this.inbox.GetMax()
			outmax = -sys.maxsize + 1 if this.outbox.IsEmpty() else this.outbox.GetMax()
			return inmax if inmax > outmax else outmax
	def solveQueuewithMinimum():
	
		n = ri()
		dic = {}
		nums = PoleQueue()
		firstidx = 0
		lastidx = -1
		for i in range(n):
			op = rt()
			if(op == b'?'):
				put(nums.GetMin())

				continue
			if(op == b'-'):
				nums.Dequeue()
				#put(dic[firstidx])
				#nums.remove(innums[0])

				continue
		
			v = ri()
			if (op == b'+'):

				nums.Enqueue(v)
				#lastidx += 1
				#dic[lastidx] = int(line[1])
				pass
			pass

		pass
	def solveQueue():
	
		n = rl(int)[0]
		dic = {}
		firstidx = 0
		lastidx = -1
		for i in range(n):
			line = rl()
			if (line[0] == '+'):
				lastidx += 1
				dic[lastidx] = int(line[1])
				pass
			else:
				put(dic[firstidx])
				firstidx += 1
				pass
			pass

		pass
	def solveStack():
		n = rl(int)[0]
		dic = {}
		lastidx = -1
		for i in range(n):
			line = rl()
			if (line[0] == b'+'):
				lastidx += 1
				dic[lastidx] = int(line[1])
				#stack.append(iof.next_int())
				pass
			else:
				#iof.writeln(stack.pop())
				put(dic[lastidx])
				lastidx -= 1
				pass
			pass
		
		pass
	def solveAplusB():
		put(sum(rs(int)))
	def solveAplusB2():
		a,b = rs(int)
		put(sum([a, b * b]))
	def solveThreeBonacci():
		a = [0,0,0]
		a[0],a[1],a[2], n = rs(int)
		k = 3
		t = a[2] + a[1] - a[0]
		if(n <= 2):
			put(a[n])
			return
		if(n == 3):
			put(t)
			return
		a[2], a[1], a[0] = t, a[2], a[1]
		while(k < n):
			t = a[2] + a[1] - a[0]
			a[2], a[1], a[0] = t, a[2], a[1]
			k += 1
		put(t)

	def solve897a():
		n,m = ri(),ri()
		ins = list(rs())
		for i in range(m):
			l, r, c1, c2 = ri(), ri(), rs(), rs()
			for ci in range(l-1,r):
				if(ins[ci] == c1):
					ins[ci] = c2
		ans = (map(lambda x: str(x), ins))
		wl(''.join(ans))

	def solve897b():
		k, p = ri(), ri()
		# 2,4,6,8,10 10,0000,0000
		# 1,2,3,4,5
		# 9,81,...
		leadpick = [1,2,3,4,5,6,7,8,9]
		midpick = [0,1,2,3,4,5,6,7,8,9]
		li = []
		i = 1
		num = 1
		ans = 0
		while(i <= k):
			ans += (int(str(num) + str(num)[::-1]))
			ans %= p

			i+=1
			num += 1

		ans %= p
		wl(ans)

	def solve897c():
		ans = []
		q = ri()
		dtxt = "What are you doing at the end of the world? Are you busy? Will you save us?"
		alen = 34
		blen = 32
		clen = 2
		levelTable = {0:[0,75]}
		maxn = 0
		for i in range(1, 11):
			levelTable[i] = [levelTable[i-1][-1],
			alen + levelTable[i-1][-1] + blen + levelTable[i-1][-1] + clen]
		for i in range(q):
			n, k = ri(), ri() - 1
			if(n > maxn):
				maxn = n
			if(n == 0):
				if(k >= 75):
					ans.append('.')
				else:
					ans.append(dtxt[k])
				continue
			else:
				while(n > 0):
					found = False
					if(n == 1):
						if(k < 218):
							ans.append("What are you doing while sending \"What are you doing at the end of the world? Are you busy? Will you save us?\"? Are you busy? Will you send \"What are you doing at the end of the world? Are you busy? Will you save us?\"?"[k])
						else:
							ans.append('.')
						break
					if(0 <= k and k < alen):
						ans.append("What are you doing while sending \""[k])
						found = False
						break
					elif(alen <= k and k < alen + levelTable[n][0]):
						k -= levelTable[n][0] + alen
						found = True
						n-=1
					elif(levelTable[n][0] + alen <= k and k < levelTable[n][0] + alen + blen):
						ans.append("\"? Are you busy? Will you send \""[k])
						found = False
						break
					elif(levelTable[n][0] + alen + blen <= k and k < 2 * levelTable[n][0] + alen + blen):
						k -= 2 * levelTable[n][0] + alen + blen
						found = True
						n-=1
					elif(2 * levelTable[n][0] + alen + blen <= k and k < 2 * levelTable[n][0] + alen + blen + clen):
						ans.append("\"?")
						found = False
						break
					else:
						ans.append('.')
						break
					# elsif(not found):
					# 	break
					

		
		wl(''.join(ans))
#[Preprocess]#endif








#[Preprocess]#ifdef ArchiveEdX
if(ArchiveEdX):
	#####################################################################################
	#
	#					How to win coding competitions : secrets of champions
	# site = https://courses.edx.org/courses/course-v1:ITMOx+I2CPx+3T2017/course/
	#####################################################################################
	MOD = 10**9 + 7

	#def solveQAQ():
	#	a = rs()
	#	arr = []
	#	lena = len(a)
	#	i = 0
	#	j = 0
	#	while(i < lena):
	#		if()


	#	put(a)



	def solveRoyalGardenersandtheTaxInspection():


		pass

	def solveJohnsonJohnson():
		#TLE at 30
		n = ri()
		arr = []
		tmp = []
		a = [0] * (n)
		b = [0] * (n)

		aa = [0] * (n)
		bb = [0] * (n)
		for i in range(n):
			a[i] = ri()
		for i in range(n):
			b[i] = ri() 
		for i in range(n):
			if(b[i] >= a[i]):
				arr.append([i, a[i], b[i]])
			else:
				tmp.append([i, a[i], b[i]])
		arr = sorted(arr, key=lambda x:x[1])
		tmp = sorted(tmp, key=lambda x:x[2])
		tmp.reverse()
		arr = arr + tmp
		ans = []
		l = 0
		ans.append([arr[0][0] ,0, arr[0][1]])
		i = 1
		while(i < n):
		
			ans.append([arr[i][0],ans[i-1][1] + arr[i-1][1],0])
			ans[-1][2] = max(ans[i][1] + arr[i][1], ans[i - 1][2] + arr[i - 1][2])
			i+=1

		put(ans[i - 1][2] + arr[i-1][2])
		ans = sorted(ans, key=lambda x:x[0])
		i = 0
		tmp = ''
		for i in range(n):
			tmp += str(ans[i][1]) + ' '
		tmp += '\n'
		for i in range(n):
			tmp += str(ans[i][2]) + ' '
		put(tmp)
		pass
	def solveKthOrderedStatistic():
		n, k1, k2 = ri(),ri(),ri()
		a,b,c,a1,a2 = ri(),ri(),ri(),ri(),ri()

		k = 2
		arr = [a1,a2]
		while(k < n):
			tmp = a * arr[k - 2] + b * arr[k - 1] + c
			tmp = tmp & 0xffffffff
			#div = tmp // 2147483647
			#if((div) % 2 == 1):
			#	tmp = tmp - (div+1)*2147483648
			#else:
			#	tmp = tmp % 2147483647
			arr.append(tmp)
			k += 1


		pass


	#py3
	def solveAntiQuicksort():
		n = ri()
		if(n == 1):
			put('1')
			return
		arr = [1,2]
		AntiQuickSort(arr,n)
		put(ToSpaceSeperatedString(arr))
		pass

	def AntiQuickSort(arr,n):
		lastputidx = 1
		k = len(arr) + 1
		while(k < n + 1):
			#if(k % 2 == 0): #짝수일 경우 : 가운데 append
			#	lastputidx = (k)/2
			#	arr.insert(lastputidx, k)
			#	k+=1
			#else:#홀수일 경우 : 마지막 수의 위치에 넣고, 마지막 수는 끝에 append
			arr.append(arr[lastputidx])
			arr[lastputidx] = k
			lastputidx = int(k / 2)
			k+=1
		return arr
		pass

	def QuickSort(arr, l, r):
		debug(arr)
		key = arr[(l + r) // 2]
		i = l
		j = r
		debug('key ,i ,j = ' + str([key,i,j]))
		while i < j:
			while arr[i] < key:
				debug('inc i')
				i+=1
			while key < arr[j]:
				debug('dec i')
				j-=1
			if(i <= j):
				debug('swap i,j : ' + str(i) + ' ' + str(j))
				arr[i], arr[j] = arr[j], arr[i]
				i+=1
				j-=1
				pass
			pass
		if(l < j):
			debug('call qs, l, j =' + str([l,j]))
			QuickSort(arr, l, j)
		if(i < r):
			debug('call qs, i, r =' + str([i,r]))
			QuickSort(arr, i, r)
		pass


	def solveSavingLives():
		n = ri()
		arr = []
		for i in range(n):
			arr.append((ri(),ri()))

			pass
		arr.sort()
		w = ri()
		ans = 0
		for i in reversed(range(n)):
			if(w > arr[i][1]):
				dif = arr[i][1]
				ans += dif * arr[i][0]
				w -= dif
			else:
				dif = w
				ans += dif * arr[i][0]
				w = 0
		put(ans)



		pass

	def InsertionSort(arr, l, r):
		min = sys.maxsize
		pick = -1
		for i in range(l, r):
			min = sys.maxsize
			for j in range(i, r + 1):
				if(arr[j] < min):
					min = arr[j]
					pick = j
			arr[i], arr[j] = arr[j], arr[i]
		pass

	ans2 = 0
	def solveInversions():
		n = ri()
		arr = [0] * (n + 1)
		donebit = 0
		for i in range(1, n + 1):
			arr[i] = ri()
		put(mergeSort2(arr, 1, n))

	

	def mergeSort2(arr, l, r):
		ans = 0
		if(r - l == 0):
			return ans
		elif(r - l == 1):
			if(arr[l] > arr[r]):
				ans+=1
				arr[r], arr[l] = arr[l], arr[r]

			return ans
		#	pass

		m = int((l + r) / 2)
		if(m == l):
			m += 1
		ansa = mergeSort2(arr, l, m) 
		ansb = mergeSort2(arr, m + 1, r)
		tmp = [0]


		ap = l
	
		bp = m + 1
		countedb = 0
		while(ap <= m or bp <= r):
			a = arr[ap]
			b = arr[bp]
			if(a > b):
				tmp.append(b)
				bp+=1
				countedb+=1
			else:
				ans+=countedb
				tmp.append(a)
				ap+=1
			if(ap > m):
				while(bp <= r):
					b = arr[bp]
					tmp.append(b)
					bp+=1
			if(bp > r):
				while(ap <= m):
					ans+=countedb
					a = arr[ap]
					tmp.append(a)
					ap+=1
			pass

		for i, x in enumerate(tmp):
			if(i == 0):
				continue
			arr[i + l - 1] = x
		
		return ans + ansa + ansb

		#while pos < n:
		#	if(pos not in dic):
		#		pos += 1
		#		continue
		#	for j in dic[pos]: #각각의 숫자가 가진
		#		#j는 현재 숫자어레이의 각 숫자들, 각 pos,j에 대해 ans를 구하는 중이다.
		#		#그러려면 pos보다 작은 수들에 대해 순회하면서,
		#		#그 수의 배열순회하면서 인덱스와 수 모두 작아야 된다.
		#		#만약 계산된 ans가 인덱스 l, 수 k가 즉 ans[k][l] 있다면 curcount에 그 값을 더하고
		#		curcount = 0
		#		for k in range(1, pos - 1):
		#			l = 0
		#			if(dic[k][l] < pos and l < j):
		#				curcount+=1
		#				l+=1
				
		#			pass
		#		ans[pos][j] = curcount #계산해야 함

		#		pass
		#	pass

		pass
	def solveSorting():
		n = ri()
		arr = [0] * (n + 1)
		for i in range(1, n + 1):
			arr[i] = ri()

		mergeSort(arr, 1, n)
		put(' '.join(map(str,arr[1:])))


		pass

	def mergeSort(arr, l, r):
		if(r - l == 0):
			return
		elif(r - l == 1):
			if(arr[l] > arr[r]):
				arr[r], arr[l] = arr[l], arr[r]

			put(' '.join(map(str,[l,r] + [arr[l], arr[r]])))
			return
		#	pass

		m = int((l + r) / 2)
		if(m == l):
			m += 1

		mergeSort(arr, l, m) 
		mergeSort(arr, m + 1, r)
		tmp = [0]


		ap = l
	
		bp = m + 1
		while(ap <= m or bp <= r):
			a = arr[ap]
			b = arr[bp]
			if(a > b):
				tmp.append(b)
				bp+=1
			else:
				tmp.append(a)
				ap+=1
			if(ap > m):
				while(bp <= r):
					b = arr[bp]
					tmp.append(b)
					bp+=1
			if(bp > r):
				while(ap <= m):
					a = arr[ap]
					tmp.append(a)
					ap+=1
			pass

		for i, x in enumerate(tmp):
			if(i == 0):
				continue
			arr[i + l - 1] = x
		
		put(' '.join(map(str,[l,r] + [arr[l], arr[r]])))
		return

	def solveSnowmenSolution():
		n = ri()
		w = [0] * (n + 1)
		p = [0] * (n + 1)
		sumw = 0

		for i in range(1, n + 1):
			a = ri()
			b = ri()
			if b == 0:
				w[i] = w[p[a]]
				p[i] = p[p[a]]
			else:
				w[i] = w[a] + b
				p[i] = a
			sumw += w[i]

		put(sumw)

	def solveSnowmen():
		#position of q/ total mass
		dic = {0:(0,0)}
		stacks = [[]]
		maxs = [0]
		refs = [(0,0)]
		#stackidx / stacklastmasspointer / totalmass
		mens = [(0,0,0)]
		n = ri()
		sums = 0
		ls = []
		for i in range(n):
			assert(len(stacks) == len(refs))
			t = ri()
			m = ri()
			if(m > 0):
				#복사 후 눈 더하기
				if(maxs[mens[t][0]] == mens[t][1]):
					#눈사람 끝에 새로추가
					mens.append((mens[t][0],mens[t][1] + 1,mens[t][2] + m))
					stacks[mens[t][0]].append(m)
					maxs[mens[t][0]] += 1
					sums+=mens[-1][2]
					ls.append(mens[-1][2])

				elif(stacks[mens[t][0]][mens[t][1]] != m):
					#중간에추가하는데 질량다름
					if(t == 0):
						#아예새로만듬
						mens.append((len(stacks), 1, m))
						stacks.append([m])
						refs.append((len(stacks), 0))
						#stacks[mens[t][0]].append(m)
						l = len(stacks[-1])
						maxs.append(l)
						sums+=mens[-1][2]
						ls.append(mens[-1][2])
					else:
					#새로추가, 기존 있음, copy
					#copy하지 않으려면?  바뀐 부분부터만 가르키도록 변경!!
						idx = len(stacks)
						mens.append((idx, 1, mens[t][2] + m))
						stacks.append(stacks[mens[t][0]][:mens[t][1]][mens[t][1]:])
						if(mens[t][1] == 0):
							refs.append((idx,mens[t][1]))
						else:
							refs.append((mens[t][0],mens[t][1]))
						stacks[idx].append(m)
						l = len(stacks[-1])
						maxs.append(l)
						sums+=mens[-1][2]
						ls.append(mens[-1][2])

					pass
				else:
					#기존에 추가
					mens.append((mens[t][0], mens[t][1] + 1, mens[t][2] + m))
					sums+=mens[-1][2]
					ls.append(mens[-1][2])


					pass

				pass
			else:
				#눈빼기
				if(mens[t][1] - 1 == 0 and refs[mens[t][0]][0] != mens[t][0]):
					#더할 것은 (참조되는 스택, 참조되는 포인터, )
					#참조 눈스택으로 revert
					mens.append((refs[mens[t][0]][0], refs[mens[t][0]][1], mens[t][2] - stacks[mens[t][0]][mens[t][1] - 1]))
					sums+=mens[-1][2]
					ls.append(mens[-1][2])

					pass
				else:
					mens.append((mens[t][0], mens[t][1] - 1, mens[t][2] - stacks[mens[t][0]][mens[t][1] - 1]))
					sums+=mens[-1][2]
					ls.append(mens[-1][2])
				##눈빼기
				#if(mens[t][1] == 0):
				#	#참조 눈스택으로 revert
				#	mens.append((refs[mens[t][0]][0], refs[mens[t][0]][1] -1, mens[t][2] -
				#	stacks[refs[mens[t][0]][0]][refs[mens[t][0]][1] - 1]))
				#	sums+=mens[-1][2]
				#	ls.append(mens[-1][2])

				#	pass
				#else:
				#	mens.append((mens[t][0], mens[t][1] - 1, mens[t][2] -
				#	stacks[mens[t][0]][mens[t][1] - 1]))
				#	sums+=mens[-1][2]
				#	ls.append(mens[-1][2])



			pass
		put(sums)
		pass
#[Preprocess]#endif


#logging

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

reader = None
writer = None

#[Preprocess]#ifdef UseFileIO
ReadTarget = os.path.join(IO_Dir, InputFileName)
WriteTarget = os.path.join(IO_Dir, OutputFileName)
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
	#put = lambda x: logger1.log(100,x)
	#info = lambda x: logger1.log(logging.INFO,x)
	#critical = lambda x: logger1.log(logging.CRITICAL,x)
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
	except:
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
			print('psutil not installed. skipping memory log')
			pass
		pass
	logf.close()

	try:
		fileinput.close()
	except:
		pass

	# minifier.run()
	pass
#[Preprocess]#endif


