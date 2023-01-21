from importlib import import_module
from pathlib import Path
import os
import inspect
import sys
import glob
import json

# Brent Reeves
# Winter '22
#

class Parsons():
    me = ''             # Ericson2017figure1, i.e. subfolder name and problem
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
    dabasename = ''
    xref = []           # problem name and function to call

    fails = None
    wins = None
    results = None
    loglevel = 0

    # will no longer get figure and function
    # instead, keep xref array
    #
    def __init__(self):
        # self.me = figurename
        # self.mfname = functionname
        self.setXref()
        self.fails = []
        self.wins = []


    def setUpFolder(self, folder):
        self.fails = []
        self.wins = []
        self.folder = folder
        self.ff = None
        dastring = f'{self.folder}/{self.me}/{self.me}*.py'
        self.log(1, f'setUpFolder globs b4: {self.ff}  glob: {dastring}')
        self.ff = glob.glob(dastring)
        self.log(1, f'setUpFolder globs affa: {self.ff}  glob: {dastring}')

        # print(f'setUpClass globs: affa: {str(self.ff)}  glob: {dastring}')


    def errortype(self, key):
        msgs = {'output': 'output incorrect',
                'runtime': 'runtime error',
                'import': 'import error'}
        if not key in msgs:
            self.logerr(1, f'ERROR - invalid error code: {key}')
            # print( f'ERROR - invalid error code: {key}')
            return 'unknown error'
        else:
            return msgs[key]

      
    def Parson_Ericson2017figure1(self):
        return self.set_predicates_return([
            ("[] = 0", self.mf([]), 0),
            ("[0] = 0", self.mf([0]), 0),
            ("[0,0,0] = 0", self.mf([0,0,0]), 0 ),
            ("[-1] = -1", self.mf([-1]), -1 ),
            ("[1,0,-1,-1] = -1 ", self.mf([1, 0, -1, -1]), -1 ),
            ("[1,2,3,4] = 10 ", self.mf([1, 2, 3, 4]), 10),
            ("[-99,1,1,1,1,1] = 94 ", self.mf([-99, 1, 1, 1, 1, 1]), -94),
        ])

    def Parson_Ericson2017figure4(self):
        return self.set_predicates_return([
            ( "[1],0,0 = 1.0 == ", self.mf([1],0,0), 1.0),
            ( "[1,1],0,0 = 1.0 == ", self.mf([1,1],0,0), 1.0),
            ( "[1,1,1],0,0 = 1.0 == ", self.mf([1,1,1],0,0), 1.0),
            ( "[1,1,1,1],0,0 = 1.0 == ", self.mf([1,1,1,1],0,0), 1.0),

            ( "[1,1],0,1 = 1.0 == ", self.mf([1,1],0,1), 1.0),
            ( "[1,1,1],0,2 = 1.0 == ", self.mf([1,1,1],0,2), 1.0),
            ( "[1,1,1,1],0,3 = 1.0 == ", self.mf([1,1,1,1],0,3), 1.0),

            ( "[1,3],0,1 = 2.0 == ", self.mf([1,3],0,1), 2.0),
            ( "[1,4,1],0,2 = 2.0 == ", self.mf([1,4,1],0,2), 2.0),
            ( "[1,2,3,4],0,3 = 2.5 == ", self.mf([1,2,3,4],0,3), 2.5),
            ( "[1,2,3,4,5],0,2 = 2 == ", self.mf([1,2,3,4,5],0,2), 2.0),
            ( "[1,2,3,4,5],2,4 = 3 == ", self.mf([1,2,3,4,5],2,4), 4.0),
            
            ( "[1],0,0 = 1.0 == ", self.mf([1],0,0), 1.0),
            ( "[2],0,0 = 2.0 == ", self.mf([2],0,0), 2.0)
        ])

    
    def Parson_Ericson2018figure5(self):
        return self.set_predicates_return([
            # ("([1],0,0) = T", self.mf( [1],0,0 ), False),
            ("([1],0,0) = T", self.mf( [1],0,0 ), True),
            ("([1,1,1],0,0) =T", self.mf( [1,1,1],0,0)  , True),
            ("([1,1,99],0,0) =T", self.mf( [1,1,99],0,0)  , True),
            ("([1,1,1],0,1) =T", self.mf([1,1,1],0,1) , True),
            ("([1,1,99],0,1) =T", self.mf([1,1,99],0,1) , True),
            ("([1,1,99],0,2) =F", self.mf([1,1,99],0,2) , False),
            ("([1,1,9],0,2) =T", self.mf([1,1,9],0,2) , True),
            ("([1,1,1,9],0,2) =T", self.mf([1,1,1,9],0,2) , True),
            ("([1,1,1,1,9],0,2) =T", self.mf([1,1,1,1,9],0,2) , True),
            ("([1,1,1,1,9],0,3) =T", self.mf([1,1,1,1,9],0,3) , True),
            ("([1,1,1,1,9],0,4) =T", self.mf([1,1,1,1,9],0,4) , True),
            ("([1,1,1,1,10],0,4) =T", self.mf([1,1,1,1,10],0,4) , True),
            ("([1,1,1,1,11],0,4) =T", self.mf([1,1,1,1,11],0,4) , True),
            ("([1,1,1,1,12],0,4) =F", self.mf([1,1,1,1,12],0,4) , False),
            ("([1,1,1,1,-9],0,4) =T", self.mf([1,1,1,1,-9],0,4) , True),
            ("([1,1,1,1,-10],0,4) =F", self.mf([1,1,1,1,-10],0,4) , False),
            ("([0,3,6,9,12,15,18,21,24,27],0,1) :", self.mf([0,3,6,9,12,15,18,21,24,27],0,1) , True),
            ("([0,3,6,9,12,15,18,21,24,27],0,2) :", self.mf([0,3,6,9,12,15,18,21,24,27],0,2) , True),
            ("([0,3,6,9,12,15,18,21,24,27],0,3) :", self.mf([0,3,6,9,12,15,18,21,24,27],0,3) , True),
            ("([0,3,6,9,12,15,18,21,24,27],0,4) :", self.mf([0,3,6,9,12,15,18,21,24,27],0,4) , False),
            ("([0,3,6,9,12,15,18,21,24,27],1,5) :", self.mf([0,3,6,9,12,15,18,21,24,27],1,5) , False),
            ("([0,3,6,9,12,15,18,21,24,27],2.6) :", self.mf([0,3,6,9,12,15,18,21,24,27],2,6) , False),
            ("([0,3,6,9,12,15,18,21,24,27],2.6) :", self.mf([0,3,6,9,12,15,18,21,24,27],3,7) , False),
            ("([0,3,6,9,12,15,18,21,24,27],0,5) :", self.mf([0,3,6,9,12,15,18,21,24,27],0,5) , False),
        ])        


    def Parson_Ericson2022figure2(self):
        return self.set_predicates_return([
            # ( "(0,0) :", self.mf( 0,0 ) , 'too low', ), # blink test
            ( "(0,0) :", self.mf( 0,0 ) , 'correct', ),
            ( "(-1,-1) :", self.mf( -1,-1 ) , 'correct', ),
            ( "(-2,-2) :", self.mf( -2,-2 ) , 'correct', ),
            ( "(1,1) :", self.mf( 1,1 ) , 'correct', ),
            ( "(2,2) :", self.mf( 2,2 ) , 'correct', ),
            ( "(0,1) :", self.mf( 0,1 ) , 'too low', ),
            ( "(0.0,1.0) :", self.mf( 0.0,1.0 ) , 'too low', ),
            ( "(0,2) :", self.mf( 0,2 ) , 'too low', ),
            ( "(0,999) :", self.mf( 0,999 ) , 'too low', ),
            ( "(-1,0) :", self.mf( -1,0) , 'too low', ),
            ( "(-2,-1) :", self.mf( -2,-1 ) , 'too low', ),
            ( "(1,0) :", self.mf( 1,0 ) , 'too high', ),
            ( "(2,0) :", self.mf( 2,0 ) , 'too high', ),
            ( "(999,0) :", self.mf( 999,0 ) , 'too high', ),
            ( "(0,-1) :", self.mf( 0,-1) , 'too high', ),
            ( "(-1,-2) :", self.mf( -1,-2 ) , 'too high', ),
        ])

    
    #     def entry(self, bug, note, actual, expected, errortype):
    def Parson_Ericson2022figure3(self):
        def classy(jive):
            note, first, last, true_name, true_initials = jive
            # print('\nclassy: ', jive)
            daname = ''
            initials=''
        
            try:
                p1 = self.m.Person(first, last)
                errortype = ''
            
                initials = ''
                try:
                    initials = p1.initials()
                except:
                    self.logerr(2, "ERROR initials()")
                    actual = str(sys.exc_info()[1])
                    return self.keep_sad(
                                  "Error initials() not happy",
                                  actual,
                                  "initials method",
                                  self.errortype('runtime'))

                if (initials != true_initials):
                    return self.keep_sad(
                                  note,
                                  initials,
                                  true_initials,
                                  self.errortype('output'))

                daname = ''
                try:
                    daname = str(p1)
                except:
                    self.logerr(2, "ERROR __str__()")
                    return self.keep_sad(
                                      "Error __str__ not happy",
                                      str(sys.exc_info()[1]),
                                      "def __str__(self): return should be defined",
                                      self.errortype('runtime'))

                if (daname != true_name):
                    return self.keep_sad(
                                  note,
                                  daname,
                                  true_name,
                                  self.errortype('output'))
                self.log(2, f'class returning happiness {note} name {daname}')
                return self.keep_happy(note, daname, '')
            except:
                # print("safely caught exception")
                ff = f'ERROR: File: {self.dafile}'
                ee = {"error" : ff, "exception" : str(sys.exc_info()[1])}
                self.logerr(2, ee)

                return self.keep_sad(
                                  note,
                                  "Could not make a Person",
                                  "class Person:...",
                                  self.errortype('runtime'))
            # end classy
        args = [
            # ("a b = 'ab' 'a b'", 'a','b','a b', 'zz'), # blink test
            ("a b = 'ab' 'a b'", 'a','b','a b', 'ab'),
            ("aa bb = 'ab'",'aa','bb','aa bb', 'ab'),
            ("aaa bbb = ab", 'aaa','bbb','aaa bbb', 'ab'),
            ("' spacea',' spaceb' = [  ] ", ' spacea',' spaceb',' spacea  spaceb', '  '),
            ("' spacesa ',' spacesb ' = ...", ' spacesa ',' spacesb ',' spacesa   spacesb ', '  '),
            ("'a z','b z' = ab", 'a z','b z','a z b z', 'ab'),
        ]
        self.predicates = list(map ( classy, args ))

        bad = list(filter(lambda x:  x["bug"] == True, self.predicates ))
        good = list(filter(lambda x:  x["bug"] == False, self.predicates ))

        return len(bad), good, bad


    def Parson_Ericson2022figure4(self):
        return self.set_predicates_return([
            ( "(0,True) :", self.mf( 0,True ), 'off'),
            ( "(1,True) :", self.mf( 1,True ), '10:00'),
            ( "(2,True) :", self.mf( 2,True ), '10:00'),
            ( "(3,True) :", self.mf( 3,True ), '10:00'),
            ( "(4,True) :", self.mf( 4,True ), '10:00'),
            ( "(5,True) :", self.mf( 5,True ), '10:00'),
            ( "(6,True) :", self.mf( 6,True ), 'off'),
            ( "(0,False) :", self.mf( 0,False ), '10:00'),
            ( "(1,False) :", self.mf( 1,False ), '7:00'),
            ( "(2,False) :", self.mf( 2,False ), '7:00'),
            ( "(3,False) :", self.mf( 3,False ), '7:00'),
            ( "(4,False) :", self.mf( 4,False ), '7:00'),
            ( "(5,False) :", self.mf( 5,False ), '7:00'),
            ( "(6,False) :", self.mf( 6,False ), '10:00'),
        ])


    #
    # maybe upgrade to passing a function ?
    #
    def Parson_Ericson2022figure8(self):
        self.predicates = [
            # self.expectN("[] = 0", self.mf, [], -1), # blink test
            self.expectN("[] = 0", self.mf, [], 0),
            self.expectN("[0,0] = 0.0", self.mf, [0,0], 0),
            self.expectN("[0,0,0] = 0.0", self.mf, [0,0,0], 0),
            self.expectN("[0,0,0,-1] = 0.0", self.mf, [0,0,0,-1], 0),
            self.expectN("[0,0,0,-3] = 0.0", self.mf, [0,0,0,-3], 0),
            self.expectN("[1,1,1,0] = 1.0", self.mf, [1,1,1,0], 1),
            self.expectN("[1,1,0,1] = 1.0", self.mf, [1,1,0,1], 1),
            self.expectN("[1,0,1,1] = 1.0", self.mf, [1,0,1,1], 1),
            self.expectN("[0,1,1,1] = 1.0", self.mf, [0,1,1,1], 1),
            
            self.expectN("[-9,-1,-3,-5] = -3", self.mf, [-9,-1,-3,-5], -3),
            self.expectN("[-1,-9,-3,-5] = -3", self.mf, [-1,-9,-3,-5], -3),
            self.expectN("[-1,-3,-9,-5] = -3", self.mf, [-1,-3,-9,-5], -3),
            self.expectN("[-1,-3,-5,-9] = -3", self.mf, [-1,-3,-5,-9], -3),
            
            self.expectN("[0,2,2,2] = 2", self.mf, [0,2,2,2], 2),
            self.expectN("[0,1,3,5] = 3", self.mf, [0,1,3,5], 3) 
         ]

        good = list(filter(lambda x:  x["bug"] == False, self.predicates ))
        bad = list(filter(lambda x:  x["bug"] == True, self.predicates ))

        return len(bad), good, bad


    def Parson_Haynes_Magyar2022figure2(self):
        return self.set_predicates_return([
            # ( " [1] = False", self.mf([1]), True), # blink test
            ( " [1] = False", self.mf([1]), False),
            ( " [1,1] = False", self.mf([1,1]), False),
            ( " [1,1,1] = False", self.mf([1,1,1]), False),
            ( " [1,2,3,4] = False", self.mf([1,2,3,4]), False),
            ( " [1,2,1,2,1,2,1] = False", self.mf([1,2,1,2,1,2,1]), False),
            ( " [1,2,2,1,2,1] = True", self.mf([1,2,2,1,2,1]), True),
            ( " [2,2] = True", self.mf([2,2]), True),
            ( " [1,2,1,2,1,2,2] = True", self.mf([1,2,1,2,1,2,2]), True),
        ])


    def Parson_Haynes_Magyar2022figure4(self):
        return self.set_predicates_return([
            # ( '0,0,0,[0]=1', self.mf( 0,0,0,[0] ), 9), # blink test
            ( '0,0,0,[0]=1', self.mf( 0,0,0,[0] ), 1),
            ( '1,0,0,[0]=0', self.mf( 1,0,0,[0] ), 0),
            ( '0,0,1,[0,0]=2', self.mf( 0,0,1,[0,0] ), 2),
            ( '0,0,1,[0,0,0]=2', self.mf( 0,0,1,[0,0,0] ), 2),
            ( '0,0,1,[0,0,0,0]=2', self.mf( 0,0,1,[0,0,0,0] ), 2),
            ( '0,0,2,[0,0,0,0]=3', self.mf( 0,0,2,[0,0,0,0] ), 3),
            ( '0,0,3,[0,0,0,0]=4', self.mf( 0,0,3,[0,0,0,0] ), 4),
            ( '3,0,3,[1,2,3,1,2,3,1,2,3]=1', self.mf( 3,0,3,[1,2,3,1,2,3,1,2,3] ), 1),
            ( '3,0,6,[1,2,3,1,2,3,1,2,3]=2', self.mf( 3,0,6,[1,2,3,1,2,3,1,2,3] ), 2),
            ( '3,0,7,[1,2,3,1,2,3,1,2,3]=2', self.mf( 3,0,7,[1,2,3,1,2,3,1,2,3] ), 2),
            ( '3,0,8,[1,2,3,1,2,3,1,2,3]=3', self.mf( 3,0,8,[1,2,3,1,2,3,1,2,3] ), 3),
            ( '2,0,8,[1,2,3,1,2,3,1,2,3]=3', self.mf( 2,0,8,[1,2,3,1,2,3,1,2,3] ), 3),
            ( '1,0,8,[1,2,3,1,2,3,1,2,3]=3', self.mf( 1,0,8,[1,2,3,1,2,3,1,2,3] ), 3),
            ( '9,0,0,[9,9,9,9,9,9,9,9,9]=1', self.mf( 9,0,0,[9,9,9,9,9,9,9,9,9] ), 1),
            ( '9,0,1,[9,9,9,9,9,9,9,9,9]=2', self.mf( 9,0,1,[9,9,9,9,9,9,9,9,9] ), 2),
            ( '9,0,2,[9,9,9,9,9,9,9,9,9]=3', self.mf( 9,0,2,[9,9,9,9,9,9,9,9,9] ), 3),
            ( '9,0,3,[9,9,9,9,9,9,9,9,9]=4', self.mf( 9,0,3,[9,9,9,9,9,9,9,9,9] ), 4),
            ( '9,0,8,[9,9,9,9,9,9,9,9,9]=9', self.mf( 9,0,8,[9,9,9,9,9,9,9,9,9] ), 9),
            ( '9,8,8,[9,9,9,9,9,9,9,9,9]=1', self.mf( 9,8,8,[9,9,9,9,9,9,9,9,9] ), 1),
            ( '9,7,8,[9,9,9,9,9,9,9,9,9]=2', self.mf( 9,7,8,[9,9,9,9,9,9,9,9,9] ), 2),
            ( '9,4,5,[9,9,9,9,9,9,9,9,9]=2', self.mf( 9,4,5,[9,9,9,9,9,9,9,9,9] ), 2),
        ])

    def Parson_Hou2022figure2(self):
        return self.set_predicates_return([
            # ( "[] = []", self.mf([]), ['a'] ), # blink test
            ( "[] = []", self.mf([]), [] ),
	    ( "[''] = [] ", self.mf(['']), []),
            ( "['a'] = [] ", self.mf(['a']), []),
            ( "['a', 'b'] = [] ", self.mf(['a', 'b']), []),
            ( "['aaa'] = [] ", self.mf(['aaa']), []),
            ( "['aaaa'] = ['aaaa'] ", self.mf(['aaaa']), ['aaaa']),
            ( "['aaaa', ''] = ['aaaa'] ",  self.mf(['aaaa', '']), ['aaaa']),
            ( "['aaaa', 'b'] = ['aaaa'] ",  self.mf(['aaaa', 'b']), ['aaaa']),
            ( "['aaaa', 'bbbb'] = ['aaaa', 'bbbb'] ", self.mf(['aaaa', 'bbbb']), ['aaaa', 'bbbb']),
            ( "['1','12','123','1234','12345','123456'] = ['1234','12345','123456'] ", self.mf(['1','12','123','1234','12345','123456']), ['1234','12345','123456']),
            ( "['123456','12345','1234','123','12','1'] = ['123456','12345','1234'] ", self.mf(['123456','12345','1234','123','12','1']), ['123456','12345','1234']),
        ])


