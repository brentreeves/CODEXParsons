#!python3
import json
import os
import MM as m
dir(m)
# n = m.Parsons('Ericson2018figure5', 'isLevel')
n = m.Parsons()
n.setLog(0)
# print ( dir(n) )
# n.go('../data/V', 0)
ps = [
    ('../data/V/V1',"Ericson2017figure1", 'Ericson2017figure1_0'),
    ('../data/V/V1',"Ericson2017figure4", 'Ericson2017figure4_0'),
    ('../data/V/V1',"Ericson2018figure5", 'Ericson2018figure5_0'),
    ('../data/V/V1',"Ericson2022figure2", 'Ericson2022figure2_0'),
    ('../data/V/V1',"Ericson2022figure3", 'Ericson2022figure3_0'),
    ('../data/V/V1',"Ericson2022figure4", 'Ericson2022figure4_0'),
    ('../data/V/V1',"Ericson2022figure8", 'Ericson2022figure8_0'),
    ('../data/V/V1',"Haynes_Magyar2022figure2", 'Haynes_Magyar2022figure2_0'),
    ('../data/V/V1',"Haynes_Magyar2022figure4", 'Haynes_Magyar2022figure4_0'),
    ('../data/V/V1',"Hou2022figure2", 'Hou2022figure2_0'),
    ('../data/V/V1',"Karavirta2012Figure3", 'Karavirta2012Figure3_0'),
    ('../data/V/V1',"Weinmann2021figure1", 'Weinmann2021figure1_0'),
]

n.setLog(0)
n.resetResults()
# print(ps[0], " -- ", ps[1])

print ( json.dumps( n.testProblems( ps[0][0], [ ps[0][1] ]) ) )
# print ( json.dumps( n.testProblems( '../data/V/V1', [ 'Ericson2017figure1' ] ) ) )


# for p in ps[0:1]:
#     print ( json.dumps( n.testProblems( p[0], p[1], p[2]) ) )

# for r in ps[0:2]:
#     print ( json.dumps (n.test1(r[0], r[1], r[2]) ))
    
