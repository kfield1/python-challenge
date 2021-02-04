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
