#import library
import os
import csv
from pathlib import Path

# path to collect data from the Resources folder
election_data = os.path.join("Resources", 'election_data.csv')

# open the election data file as a csv
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    ## initialize variables to store information
    #votes = []

    ##read through each row of data following header
    #for rows in csvreader:
        
        ## append totals for votes
        #votes.append(int(rows[0]))
        

        

    # empty variable for candidates list
    candidates = []

    #read through each row of data following header
    for row in csvreader:
        candidates.append(int(row[2]))
        print (candidates)



    ## append totals for votes
    #votes.append(int(rows[0]))


######################

# Objectives:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.