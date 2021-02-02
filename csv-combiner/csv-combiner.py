'''Write a command line program that takes several CSV files as arguments. 
Each CSV file (found in the fixtures directory of this repo) will have the 
same columns. Your script should output a new CSV file to stdout that contains 
the rows from each of the inputs along with an additional column that has the 
filename from which the row came (only the file's basename, not the entire path). 
Use filename as the header for the additional column.'''

#!/usr/bin/python

import sys
import csv
import pandas

file1=sys.argv[1]
file2=sys.argv[2]

file1_name=file1.split('/')[1]
file2_name=file2.split('/')[1]

'''first=pandas.read_csv(file1)
second=pandas.read_csv(file2)

first['filename']=[file1_name]*len(first.index)
second['filename']=[file2_name]*len(second.index)

combined=pandas.concat([first, second], axis=0)

print(combined)'''

#Reading both files as pandas dataframes - doing so in chunks of size 10^6 
#to cater to larger files that may throw memory errors otherwise
file_iter1=pandas.read_csv(file1, chunksize=10000000)
file_iter2=pandas.read_csv(file2, chunksize=10000000)

combined=[]  

#Iterating through each chuck to add the filename to the dataframe and then
#putting the updated datarfarme in a list
for data in file_iter1:  
    data['filename']=[file1_name]*len(data.index)
    combined.append(data)
for data in file_iter2:  
    data['filename']=[file2_name]*len(data.index)
    combined.append(data)

#concatenating all of the chunks and converting to a csv format for printing    
print((pandas.concat(combined, axis=0, ignore_index=True)).to_csv())