import csv

# csv file name
filename = "movie_quotes.csv"

# reading csv file
with open(filename, 'r') as csvfile:
    # create a csv reader with DictReader
    csvreader = csv.DictReader(csvfile)
    # initialize empty list to store the dictionaries
    data_list = []
    # iterate through each row in the csv file
    for row in csvreader:
        # append each row (as dictionary) to the list
        data_list.append(row)
