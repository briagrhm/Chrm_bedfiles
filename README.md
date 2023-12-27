# Chrm_bedfiles
Read bed file that can be separated into chunksize files as well as add bumpers
## Overview of the Project
The bedfiles consisit of tab-delimited  text files that contain chromosome numbers in the first column and then start and stop coordinates in the second and third columns. An input will be created to split the bed file into percentages based on the users need. These files will then be saved seperately into individual txt filess.
## Summary 
Two seperate python files were created in jupyter notebookto first to add bumpers onto the chromosome files start and end as well as save the chunksize files. For the bumper file user input is required to determine bumper amount. Parameters were put into place to stop columns from going into the negatives but to be set them to zero instead. For the chinksize file the user inputs what percentage they want the files to be seperated into. The files are divided based on the input and the files are seperated and saved to individual txt files. The python function ArgParse was used to join these two python scripts together so that they could be used for command line interface (CLI). This makes the code user friendly for other users to input whatever bedfile they want and obtain the needed changes. This code of the combined files was then tested in Visual Studio Code to make sure the command line could be easily used.  

