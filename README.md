# Python sport programming tools

## Description

Small python library that helps writing and debugging competetive
programming problem solutions.

Automates creating debugging/solution file.

Log memory usage with psutils

## Getting Started
Write your program on solve function of main.py and run main.py then
solution.py created. Debug, info, critical log level is for debug only
and solution.py prints only put log level.

### Dependencies
 - pypreprocessor > 0.75 
 (https://github.com/interpreters/pypreprocessor : Use `pip install git+https://github.com/interpreters/pypreprocessor.git`)
 - psutil (optional)

### Usage:
- input.txt :
```text
120
epi
```

- main.py :
```text
def solve():
val1 = ri()
str1 = rs()
debug(val1, str1)
put(str1 + str(val1))
```

After `python main.py` executed, debug version of main.py (debug.py)
created and executed, creating below output.txt file.

- output.txt (created by main.py) :
```text
DEBUG :Start------------------------
DEBUG :120 epi
PUT :epi120
DEBUG :End------------------------
DEBUG :running time : 0.0
```

And if you run `python solution.py`, it creates/overrides output.txt.

- output.txt (created by solution.py) :
```text
epi120
```
Also each time you run, run data is appended to log.txt
- log.txt :
```text
2018-02-05 13:57:47.043218 | Program started.
memory : 11657216
```
