# Winter '22
# Brent Reeves
#
# get some nested items out of json data to produce csv
#
cat /dev/null > all.json
for v in V*
do
echo working on data$v.json
jq '.[] | .folder as $fol | .problem as $p | .tests[] | .figure as $fig | (.issues[] | {"folder": $fol, "problem": $p, "file": $fig, ok, errortype, msg, actual})' < data$v.json >> all.json
done
#
# that json is illformed, just a sequence of {}
# now slurp and reformat into legit json
jq -s '.' all.json > alls.json
#
# convert to csv
python3 json2csv.py alls.json
