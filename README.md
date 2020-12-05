# Adamic_FinalProject

This is my final project for Biol 7863. 

DESCRIPTION: 
This Python script takes an Excel file (.xlsx) as input, containing subject repsonse data for the Visceral Interoceptive Awareness brain imaging task.
It will find invalid negative responses (occurring due to subject error), and will replace these with NaN's. 
This Excel file MUST have the following format: 

- One sheet for each imaging run 
- 12 rows, one for each event (4 conditions (heart, lung, stomach, target) x 3 trials each = 12 rows total)
- One column for each subject (with the exception of the first column, labelled "Event") 

INSTRUCTIONS: 
This Python script is run via the command line. 

>> Navigate to directory containing the script, and the data file 

>> python3 Adamic_FinalProj.py VIA_response_data.xlsx
