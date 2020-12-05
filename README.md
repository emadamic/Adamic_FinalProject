This is my final project for Biol 7863. 

## DESCRIPTION: 
Input to this Python script is an Excel workbook containing subject repsonse data from the Visceral Interoceptive Awareness (VIA) brain imaging task.
This script will replace invalid *negative* responses (occurring due to subject error) with NaN's. This is a necessary step before the response data can be used for further analysis. It will save each processed run as a separate CSV file in the same directory. 

## INSTRUCTIONS: 
This Python script is written via argument parsing, and run via the command line. 
The input Excel file MUST have the following format: 

- One sheet for each imaging run
- Per sheet: 
  - 12 rows, one for each event (4 conditions (heart, lung, stomach, target) x 3 trials each = 12 rows total)
  - One column for each subject (with the exception of the first column, labelled "Event") 

>> First, navigate to the directory containing the script & the data file (must be in the same directory). 

>> python3 Adamic_FinalProj.py VIA_response_data.xlsx
