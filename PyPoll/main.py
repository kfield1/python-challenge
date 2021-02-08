<<<<<<< HEAD
total_votes = 0


import csv
file_path = "./Resources/election_data.csv"
with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        # The total number of votes cast
        total_votes = total_votes + 1

        # A complete list of candidates who received votes


        # The percentage of votes each candidate won


        # The total number of votes each candidate won


        # The winner of the election based on popular vote.

# print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")



# What it should look like
=======
# The total number of votes cast
total_votes = 0

# A complete list of candidates who received votes
import csv
file_path = "../Resources/election_data.csv"

with open(file_path) as csvfile:
    
    csvreader = csv.reader(csvfile)
    
    csv_header = next(csvreader)
   
    for row in csvreader:

# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.


>>>>>>> cf1df046be2518b04d129361efd0c3fdb3cd3074
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
<<<<<<< HEAD




=======
>>>>>>> cf1df046be2518b04d129361efd0c3fdb3cd3074
