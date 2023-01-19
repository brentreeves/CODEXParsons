#!python3
import os
import pandas as pd
import json

import MM as m
# dir(m)
# n = m.Parsons('Ericson2018figure5', 'isLevel')
n = m.Parsons()

n.resetResults()
n.setLog(1)
alls = n.testAll()
df = pd.json_normalize(alls,meta=['folder', 'figure', 'file', 'fullfile', 'bug', 'msg', 'actual', 'expected', 'errortype'])

g1 = df.groupby(['folder','figure','file'], as_index = False).sum('bug')
g1.to_csv('alls.csv', sep=',', index=False, encoding='utf-8')

bugs = g1[ g1['bug'] > 0]
print("\nbugs -----")
print(bugs)

g2 = bugs.groupby(['folder','figure'], as_index = False).count()
print("\ng2 -----")
print(g2)

g2.to_csv('alls_bugs.csv', sep=',', index=False, encoding='utf-8')

