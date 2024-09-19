import csv

class Database:
    # initializes decade lists as empty lists
    def __init__(self):
        self.thirties = []
        self.fourties = []
        self.fifties = []
        self.sixties = []
        self.seventies = []
        self.eighties = []
        self.nineties = []
        self.aughts = []
        self.tens = []

    # creates list of dictionaries for the movies in database
    def createDataList(self):
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
        return data_list

    # separates data_list into their individual attributes (by decade)
    def separateList(self, data_list):
        for item in data_list:
            if item['year'][2] == '3':
                self.thirties.append(item)
            elif item['year'][2] == '4':
                self.fourties.append(item)
            elif item['year'][2] == '5':
                self.fifties.append(item)
            elif item['year'][2] == '6':
                self.sixties.append(item)
            elif item['year'][2] == '7':
                self.seventies.append(item)
            elif item['year'][2] == '8':
                self.eighties.append(item)
            elif item['year'][2] == '9':
                self.nineties.append(item)
            elif item['year'][2] == '0':
                self.aughts.append(item)
            elif item['year'][2] == '1':
                self.tens.append(item)



