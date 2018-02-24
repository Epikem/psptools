
#!/usr/bin/env python

# /*
#  * Copyright (c) 2018 Epikem
#  * edx_in and edx_out : Copyright (c) 2018 Maxim Buzdalov. Modified by Epikem
#  *
#  * Permission is hereby granted, free of charge, to any person obtaining a copy of
#  * this software and associated documentation files (the "Software"), to deal in
#  * the Software without restriction, including without limitation the rights to use,
#  * copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
#  * Software, and to permit persons to whom the Software is furnished to do so,
#  * subject to the following conditions:
#  *
#  * The above copyright notice and this permission notice shall be included in all
#  * copies or substantial portions of the Software.
#  *
#  * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#  * FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#  * COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
#  * AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
#  * THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# */

# NYAN NYAN
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

import io
import os
import time
from datetime import datetime

import mmap
import os
IO_Dir = '.'
InputFileName = 'input.txt'
OutputFileName = 'output.txt'
ReadTarget = os.path.join(IO_Dir, InputFileName)
WriteTarget = os.path.join(IO_Dir, OutputFileName)


def format(arg):
    if(PythonVersion < 3):
        if isinstance(arg, bytes):
            return arg
        elif isinstance(arg, str):
            return arg.encode()
        elif hasattr(arg, '__iter__'):
            return b' '.join(map(format, arg))
        else:
            return bytes(arg)
    else:
        if isinstance(arg, bytes):
            return arg.decode(WriteEncoding)
        elif isinstance(arg, str):
            return arg
        elif hasattr(arg, '__iter__'):
            return ' '.join(map(format, arg))
        else:
            return str(arg)
        pass

# Copyright (c) 2018 Maxim Buzdalov. Modified by Epikem


class edx_in:
    def __init__(self, target=None):
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
            self.mm = mmap.mmap(self.stream.fileno(), 0,
                                access=mmap.ACCESS_READ)
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

    def nextNToken(self, rep=0):

        ans = []
        while(rep > 0):
            ans.append(self.next_token())
            rep -= 1
        # TODO : Determine return value : iterator? or joined string? or array?
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
    def __init__(self, target=None):
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
        self.stream.write(format(arg))

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
            this.debug(b'test : ' + exp.encode(WriteEncoding) +
                       b' = ' + ans.encode(WriteEncoding))
        else:
            this.debug('test : ' + exp + ' = ' + ans)
        pass

# endregion Default IO Functions


sys.setrecursionlimit(100)

# region Helper Functions

import functools
from functools import wraps


def counted(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper




@counted
def it():
    put('it')
    pass



@counted
def useless():
    # put(useless)
    pass



@counted
def modmul():
    return 0


import collections
import functools


@counted
class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''

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



@counted
def ToSpaceSeperatedString(targetList):
    return " ".join(map(str, targetList))


import operator
import functools


@counted
def combination(n, r):
    r = min(r, n - r)
    if(r == 0):
        return 1
    if(r < 0):
        return 0

    numer = functools.reduce(operator.mul, range(n, n - r, -1))
    denom = functools.reduce(operator.mul, range(1, r + 1))
    return numer // denom



@counted
def sumdigit(num):
    num = str(num)
    r = 0
    for x in num:
        r = r + int(x)
        pass

    return r



@counted
def digitListToInt(numList):
    return int(''.join(map(str, numList)))



@counted
def listByDigit(digitLen):
    return [0 for _ in range(digitLen)]



@counted
def Fibonacci(n, k):
    ans = 0
    for x in range(1, n):
        ans = ans + x * C(n - x, k - 1)

        pass
    return ans
    pass



@counted
def keyOfMaxValue(d1):
    '''
    O(n)
    '''
    v = list(d1.values())
    return list(d1.keys())[v.index(max(v))]



@counted
def checkProperIrreducible(a, b):
    if(a == 1):
        return True
    if(a == b):
        return False
    if(a > b):
        return checkProperIrreducible(b, a)
    else:
        return checkProperIrreducible(a, b - a)



@counted
class MultiArray(object):

    def MultiArray(defaultList, listCount):
        this.Lists[0] = defaultList
        for i in range(1, listCount):
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



@counted
def longDivisionDigits(dividend, divisor):
    d = dividend
    while True:
        yield d // divisor
        d = d % divisor * 10


# endregion

def solve():
    debug('Test')
    pass

# logging




def gettime():
    return str(datetime.now())


def memory():
    pass


logf = io.open(os.path.join(IO_Dir, "log.txt"), "a", encoding=LogEncoding)

if(PythonVersion < 3):
    content = (gettime() + " | Program started.\n").encode(encoding=LogEncoding)
    logf.write(unicode(content))
else:
    content = (gettime() + " | Program started.\n")
    logf.write(content)


def log(str1):
    if(PythonVersion < 3):
        print(unicode(str1), file=logf)
    else:
        print(str1, file=logf)
    pass


pass
try:
    logger1 = logging.getLogger('log1')
    debug = lambda *x: logger1.log(logging.DEBUG, format(x))

    PutLevel = 100
    logging.PUT = PutLevel
    logging.addLevelName(PutLevel, 'PUT')
    logger1.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)-8s:%(message)s')
    debugHandler = logging.StreamHandler(sys.stdout)
    debugHandler.setFormatter(formatter)
    logger1.addHandler(debugHandler)
except:
    pass

#WriteTarget = None
with edx_in(ReadTarget) as Reader, edx_out(WriteTarget) as Writer:

    try:
        if(Writer.stream == sys.stdout):
            logger1.removeHandler(debugHandler)
        outHandler = logging.StreamHandler(Writer.stream)
        outHandler.setFormatter(formatter)
        logger1.addHandler(outHandler)
        if(PythonVersion >= 3):
            put = lambda *args: logger1.log(logging.PUT, format(args))
            info = lambda *args: logger1.log(logging.INFO, format(args))
            critical = lambda *args: logger1.log(
                logging.CRITICAL, format(args))
        else:
            put = lambda *args: logger1.log(logging.PUT, format(args))
            info = lambda *args: logger1.log(logging.INFO, format(args))
            critical = lambda *args: logger1.log(
                logging.CRITICAL, format(args))
    except ModuleNotFoundError:  # judge does not have logging module.
        debug = Writer.writeln
        put = Writer.writeln
        info = Writer.writeln
        critical = Writer.writeln
    debug("Start------------------------")
    duration = time.time()
    pass

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
    debug("End------------------------")
    duration = time.time() - duration
    debug("running time : " + str(duration))
    if(PythonVersion >= 3):
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
