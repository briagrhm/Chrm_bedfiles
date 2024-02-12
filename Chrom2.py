import pandas as pd
from pandas import DataFrame
from pandas import read_csv
import csv
import os
import argparse


parser = argparse.ArgumentParser(description = 'Generate chunk files and add bumpers if needed for chromosome analysis.', add_help= True)
parser.add_argument('--file', help='Specify the filename to be used', type=str)
parser.add_argument('--bumper', help='Specify the bumper amount you want subtracted from the start and added to the end chrom.', default= '0', type=int)
parser.add_argument('--chunk_size', help="Enter the percentage you want the files split into", type=int)

if __name__ == "__main__":

    args = parser.parse_args()

# Load up the file 
    
# Get the current working directory 
now = os.getcwd()

#Create user input of file name 
file = args.file

# Join the current working directory and the file name to be loaded 
files = os.path.join(now, file)


#read the file 
chrom_file = pd.read_csv(files, sep = '\t', header = None)
#Print to make sure the file succesfully loaded
print("file loaded")

# # Create bumper input 
input_value = args.bumper
print(input_value)



# # Subtract bumper input from column 1 and add to column 2 
chrom_file[1] = chrom_file[1]- input_value
chrom_file[2] = chrom_file[2]+ input_value
# Set df[1] to 0 if negative, but leave other columns alone
chrom_file[1] = chrom_file[1].where(chrom_file[1] >= 0, 0)
#Print the entire file with the changed bumper amounts
print(chrom_file)

# # Save the new dataframe as txt or csv file to open again 
# Save the whole data file before breaking into chunksizes
# df = pd.DataFrame(chrom_file)
# df.to_csv('chrom_file.csv', sep = '\t', encoding='utf-8', index = False, header= None)

## Chunksize file code

# Obtain the length of the file 
CTCF = len(chrom_file)


#Creat input for the integer to represent the percentage. 
percent_input = args.chunk_size
deliverables = round((CTCF*(percent_input/100)))



# Set variables for chunksize, label batches of data(batch_no)
chunk_size = deliverables


#Setting the percentages up for the saved files
lower_variable = 0 
upper_variable = percent_input 

#Break into chunk and iterate through the chunked data. Also save chuked data into seperate folders 
  #load file name in and use input file as output file name
for chunk in pd.read_csv('chrom_file.csv', chunksize=chunk_size):
    file_name = f"{file}_{lower_variable}-{upper_variable}%.bed"
    chunk.to_csv(file_name, sep = '\t', header=None, index=False)

    print(f"File '{file_name}' created. ")

    #Iterate upper and lower variable 
    lower_variable += percent_input
    upper_variable += percent_input
    