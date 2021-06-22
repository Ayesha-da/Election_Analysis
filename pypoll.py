#list of candidates who received votes
#number of total votes 
#number of votes each candidate received
#percentage of votes received by each
#winner
file_to_load='Resources/election_results.csv'
##with open(file_to_load) as election_data:
# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
    # open election result and read the file
with open(file_to_load) as Election_data:

# To do: read and analyze the data here.
  file_reader = csv.reader(Election_data)
# read and print the header row
  headers =next(file_reader)
  print(headers)
