rm *.csv
#cat sobol_monica.py | tail -14 | head -10 > conditions.txt
#touch sugar-beet-2011.csv spring-barley-2012.csv sugar-beet-2014.csv soybean-000-2015.csv sugar-beet-2017.csv
date > start.txt
./sobol_monica.py > logerror.txt
#date > finish.txt
#touch Sobol_SA.txt
#cat conditions.txt >>Sobol_SA.txt
#python sobol.py >> Sobol_SA.txt

