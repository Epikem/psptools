# -*- coding:utf-8 -*-
from sniffer.api import * # import the really small API
import os, termstyle

# you can customize the pass/fail colors like this
pass_fg_color = termstyle.green
pass_bg_color = termstyle.bg_default
fail_fg_color = termstyle.red
fail_bg_color = termstyle.bg_default

# All lists in this variable will be under surveillance for changes.
watch_paths = ['..']

# this gets invoked on every file that gets changed in the directory. Return
# True to invoke any runnable functions, False otherwise.
#
# This fires runnables only if files ending with .py extension and not prefixed
# with a period.
@file_validator
def py_files(filename):
    return (filename.endswith('.py') or filename.endswith('.txt')) and not os.path.basename(filename).startswith('.')

# @file_validator
# def txt_files(filename):
#     return filename.endswith('.txt') and not os.path.basename(filename).startswith('.')

# This gets invoked for verification. This is ideal for running tests of some sort.
# For anything you want to get constantly reloaded, do an import in the function.
#
# sys.argv[0] and any arguments passed via -x prefix will be sent to this function as
# it's arguments. The function should return logically True if the validation passed
# and logicially False if it fails.
#
# This example simply runs nose.

#          foreground background
# black        30         40
# red          31         41
# green        32         42
# yellow       33         43
# blue         34         44
# magenta      35         45
# cyan         36         46
# white        37         47
# Additionally, you can use these:

# reset             0  (everything back to normal)
# bold/bright       1  (often a brighter shade of the same colour)
# underline         4
# inverse           7  (swap foreground and background colours)
# bold/bright off  21
# underline off    24
# inverse off      27

def BLACK_TEXT(x): return "\033[30;1m" + x + "\033[0m"
def RED_TEXT(x): return "\033[31;1m" + x + "\033[0m"
def GREEN_TEXT(x): return "\033[32;1m" + x + "\033[0m"
def YELLOW_TEXT(x): return "\033[33;1m" + x + "\033[0m"
def BLUE_TEXT(x): return "\033[34;1m" + x + "\033[0m"
def MAGENTA_TEXT(x): return "\033[35;1m" + x + "\033[0m"
def CYAN_TEXT(x): return "\033[36;1m" + x + "\033[0m"
def WHITE_TEXT(x): return "\033[37;1m" + x + "\033[0m"
def BOLD_BLACK_TEXT(x): return "\033[1m\033[30m;1m" + x + "\033[0m"
def BOLD_RED_TEXT(x): return "\033[1m\033[31m;1m" + x + "\033[0m"
def BOLD_GREEN_TEXT(x): return "\033[1m\033[32m;1m" + x + "\033[0m"
def BOLD_YELLOW_TEXT(x): return "\033[1m\033[33m;1m" + x + "\033[0m"
def BOLD_BLUE_TEXT(x): return "\033[1m\033[34m;1m" + x + "\033[0m"
def BOLD_MAGENTA_TEXT(x): return "\033[1m\033[35m;1m" + x + "\033[0m"
def BOLD_CYAN_TEXT(x): return "\033[1m\033[36m;1m" + x + "\033[0m"
def BOLD_WHITE_TEXT(x): return "\033[1m\033[37m;1m" + x + "\033[0m"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

@runnable
def execute_nose(*args):
    template = '######################################################################'
    templateColor = '\033[36;46;1m######################################################################\033[0m'

    # print(bcolors.OKBLUE + "testtext dddssdsd" + bcolors.ENDC)d
    print(templateColor)
    print('')
    print('\033[33mTest Start\033[0m'.center(len(template)))
    # print('{:^80}'.format('Test Start'))ddds
    print('')
    print(templateColor)
    import nose
    return nose.run(argv= list(args) + ["--verbosity=2"])
