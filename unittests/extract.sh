# Winter '22 Brent Reeves
#
cat /dev/null > all.json
for v in V*
do
echo working on data$v.json
jq '.[] | .folder as $fol | .problem as $p | .tests[] | .figure as $fig | (.issues[] | {"folder": $fol, "problem": $p, "file": $fig, ok, errortype, msg, actual})' < data$v.json >> all.json
done
jq -s '.' all.json > alls.json

python3 json2csv.py alls.json
