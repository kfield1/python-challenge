total_votes = 0
candidate_options =[]
candidate_votes = {}
winning_candidate = ""
winning_count = 0
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
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]= 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] +1

    for candidate in candidate_votes:
         # The percentage of votes each candidate won
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
            
        # The total number of votes each candidate won
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # The winner of the election based on popular vote.
        
# print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_votes:
    voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})" 
    print(voter_output)
print("-------------------------")
print(f"Winner:{winning_candidate}")
# What it should look like
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




