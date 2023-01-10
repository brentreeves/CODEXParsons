from importlib import import_module
import os
import inspect
import sys
import glob
import json
import inspect

# Brent Reeves
# Winter '22
#
class Marsons():
    me = ''             # Ericson2017figure1, i.e. subfolder name and problem name
    m = None            # holds imported module (i.e codex solution)
    mfname = 'yo'         # name of function in the solution, e.g. 'getSum'
    mf = None           # function definition
    folder = ''
    ff = []
    solutions = ""      # ~20 solution files
    predicates = None   # 'shoulda orta'
    failedtests = None  # dictionary of failed tests
    failcount = 0
    successcount = 0    # how many problems passed
    dafile = ''         # the current codex being tested

    fails = None
    wins = None
    loglevel = 0


    def __init__(self, figurename, functionname):
        self.me = figurename
        self.mfname = functionname

    def go(self, folder, dbg=0):
        print(f'   go folder: {folder}, dbg: {dbg}')


if __name__ == '__main__':
    # print( p.pp(sys.argv[1], int(sys.argv[2])) )
    print( "MMM..." )

