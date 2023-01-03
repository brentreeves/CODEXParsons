
# CODEXParsons
Testing CODEX with Parsons problems

1. O.py main class for unit testing
1. Parsons_X classes for various specific Parsons problems

# Jupyter
Jupyter Notebook analyze.ipynb does some initial processing from /data and organizes unittests/V1,V2,V3

# batch
/unittests/runall.sh will run each problem in each of the V folders, creating some json files and finally producing ppfails.json.csv
cd to /unittests and run it from there.

# Notes
We use jq is a utility to filter json.
We use pandas to convert json to csv.  Overkill.
