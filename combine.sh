
#Add header to chomosome gene data
#Author: Aude "bash woman" 
#Last modified Fri Dec 9, 2016
#for question, contact <aude.bouagnon@ucsf.edu>


echo "Starting combining script"
for file in "$@"
do
	
   	echo "$file"
	cat raw/header.txt "$file" > processed/$file
	python gc_gene_plot.py processed/$file
hello
done
echo "Done!!"


#here is an edit i made on github
