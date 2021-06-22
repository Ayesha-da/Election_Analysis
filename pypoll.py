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

#initialize a total vote counter
total_votes = 0
# initialize candidate list
candidate_options = []
# declare dictionary to link candidates and votes
candidate_votes = {}
# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
    # open election result and read the file
with open(file_to_load) as Election_data:

# To do: read and analyze the data here.
  file_reader = csv.reader(Election_data)
# read and print the header row
  headers =next(file_reader)
#print each row in csv file
  for row in file_reader:
      # add to the total count
      total_votes += 1
      # Print the candidate name from each row
      candidate_name = row[2]
      #if candiate doesnot match any exixting candidate
      if candidate_name not in candidate_options:
# add candidate name to the list
         candidate_options.append(candidate_name)
         # begin tracking candidate votes
         candidate_votes[candidate_name] = 0
    #add a vote to candidate count
      candidate_votes[candidate_name] += 1
      # Save the results to our text file.
with open(file_to_save, "w") as text_file:
        # Print the final vote count to the terminal.
  election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
  print(election_results, end="")
    # Save the final vote count to the text file.
  text_file.write(election_results)
        # determine percentage of vote for each candidate by looping through counts
        # 1. Iterate through candidate list
  for candidate_name in candidate_votes:
            # retrieve vote count of candidate
            votes = candidate_votes[candidate_name]
            # calculate the percentage of votes
            vote_percentage = float(votes)/float(total_votes)*100

            #To do: print out each candidate's name, vote count, and percentage votes to the terminal.

            # detrermine winning voate and canmdidate
            #1. determine if the votes are greater than winning count
            if(votes > winning_count) and (vote_percentage > winning_percentage):
              # if true set winning count = vote and winning percentage = vote percentage
              winning_count = votes
              winning_percentage = vote_percentage
              # set winning candidate equal to candidate name
              winning_candidate = candidate_name
            #print candidate name and percentage of votes
            candidate_result = (f"{candidate_name}:  {vote_percentage:.1f}%  ({votes})\n")
          # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_result)
          #  Save the candidate results to our text file.
            text_file.write(candidate_result)
  winning_candidate_summary =(
      f"------------------\n"
      f"Winner = {winning_candidate}\n"
      f"Winner vote count = {winning_count:,}\n"
      f"Winning Percentage = {winning_percentage:.1f}%\n")
  print(winning_candidate_summary)
  text_file.write(winning_candidate_summary)