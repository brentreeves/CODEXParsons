#!python3
import sys
import os
import pandas as pd
import numpy as np
import json
import MM as m
dir(m)

n = m.Parsons()
n.resetResults()
n.setLog(0)
#units = n.testProblems( '../data/V/V3',["Weinmann2021figure1"], True)
units = n.testProblems( '../data/V/V1',['Karavirta2012Figure3'], True)
#units = n.testProblems( '../data/V/V1',['Ericson2017figure1'], True)
# units = n.testProblems( '../data/V/V2',['Karavirta2012Figure3'], False)
# units = n.testProblems( '../data/V/V3',['Karavirta2012Figure3'], False)
df = pd.json_normalize(units,meta=['folder', 'figure', 'file', 'bug', 'msg', 'actual', 'expected', 'errortype'])

print("\ndf ---------------------------------------------------------")
print(df)
dg = df.groupby(['folder','figure','file'], as_index = False).sum('bug')
f = dg[ dg['bug'] > 0]
print(f)
