import pandas as pd
from pandas import DataFrame
from pandas import read_csv
import csv
import os
import argparse


parser = argparse.ArgumentParser(description = 'Generate chunk files and add bumpers if needed for chromosome analysis.', add_help= True)
parser.add_argument('--chrom_file', help='Specify the filename to be used', required=True)
parser.add_argument('--bumper', help='Specify the bumper amount you want subtracted from the start and added to the end chrom.', default= 0)
parser.add_argument('--chunk_size', help="Enter the percentage you want the files split into")

if __name__ == "__main__":

    args = parser.parse_args()

# Load up the file 
    
# Get the current working directory 
now = os.getcwd()

#Create user input of file name 
files = str(input('file name:'))

# Join the current working directory and the file name to be loaded 
file = os.path.join(now, files)


#read the file 
chrom_file = pd.read_csv(file, sep = '\t', header = None)
#Print to make sure the file succesfully loaded
print("Chrom file loaded")

# # Create bumper input 
input_value = int(input('Bumper Amount:'))
if args.bumper == input_value:
    print(input_value)

# # Subtract bumper input from column 1 and add to column 2 
chrom_file[1] = chrom_file[1]- input_value
chrom_file[2] = chrom_file[2]+ input_value
# Set df[1] to 0 if negative, but leave other columns alone
chrom_file[1] = chrom_file[1].where(chrom_file[1] >= 0, 0)
#Print the entire file with the changed bumper amounts
print(chrom_file)

# Save the new dataframe as txt or csv file to open again 
df = pd.DataFrame(chrom_file)
df.to_csv('chrom_file.csv', encoding='utf-8', index = False, header= None)

## Chunksize file code

# Obtain the length of the file 
CTCF = len(chrom_file)


#Creat input for the integer to represent the percentage. 
percent_input = int(input("Percentage:%"))
deliverables = round((CTCF*(percent_input/100)))

if args.chunk_size == percent_input:
    print(percent_input)

# Set variables for chunksize, label batches of data(batch_no)
chunk_size = deliverables
batch_no = 1

#Break into chunk and iterate through the chunked data. Also save chuked data into seperate folders 
for chunk in pd.read_csv('chrom_file.csv', chunksize=chunk_size):
    chunk.to_csv('CTCF Chunks' + str(batch_no)+ '.txt')
    batch_no +=1