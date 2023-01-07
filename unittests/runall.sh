# runall.sh
#
# Winter '22 / Brent Reeves
#
# for each version (V1, V2, V3)
#    test each python file and append to data_$v
#
for v in V*
do
    echo "folder start " $v "----------------------------"
    echo '[' > data$v.txt
    for f in Parsons_*.py
    do
	echo $f $v --------------
	python3 $f $v >> data$v.txt
    done
    sed "$ s/, $/]/" data$v.txt > data$v.json
    echo "folder end   " $v "----------------------------"
    python3 -m json.tool data$v.json > pp$v.json
    /Applications/jq '.[] | {folder: .folder, problem: .problem, fails: .fails}' < data$v.json > fails$v.json
done
# -s 'slurp' accepts sequences of {} without separating commas
cat failsV*.json | /Applications/jq -s '.' > ppfails.json
python3 json2csv.py ppfails.json