# write a function getSum(numList) that returns the sum of a list of numbers.
# def getSum(numList):
# vs
# construct a function that finds the maximum value in a given list
# def findmax(alist):
        # return self.set_predicates_return([
        #     ("[] = 0", self.mf([]), 0),
        #     ("[0] = 0", self.mf([0]), 0),


# import trying: Ericson2017figure1_1 whole: ../data/V/V1/Ericson2017figure1/Ericson2017figure1_1.py
# import happy : Ericson2017figure1_1
# source code: def getSum(numList):
#     sum = 0
#     for num in numList:
#         sum = sum + num
#     return sum
# attribute function happy getSum
# testFolderProblemFile calling testit
# testit start: Ericson2017figure1
#         testit start: Ericson2017figure1
# testit: fname: getSum  fn: <bound method Parsons.Parson_Ericson2017figure1 of <MM.Parsons object at 0x116079d20>>


# testit start: Karavirta2012Figure3

# testit: fname: findmax  fn: <bound method Parsons.Parson_Karavirta2012Figure3 of <MM.Parsons object at 0x102755d20>>
# {'error': 'ERROR: error running File: ../data/V/V1/Karavirta2012Figure3/Karavirta2012Figure3_1.py',
# 'exception': 'Parsons.Parson_Karavirta2012Figure3() takes 0 positional arguments but 1 was given'}
#    runtime issue {'folder': '../data/V/V1', 'figure': 'Karavirta2012Figure3', 'file': 'Karavirta2012Figure3_1.py',
# 'fullfile': '../data/V/V1/Karavirta2012Figure3/Karavirta2012Figure3_1.py', 'bug': 1,
# 'msg': 'error running ../data/V/V1/Karavirta2012Figure3/Karavirta2012Figure3_1.py',
# 'actual': 'Parsons.Parson_Karavirta2012Figure3() takes 0 positional arguments but 1 was given', 'expected': 'should run', 'errortype': self.errortype('runtime')}
# success removing module: Karavirta2012Figure3_1
# testfile returns fails: 1 wins: 0

    def Parson_Karavirta2012Figure3(self):
        return self.set_predicates_return([
            # ( "[]", self.mf([]), 999999), # blink test
            ( "[-9]", self.mf([-9]), -9),
            ( "[-9,-8]", self.mf([-9,-8]), -8),
            ( "[-9,-8,-10]", self.mf([-9,-8,-10]), -8),
            ( "[1,2,3]", self.mf([1,2,3]), 3),
            ( "[3,2,1]", self.mf([3,2,1]), 3),
            ( "[-9,-8,-7,3,2,1]", self.mf([-9,-8,-7,3,2,1]), 3),
            ( "[1,1,1,1,1,1,1]", self.mf([1,1,1,1,1,1,1]), 1),
            ( "[2,1,1,1,1,1,1]", self.mf([2,1,1,1,1,1,1]), 2),
            ( "[1,1,1,1,1,1,2]", self.mf([1,1,1,1,1,1,2]), 2),
            ( "[1,1,1,2,1,1,1]", self.mf([1,1,1,2,1,1,1]), 2),
        ])


    def stringOrFunction(self, jive):
        # print("stringOrFunction: ", jive, file=sys.stderr)
        note, f, arg1, arg2, expect = jive
        v1 = None
        v2 = None
        try:
            v1 = f(arg1)
            self.log(2, f'stringOrFunction worked: {str(v1)}')
            v2 = None
            if (callable(v1)):
                try:
                    v2 = v1(arg2)
                    happy = v2 == expect
                    return self.keep(not happy, note, v2, expect, self.errortype('output'))
                except:
                    ff = f'ERROR: Weinmann2021figure1 stringOrFunction 1  Folder: {self.folder} File: {self.dafile}\nNote: {note} arg1: {arg1} arg2: {arg2}'
                    ee = {"error" : ff, "exception" : str(sys.exc_info()[1])}
                    self.logerr(2, ee)
                    return self.keep_sad(note, str(sys.exc_info()[1]), expect, self.errortype('runtime'))
            else:
                if (type(v1) is str):
                    happy = v1 == expect
                    return self.keep(not happy, note, v1, expect, self.errortype('output'))
                
                return self.keep_sad(note, v1, expect, self.errortype('output'))
            
        except:
            ff = f'ERROR: Weinmann2021figure1 stringOrFunction 2  Folder: {self.folder} File: {self.dafile}\nNote: {note} arg1: {arg1} arg2: {arg2}'
            ee = {"error" : ff, "exception" : str(sys.exc_info()[1])}
            self.logerr(2, ee)
            return self.keep_sad(note, v1, expect, self.errortype('runtime'))

    def Parson_Weinmann2021figure1(self):
        def stringOrFunctionOld(self, jive):
            # print("stringOrFunction: ", jive, file=sys.stderr)
            note, f, arg1, arg2, expect = jive
            v1 = None
            v2 = None
            try:
                v1 = f(arg1)
                self.log(2, f'stringOrFunction worked: {str(v1)}')
                v2 = None
                if (callable(v1)):
                    try:
                        v2 = v1(arg2)
                        happy = v2 == expect
                        return self.keep(not happy, note, v2, expect, self.errortype('output'))
                            
                    except:
                        ff = f'ERROR: Weinmann2021figure1 stringOrFunction 1  Folder: {self.folder} File: {self.dafile}\nNote: {note} arg1: {arg1} arg2: {arg2}'
                        ee = {"error" : ff, "exception" : str(sys.exc_info()[1])}
                        self.logerr(2, ee)
                        return self.keep_sad(note, str(sys.exc_info()[1]), expect, self.errortype('runtime'))
                    # return {"msg": note, "bug": True, "actual": v2}
                else:
                    if (type(v1) is str):
                        # print("stringOrFunction returning v1", file=sys.stderr)
                        happy = v1 == expect
                        return self.keep(not happy, note, str(sys.exc_info()[1]), expect, self.errortype('output'))
                    
                    return self.keep_sad(note, v1, expect, self.errortype('output'))
                
            except:
                ff = f'ERROR: Weinmann2021figure1 stringOrFunction 2  Folder: {self.folder} File: {self.dafile}\nNote: {note} arg1: {arg1} arg2: {arg2}'
                ee = {"error" : ff, "exception" : str(sys.exc_info()[1])}
                self.logerr(2, ee)
                return self.keep_sad(note, v1, expect, self.errortype('runtime'))

        self.predicates = []
        args = [
            ( "[1] = 'All odd'", self.mf, [1], '', 'All odd' ),
            ( "[1,3] = 'All odd'", self.mf, [1,3], '', 'All odd' ),
            ( "[1,3,5] = 'All odd'", self.mf, [1,3,5], '', 'All odd' ),
            ( "[3,3,3,3] = 'All odd'", self.mf, [3,3,3,3], '', 'All odd' ),
            ( "[-3,-3,-3,-3] = 'All odd'", self.mf, [-3,-3,-3,-3], '', 'All odd' ),
            ( "[0] = 0", self.mf, [0], 3, 3 ),
            ( "[0, 0] = 0", self.mf, [0, 0], 4, 4 ),
            ( "[0, 0, 0] = 0", self.mf, [0, 0, 0], 5, 5 ),
            ( "[2, 0, 0] = 0", self.mf, [2, 0, 0], 5, 5 ),
            ( "[0, 2, 0] = 0", self.mf, [0, 2, 0], 5, 5 ),
            ( "[0, 0, 2] = 0", self.mf, [0, 0, 2], 5, 7 ),
            ( "[1, 0, 0] = 0", self.mf, [1, 0, 0], 5, 5 ),
            ( "[0, 1, 0] = 0", self.mf, [0, 1, 0], 5, 5 ),
            ( "[0, 0, 1] = 0", self.mf, [0, 0, 1], 5, 5 ),
            ( "[1, 2, 0] = 0", self.mf, [1, 2, 0], 5, 5 ),
            ( "[0, 1, 2] = 5 7", self.mf, [0, 1, 2], 5, 7 ),
            ( "[0, 2, 1] = 5 7", self.mf, [0, 2, 1], 5, 7 ),
            ( "[4, 1, 1] = 5 9", self.mf, [4, 1, 1], 5, 9 ),
            ( "[-4, 1, 1] = 5 1", self.mf, [-4, 1, 1], 5, 1 ),
            
        ]
        # self.predicates = list(map ( self.stringOrFunction, args ))
        self.predicates = list(map ( self.stringOrFunction, args ))
        good = list(filter(lambda x:  x["bug"] == False, self.predicates ))
        bad = list(filter(lambda x:  x["bug"] == True, self.predicates ))
        return len(bad), good, bad

    #
    # ============================================================================================
    # 
        
    def setXref(self):
        self.xref = {}
        for x in [
                ("Ericson2017figure1", self.Parson_Ericson2017figure1, "getSum"),
                ("Ericson2017figure4", self.Parson_Ericson2017figure4, "avgValuesInRange"),
                ("Ericson2018figure5", self.Parson_Ericson2018figure5, "isLevel"),
                ("Ericson2022figure2", self.Parson_Ericson2022figure2, "check_guess"),
                ("Ericson2022figure3", self.Parson_Ericson2022figure3, "Person"),
                ("Ericson2022figure4", self.Parson_Ericson2022figure4, "alarm_clock"),
                ("Ericson2022figure8", self.Parson_Ericson2022figure8, "getAverageDropLowest"),
                ("Haynes_Magyar2022figure2", self.Parson_Haynes_Magyar2022figure2, "has22"),
                ("Haynes_Magyar2022figure4", self.Parson_Haynes_Magyar2022figure4, "countInRange"),
                ("Hou2022figure2", self.Parson_Hou2022figure2, "filter_strings"),
                ("Karavirta2012Figure3", self.Parson_Karavirta2012Figure3, "findmax"),
                ("Weinmann2021figure1", self.Parson_Weinmann2021figure1, "last_even_adder")
        ]:
            self.xref[ x[0] ] = (x[1], x[2])
            

    def entry(self, bug, note, actual, expected, errortype=''):
        return {"folder": self.folder,
                "figure": self.me,
                "file": self.basename,
                "fullfile": self.dafile,
                "bug" : bug,
                "msg": note,
                "actual" : actual,
                "expected": expected,
                "errortype": errortype
                }

    def keep_happy(self, note, actual, expected):
        return self.entry(0, note, actual, expected, '')

    def keep_sad(self, note, actual, expected, errortype):
        return self.entry(1, note, actual, expected, errortype)

    def keep(self, bug, note, actual, expected, errortype):
        if bug:
            return self.keep_sad(note, actual, expected, errortype)
        else:
            return self.keep_happy(note, actual, expected)

    
    def setLog(self, n):
        self.loglevel = n
        # print("self.loglevel is now: " + str(self.loglevel) + ' after receiving: ' + str(n))

    def log(self, lvl, msg):
        if (lvl <= self.loglevel):
            print(msg)

    def logerr(self, lvl, msg):
        if (lvl < self.loglevel):
            print(msg, file=sys.stderr)

            
    def getFoldersIn(self, folder):
        files = os.listdir(folder)
        f = list( filter( lambda x: os.path.isdir(os.path.join(folder, x)),  files) ) 
        return f


    def checkem(self, args):
        note, result, expected = args
        rc = False
        if ( (type(expected) is int ) or (type(expected) is float)):
            rc = abs(  abs(result) - abs(expected)) < 0.0001
        else:
            rc = result == expected
        errortype = ''
        if not rc:
            errortype = self.errortype('output')
        return self.keep(not rc, note, result, expected, errortype)



    def set_predicates(self, alist):
        self.predicates = list(map ( self.checkem, alist ))

    def set_predicates_return(self, alist):
        self.set_predicates(alist)
        self.log(2,'set_predicates_return: ' + str(self.predicates))

        good = list(filter(lambda x: x["bug"] == False, self.predicates ))
        bad = list(filter(lambda x: x["bug"] == True, self.predicates ))
        self.log(2,'set_predicates_return good: ' + str(good))
        self.log(2,'set_predicates_return bad : ' + str(bad))
        return len(bad), good, bad


    def expectN(self, note, f, args, expect):
        # print(f'expectN: {note} f: {f}  args: {args} expect: {expect}')
        actual = None
        errortype = ''

        try:    
            actual = f(args)
        except:
            ff = f'ERROR: M.py expectN  Folder: {self.folder} File: {self.dafile}\nNote: {note} args: {args} expect: {expect}'
            ee = {"error" : ff, "exception" : str(sys.exc_info()[1]) }
            self.logerr(2, ee)
            return self.keep_sad(note, actual, expect, self.errortype('runtime'))

        withinlimit = abs(abs(actual) - abs(expect)) < 0.001
        if not withinlimit:
            errortype = self.errortype('output')

        return self.keep(not withinlimit, note, actual, expect, errortype)


    def me(self):
        return ""
    
    def mfname(self):
        return "getSum"
    
    def testit(self, problem):
        self.log(2, f'\ntestit start: {problem}') 
        fn, fname = self.xref[problem]
        self.log(2, f'\ntestit: fname: {fname}  fn: {fn} ') 
        rc = fn()
        self.log(2, f'\ntestit: rc {rc} ') 
        return rc



    def resetResults(self):
        self.results = []
        self.fails = []
        self.wins = []

    def addResults(self, things):
        self.results = self.results + things
    

    #
    # just the file
    #
    def getFileNames(self, folder, problem):
        dastring = f'{folder}/{problem}/{problem}*.py'
        self.ff = None
        self.log(1, f'getFileNames globs b4  : {self.ff}  glob: {dastring}')
        ff = glob.glob(dastring)
        justbase = list (map( os.path.basename, ff))
        self.log(1, f'getFileNames nices     : {justbase}')
        return justbase

    #
    # the whole path
    #
    def getFileNamesPath(self, folder, problem):
        dastring = f'{folder}/{problem}/{problem}*.py'
        self.ff = None
        self.log(1, f'getFileNames globs b4  : {self.ff}  glob: {dastring}')
        ff = glob.glob(dastring)
        self.log(1, f'getFileNames globs affa: {ff}  glob: {dastring}')
        return ff

    def getProblems(self):
        # return ['Hou2022figure2', 'Karavirta2012Figure3', 'Weinmann2021figure1']
        return ['Ericson2017figure1', 'Ericson2017figure4', 'Ericson2018figure5', 
                'Ericson2022figure2', 'Ericson2022figure3', 'Ericson2022figure4', 'Ericson2022figure8', 
                'Haynes_Magyar2022figure2', 'Haynes_Magyar2022figure4', 
                'Hou2022figure2', 'Karavirta2012Figure3', 'Weinmann2021figure1']


