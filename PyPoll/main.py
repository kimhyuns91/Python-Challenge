#Import the Modules/CSV File
import pathlib
import csv

#Use module to open csv file location
poll_path = pathlib.Path('Resources/election_data.csv')

#Open as csvfile
with open(poll_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip the header
    header = next(csvreader)

    #Variable
    votes_count = 0
    candidate = []
    candidate_list = []
    county_list = []
    can_vote_count = []
    vote_perc = []

    #Start a loop to iterate through all rows
    for rows in csvreader:

        #Count the number of Votes
        votes_count += 1

        #create separate list for candidate, county
        candidate_list.append(rows[2])
        county_list.append(rows[1])

        #Capture candidates
        if rows[2] not in candidate:
                candidate.append(rows[2])

    #Count the number of votes for each candidate
    for i in range (0, len(candidate)):
        can_vote_count.append(candidate_list.count(candidate[i]))

    #Calculate the percentage for each candidate
    for i in range (0, len(candidate)):
        vote_perc.append(can_vote_count[i]/votes_count*100)

    #Winner of election based oon popular vote
    winner_perc = vote_perc[0]
    winner = candidate[1]
    for i in range (1, len(vote_perc)):
        if winner_perc < vote_perc[i]:
            winner = candidate[i]
    
 #Print out Result
line_4 = []

line_1 = "Election Results"
line_2 = "-------------------------------------"
line_3 = (f"Total Votes: {votes_count}")
for i in range (0, len(candidate)):
    line_4.append(f"{candidate[i]}: {vote_perc[i]}% ({can_vote_count[i]})")
line_5 = f"Winner : {winner}"



print(line_1,"\n",line_2,"\n",line_3,"\n",line_2, sep="")
for i in line_4:
    print(i)
print(line_2,"\n",line_5,"\n",line_2, sep="")

#Create output for result
output_path = pathlib.Path('Analysis/Poll_Analysis.txt')

with open(output_path, 'w') as output:
    output.write("{}\n{}\n{}\n{}\n".format(line_1, line_2, line_3, line_2))
    for i in line_4:
        output.write(i)
        output.write("\n")
    output.write("{}\n{}\n{}\n".format(line_2, line_5, line_2))
