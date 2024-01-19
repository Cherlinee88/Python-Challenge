import csv
from collections import defaultdict

# This function by passing the path to the data
# will read the records and store them in a dictionary
# and return the dictionary
def load_data(path):

    # This dictionary will contain the records from the csv file
    data_dict = {}

    with open(f'{path}', 'r') as file:

        # read the content of the csv file
        csvreader = csv.reader(file)

        # read the header of the data
        header = next(csvreader)

        # looping over the records in the data
        # and add the records to the dictionary
        for index, record in enumerate(csvreader):

            # giving an index to the records in the file
            # and store them in the dictionary
            data_dict[index] = dict(zip(header, record))

    # return the dictionary containing the records in the .csv file
    return data_dict

# This function given the dictionary
# will return the number of votes
def total_votes(data_dict):

    # return the length of the dictionary
    return len(data_dict)

# This function given the dictionary
# will compute the distribution of the votes
# for each candidate
def votes_distribution(data_dict):

    # this dictionary will contain the number of votes
    # for each candidate
    candidate_votes = defaultdict(int)

    # looping over the votes
    for records in data_dict:

        # increment the number of votes for that candidate
        candidate_votes[data_dict[records]['Candidate']] += 1

    # this dictionary will put the total votes and percentage of votes that
    # each candidate could get
    candidate_votes_percentage = defaultdict(dict)

    for candidate in candidate_votes:

        # put the total vote for that candidate
        candidate_votes_percentage[candidate]['total vote'] = candidate_votes[candidate]

        # compute the percentage of votes for that candidate
        candidate_votes_percentage[candidate]['vote percentage'] = round(candidate_votes[candidate] / len(data_dict) * 100, 3)

    # return the total vote and percentage for each candidate
    return candidate_votes_percentage

# This function given the dictionary
# will return the winner of the election
def winner(data_dict):

    # get the distribution of the votes
    votes_dist = votes_distribution(data_dict)

    # stores the winner and the total vote for that winner
    # this variable will store the winner of the election
    candidate_winner, total_vote = None, 0

    # looping over the candidates
    for candidate in votes_dist:

        # check if the number of votes for that candidate
        # is greater than the current winner
        if votes_dist[candidate]['total vote'] > total_vote:

            candidate_winner, total_vote = candidate, votes_dist[candidate]['total vote']

    # return the winner of the election
    return candidate_winner

# This function given the dictionary
# will compute the 
if __name__ == '__main__':

    # Loading the data to a dictionary
    Poll_dict = load_data('Resources/election_data.csv')

    with open('analysis/PyPoll.txt', 'w') as out_file:

        out_file.write('Election Results\n')
        out_file.write('-' * 30 + '\n')
        out_file.write(f'Total Votes: {total_votes(Poll_dict)}\n')
        out_file.write('-' * 30 + '\n')

        # getting the distribution of the votes
        votes_dist = votes_distribution(Poll_dict)

        # looping over the candidates and print their information
        for candidate in votes_dist:

            out_file.write(f'{candidate}: {votes_dist[candidate]["vote percentage"]}% ({votes_dist[candidate]["total vote"]})\n')

        out_file.write('-' * 30 + '\n')
        # getting the winner of the election
        out_file.write(f'Winner: {winner(Poll_dict)}\n')
        out_file.write('-' * 30 + '\n')
