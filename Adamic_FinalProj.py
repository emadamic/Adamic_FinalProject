"""
BIOL 7863: FINAL PROJECT
Written by: Emily Adamic
Created: 12/04/2020
Last edited: 12/04/2020
"""

# ------------------
# This script is written via argument parsing, run via command line. 

# To run: 
# python3 Adamic_FinalProj.py <name_of_Excel_file.xlsx>

# Input file MUST contain:
# One tab for each run
# On each tab: 
    # 12 rows (3 trials x 4 conditions - heart, stomach, lungs, target)
    # one column for each subject, except the first column as the "Event"

# ------------------


#%% 
import pandas as pd
import argparse
from pyxlsb import open_workbook

#%% 
"""
Argument parser set-up
"""
# initialize the class
parser = argparse.ArgumentParser(description='This script will replace all negative VIA task responses with an NaN.')

# add positional arguments
parser.add_argument("input_file", help="Input file is an Excel workbook in this format: 1 sheet per run, each sheet has 12 rows (3 trials x 4 conditions) & 1 column per participant with 1st column labelled 'Event'.")

# put args togehter 
args = parser.parse_args()

#%% 
'''
Run the code: 
    For every sheet in the Excel file: 
        Load sheet
        Execute code to processed responses
        Save as new processed sheet
'''

#%%
# TO TEST this script without arg parsing, can load this input file as df:
# df = pd.ExcelFile('VIA_response_data.xlsx')
# sheets = df.sheet_names
# df = pd.read_excel('VIA_response_data.xlsx', sheet_name = 'Run_A') 
#%% 

# get a list of all the sheets in the Excel workbook 
workbook = pd.ExcelFile(args.input_file)
sheets = workbook.sheet_names

#%% 

for sheet in sheets:    # for every sheet in the Excel workbook (i.e. for every imaging Run)
    
    COUNTER=0

    print("\nWorking on: ", sheet)
    df = pd.read_excel('VIA_response_data.xlsx', sheet_name = sheet) # load the sheet as a df 

    events = df.iloc[:,0]  # get the first column (should be "Event")
    processed_df = pd.DataFrame(events) # make the 1st column a data frame
    # will add each subject's processed column to this

    for column in df:  # for every subject column
        if column != "Event":  # except for Event column 
            
            col = df[column] # pull out column for that subject
            processed_col = []  # initialize empty list for this subject's new (processed) column 
        
            for row in col: # for every row in this subject's column 
                if row < 0: # if row is neg, change to NaN
                    new_row = float('NaN') # if negative, change to NaN 
                    COUNTER=COUNTER+1  # keep count of how many data points are missing 
                else:      # else row is positive, keep as is 
                    new_row = row
                processed_col.append(new_row)  # add new row to processed column

            processed_col = pd.DataFrame(processed_col) # convert new col to df 

            processed_col.rename( columns={ processed_col.columns[0]: column}, inplace=True )  # add subject ID as column title

            processed_df = pd.concat([processed_df, processed_col], axis=1) # add subject's new column to processed df

    # make sure the 
    if df.shape == processed_df.shape:
        print("\n\tSuccess!  Processed all subject columns for", sheet) 
        print("\tThere were", COUNTER, "NaN's.")
    else:
        print("\nUh oh. Looks like the new and old data frames don't match up.")
        break

    # save the CSV file for the run 
    new_file_name = sheet + "_VIAProcessed.csv"
    print("\tSaving sheet: ", sheet, "\n")
    processed_df.to_csv(new_file_name)

    del processed_df   # delete from the env so can reset for next run 

    if sheet == sheets[len(sheets)-1]:
        print("All done-zo!\n\n")


#%% 