# # ------------------------------------------------------------------------------

    def testProblems(self, folder, problems, reset=False):
        self.log(1,f'\ntestProblems() folder: {folder} problems: {problems} reset: {reset}')
        if reset:
            self.resetResults()
        for p in problems:
            fnames = list( self.getFileNames(folder, p) )
            self.log(2,f'   testProblems running: {p} files: {fnames}')
            self.testFolderProblemFiles(folder, p, fnames)
        return self.results


    def testFolderProblemFiles(self, folder, problem, files):
        self.log(1,f'\ntestFolderProblemFiles() folder: {folder} problem: {problem} files: {files}')
        p = Path('.')
        for f in files:
            self.addResults(
                self.testFolderProblemFile(folder, problem, f)
            )

    #
    # nerf through subfolders 
    #
    def testAll(self, folder= '../data/V'):
        self.resetResults()
        for adir in self.getFoldersIn(folder):
            self.log(1,f'testAll folder: {adir} --------------------------------------------------------------')
            apath = os.path.join(folder, adir)
            self.testProblems(apath, self.getProblems())
            self.log(1,f'result size now: {len(self.results)}')
        return self.results

    #
    # testFile('./V/V1', 'Ericson2018figure5', 'Parson_Ericson2018figure5_13.py')
    #
    def testFolderProblemFile(self, folder, problem, afile):
        self.log(1, f'\ntestFolderProblemFile() folder: {folder} problem: {problem} file: {afile}')
        # self.dafile = f'{folder}/{problem}/{afile}'
        self.dafile = os.path.join(folder, problem, afile)
        self.folder = folder
        self.me = problem
        self.basename = afile
        myfails = []
        mywins = []
                
        # mpath = f'{folder}/{problem}'
        mpath = os.path.join(folder, problem)
        seeking = os.path.join(folder, problem, afile)
        self.log(2, f'  seeking: {seeking}')

        there = os.path.exists(seeking+".py")
        self.log(2, f'  seeking? {there}: {seeking}')
        f = os.path.abspath(seeking)

        fails = 0

        sys.path.insert(0, mpath)
                
        self.log(2,f'testFolderProblemFile() xref [{problem}]...')
        m, f = self.xref[problem]

        self.log(2,"\ntestFolderProblemFile start\n")
        # self.dafile = f'{problem}_{i}'
        expect_export = False
        try:
            modulename = os.path.basename(self.dafile)[:-3]
            self.log(3,f'\nimport trying: {modulename} whole: {self.dafile}')
            self.m = __import__(modulename)
            expect_export = True
            self.log(3,f'\nimport happy : {modulename}')
            try:
                self.log(3,"source code: " + inspect.getsource(self.m))
            except:
                self.log(3,"inspect not happy.")

            if (hasattr(self.m, f)):
                self.log(3,"attribute function happy " + f)
                self.mf = getattr(self.m, f)                            

            try: 
                self.log(3,"\ntestFolderProblemFile calling testit\n")

                nfail, good, bad = self.testit(problem)

                self.log(3,f'\n\ntestit()====================================\n fail: {nfail} \n  good: {good} \n  bad: {bad} ')
                if (nfail >0):
                    fails += 1

                myfails = myfails + bad
                mywins = mywins + good
                # self.fails = self.fails + bad
                # self.wins = self.wins + good 

            except:
                ff = f'ERROR: error running File: {self.dafile}'
                ee = {"error" : ff, "exception" :  str(sys.exc_info()[1]) }
                self.logerr(2, ee)

                fails += 1
                bug = self.keep_sad("error running " + self.dafile,
                                 str(sys.exc_info()[1]),
                                 'should run',
                                 self.errortype('runtime')
                                 )
                self.log(2,"   runtime issue " + str(bug))
                # self.fails.append( bug )
                myfails.append( bug )
    
        except:
            ff = f'ERROR: problem with import  File: {self.dafile}'
            ee = {"error" : ff, "exception" :  str(sys.exc_info()[1]) }
            self.logerr(2, ee)

            fails += 1

            # self.fails.append(
            myfails.append(
                self.keep_sad("error importing source code " + self.dafile,
                           str(sys.exc_info()[1]),
                           'should import',
                           self.errortype('import')
                           )
            )

        try:
            del sys.modules[modulename]
            # del sys.modules[self.dafile]
            self.log(2, f'success removing module: {modulename}')
        except:
            #
            # not necessarily bad, might not have imported ?
            #
            if expect_export:
                self.log(1, f'error: could not remove module: {modulename}')

        # return fails
        self.log(1, f'testFolderProblemFile returns fails: {len(myfails)} wins: {len(mywins)}')
        return myfails + mywins
        


    def ppjson(self):
        return json.dumps (self.fails + self.wins) 
        
    # def pp(self):
    #     for key, (n, good, bad) in self.fails.items():
    #         print(f'{key}: ({n})')

    # def pp2(self):
    #     for key, (n, good, bad) in self.fails.items():
    #         print(f'\n{key}: ({n})\nGood: {good}\nBad : {bad}')

    # def pp3(self):
    #     for key, (n, good, bad) in self.fails.items():
    #         print(f'\n{key}: ({n})\nGood: {good}\nBad : {bad}')

    def go(self, folder, dbg=0):
        self.setLog(dbg)
        self.setUpFolder(folder)
        rc = self.loopit(dbg)
        return self.fails + self.wins

    def pp(self, folder, dbg=0):
        x = self.go(folder, dbg)
        return json.dumps (x)

    def cmdfolder(self):
        n = len(sys.argv)
        folder = ''
        if (n>1):
            folder = sys.argv[1]
        # print("folder: ", folder)
        return folder

