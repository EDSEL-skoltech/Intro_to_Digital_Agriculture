monica run sim_*
rm sim*
rm site*
cat ./total_result/*out* | head -4 | tail -1 >> potato-2015.csv
cat ./total_result/*out* | head -5 | tail -1 >> sugarbeat-2016.csv
cat ./total_result/*out* | head -6 | tail -1 >> potato-2017.csv
cat ./total_result/*out* | head -7 | tail -1 >> sugarbeat-2018.csv
cat ./total_result/*out* | head -8 | tail -1 >> potato-2019.csv
rm ./total_result/*out*
