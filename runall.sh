# runall.sh
#
# Winter '22 / Brent Reeves
#
# for each version (V1, V2, V3)
#    test each python file append to data_$v
#
# for f in Parsons_Ericson2017f*.py
# for f in Parsons_Ericson2022f*.py
# for f in Parsons_Haynes*.py
# for f in Parsons_Hou*.py
# for f in Parsons_Kara*.py
# for f in Parsons_Kara*.py
# for f in Parsons_Wei*.py
for v in V*
do
    cat '' > data_$v.txt
done

for f in Parsons_*.py
do
    for v in V*
    do
	echo $f $v --------------
	python $f $v >> data_$v.txt
    done
done
