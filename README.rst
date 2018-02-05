# psptools

## Description

Small python library that helps writing and debugging competetive programming problem solutions.

## Getting Started

Write your program on solve function of main.py and run main.py then solution.py created. Debug, info, critical log level is for debug only and solution.py prints only put log level.


Usage:
-- input.txt --
120
epi

-- main.py --
def solve():
	val1 = ri()
	str1 = rs()
	debug(val1, str1)
	put(str1 + str(val1))

After run 'python main.py', debug version of main.py (debug.py) created and executed, creating below output.txt file.

-- output.txt (created by main.py) --
DEBUG   :Start------------------------
DEBUG   :120 epi
PUT     :epi120
DEBUG   :End------------------------
DEBUG   :running time : 0.0

And if you run 'python solution.py', it creates/overrides output.txt.

-- output.txt (created by solution.py) --
epi120

Also each time you run, run data is appended to log.txt

-- log.txt --
2018-02-05 13:57:47.043218 | Program started.
memory : 11657216

