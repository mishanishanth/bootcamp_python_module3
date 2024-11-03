# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
Candidate=[]
vote_count={}  


# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes=total_votes+1

        # Get the candidate's name from the row
        candidate_name=row[2]


        # If the candidate is not already in the candidate list, add them
        if candidate_name not in Candidate:
            Candidate.append(candidate_name)
            vote_count[candidate_name] = 0 

        # Add a vote to the candidate's count
        vote_count[candidate_name]+=1
        
        


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)

    print(f"Total votes: {total_votes}")
    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner
     # Get the vote count and calculate the percentage

    winning_candidate=None
    highest_votes=0
    for candidate,votes in vote_count.items():
            percentage=round((votes/total_votes)*100,3)
            print(f"{candidate}: {percentage:}% ({votes})")  # Print and save each candidate's vote count and percentage
            if votes>highest_votes:
                 highest_votes=votes
                 winning_candidate=candidate    # Update the winning candidate if this one has more votes
    print(f"Winner: {winning_candidate}")            
         
   
 
   # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(f"Election Results\n")
        txt_file.write(f"-----------------\n")	
        txt_file.write(f"Total Votes:{total_votes}\n")
        winning_candidate=None
        highest_votes=0
        for candidate,votes in vote_count.items():
            percentage=round((votes/total_votes)*100,3)
            txt_file.write(f"{candidate}: {percentage:}% ({votes})\n")  # Print and save each candidate's vote count and percentage
            if votes>highest_votes:
                 highest_votes=votes
                 winning_candidate=candidate

        txt_file.write(f"Winner: {winning_candidate}")    

