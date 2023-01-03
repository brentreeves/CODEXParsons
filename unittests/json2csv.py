import pandas as pd
import sys

try:
    f = sys.argv[1]

    with open(f, encoding='utf-8') as inputfile:
        df = pd.read_json(inputfile)

    df.to_csv(f+".csv", encoding='utf-8', index=False)

except:
    print("no bueno: ", str(sys.exc_info()[1]))
    
