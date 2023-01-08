# runall.sh
#
# Winter '22 / Brent Reeves
#
# for each version (V1, V2, V3)
#    test each python file and append to data_$v
#
cat /dev/null > alldata.csv
for v in V*
do
    echo "folder start " $v "---------------------------------------------------------------"
    for f in Parsons_*.py
    do
	echo $f $v --------------------------------------------------------------
	python3 $f $v 0 > temp.json
	python3 json2csv.py temp.json
	cat temp.json.csv >> alldata.csv
    done
    echo "folder end   " $v "---------------------------------------------------------------"
done
head -1 alldata.csv > header.csv
grep -v  "^folder,figure,file" alldata.csv > temp1.csv
sort -t, -k 2,2 -k 1,1 -k 3,3 temp1.csv > temp2.csv
cat header.csv temp2.csv > parsons.csv
#
# now for uniques
#
sort -t, -u -k2,2 -k1,1 -k3,3 -k4,4n temp1.csv > temp3.csv
cat header.csv temp3.csv > u.csv




