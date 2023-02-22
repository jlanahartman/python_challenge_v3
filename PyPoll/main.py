"""
We are looking for......

- The total number of votes cast

- A complete list of candidates who received votes

- The percentage of votes each candidate won

- The total number of votes each candidate won

- The winner of the election based on popular vote
"""

import os
import csv

election_data_csv_path = os.path.join("Resources", "election_data.csv")
outputFile = os.path.join("analysis", "electionResults.txt")

# Declare variables 
totalVotes = 0 
candidateList = [] 
candidateVotes = {}   
winningCount = 0
electionWinner = 0

# os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(election_data_csv_path, "r") as csvFile: 
    readFile= csv.reader(csvFile, delimiter=",")

    header = next(readFile)

    # rows will be lists where index[0] is ballot id, index[1] is county, index[2] is the canidate

    for row in readFile: 
        totalVotes += 1

        # check to see if the canidate is in the list of canidates 
        if row[2] not in candidateList:
            candidateList.append(row[2])
        
        # add the value to the dictionary as well
        # {'key': 'value'}
        # start the count at 1 for votes
    
            candidateVotes[row[2]] = 1
        else:
            candidateVotes[row[2]] += 1

       # print(canidateVotes)

    # print(canidateVotes)   
for candidate in candidateList:
    votes = candidateVotes[candidate]
    votePercentage = float(votes) / float(totalVotes) * 100

    voteOutput = f"\t {candidate} : {votePercentage: .2f}% "
   #  print(voteOutput)

if votes > winningCount:
    winningCount = votes
    electionWinner = candidate


# print the results data to our txt file
with open(outputFile, "w") as textFile:
    

    output = (
    f"Survey Results"
    f"\n -------------------------- \n"
    f"\n Total Votes: {totalVotes} \n"
    f"\n -------------------------- \n"
    )

    textFile.write(output)
    
    for candidate in candidateList:
        votes = candidateVotes[candidate]
        votePercentage = float(votes) / float(totalVotes) * 100

        voteOutput = f"\n{candidate} : {votePercentage: .2f}% : {votes} \n"
        textFile.write(voteOutput)

        print(voteOutput)

        if votes > winningCount:
            winningCount = votes
            electionWinner = candidate

    electionWinnerOutput = f"\n Winner: {electionWinner} \n"
    textFile.write(electionWinnerOutput)

    print(electionWinnerOutput)





    





   












