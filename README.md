
# CODEXParsons
Testing CODEX with Parsons problems

## New
Two notebooks:
1. analyze read a csv and distribute things into folders/files
2. unit/reports read a csv, distribute things, run unit tests on them
3. unit/PCA principal component analysis on loops, ifs, linecount, returns

## Old:
Two major parts:

# The first part lives in /unittests

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

# The second major part lives in /unit

This part is working towards inclusion in jupyter notebook.
O.py has been renamed to M.py and the Parsons_*.py files have been adjusted to be callable.

this folder also has a runall.sh which loops through V1/2/3 subfolders and runs each Parsons_*.py program.

It uses some unix utilities: grep, head, sort and cat.
Usage for runall is:
./runall.sh &> errors