#   import os library to standardize file path across various os and cs library to open and close csv files
import os
import csv

#   Define file path for source file
file_path = os.path.join('Resources', 'election_data.csv')

#   create empty strings to populate relevant results later in analysis
candidate_list = []
candidate_shortlist = []
candidate_votecount = []
candidate_votepercent = []


#   open source csv file as read only and specify how file is delimited and extract applicable data to lists before closing
with open(file_path, 'r') as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter = ',')

#   skip header in csv file so does not act as noise in analysis
    header = next(csv_reader)

#   populate list of candidates from csv table to prior defined string
    for row in csv_reader:
        candidate_list.append(row[2])


#   find the length of the list. This will tell you how many voter entries there are, hence total vote count.
vote_count = len(candidate_list)

#   populate the distinct list of candidates in the prior defined string
for i in candidate_list: 
    if i not in candidate_shortlist: 
        candidate_shortlist.append(i)

#   Begin counter at 0
counter = 0
#   for each candidate as defined in candidate_list, return the total number of votes into the prior defined string
for i in candidate_shortlist:
    candidate_vote_count = candidate_list.count(i)
    candidate_votecount.append(candidate_vote_count)
    counter += 1

#   for each candidate vote count in candidate_votecount string, find its proportion of votes as a factor of total votes (vote_count)
for i in candidate_votecount:
    candidate_votepercent.append("{:.3%}".format(i/vote_count))
    counter += 1


#   zip the three lists to create a tuple
consolidated_list = list(zip(candidate_shortlist, candidate_votepercent, candidate_votecount))

#   zip the candidate and vote counts list to create a key, value dictionary in order to determine the candidate with the highest votes
candidate_dict = dict(zip(candidate_shortlist, candidate_votecount))
winner = max(candidate_dict, key=candidate_dict.get)


# define variable that will contain string to print to terminal and text file
election_results = (
    f"```text\n"
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {vote_count}\n"
    f"-------------------------\n"
    f'{consolidated_list[0][0]}: {consolidated_list[0][1]} ({consolidated_list[0][2]})\n'
    f'{consolidated_list[1][0]}: {consolidated_list[1][1]} ({consolidated_list[1][2]})\n'
    f'{consolidated_list[2][0]}: {consolidated_list[2][1]} ({consolidated_list[2][2]})\n'
    f'{consolidated_list[3][0]}: {consolidated_list[3][1]} ({consolidated_list[3][2]})\n'
    f"-------------------------\n"
    f'Winner: {winner}\n'
    f"-------------------------\n"
    f" ```\n"
    )


print(election_results)


output_path = os.path.join('Analysis', 'election_results.txt')
with open(output_path, 'w') as txt_file:
    txt_file.write(election_results)



 

