import random
from database import Database
from titleScreen import TitleScreen

class Game:
    def __init__(self):
        self.quote = ""
        self.movieTitle = ""
        self.randomMovie = []
        self.randomQuote = []
        self.correctIndex = 0
        self.points = 0
        self.incorrect = 0

    # Choose a quote at random and create a list of answer choices 
    def quoteToMovie(self, decadeList):
        movieSet = set()
        randomNum = random.randint(0,len(decadeList)-1)
        self.quote = decadeList[randomNum]['quote']
        answer = decadeList[randomNum]['movie']
        movieSet.add(answer)

        # Choose 3 random movies without repetition
        while len(movieSet) < 4:
            movies = [item["movie"] for item in decadeList]
            self.randomMovie = random.sample(movies, 1)
            movieSet.add(self.randomMovie[0])

        # Shuffle the list to randomize the position of the answer
        self.randomMovie = []

        for i in movieSet:
            self.randomMovie.append(i)
        
        random.shuffle(self.randomMovie)

        # Track the correct answer's position
        self.correctIndex = self.randomMovie.index(answer)
    
    # Choose a quote at random and create a list of answer choices 
    def movieToQuote(self, decadeList):
        movieSet = set()
        randomNum = random.randint(0,len(decadeList)-1)
        self.movieTitle = decadeList[randomNum]['movie']
        answer = decadeList[randomNum]['quote']
        movieSet.add(answer)

        # Choose 3 random quotes without repetition
        while len(movieSet) < 4:
            quotes = [item["quote"] for item in decadeList]
            self.randomQuote = random.sample(quotes, 1)
            movieSet.add(self.randomQuote[0])

        # Shuffle the list to randomize the position of the answer
        self.randomQuote = []

        for i in movieSet:
            self.randomQuote.append(i)
        
        random.shuffle(self.randomQuote)

        # Track the correct answer's position
        self.correctIndex = self.randomQuote.index(answer)
    
    # Print quote and answer choices
    def printQuoteToMovie(self):
        print (f"\"{self.quote}\"", "\n")

        for i in range(4):
            print (f"{i + 1})", self.randomMovie[i])

    # Print movie and answer choices
    def printMovieToQuote(self):
        print (f"\"{self.movieTitle}\"", "\n")
         
        for i in range(4):
            print (f"{i + 1})", self.randomQuote[i])

    # Compare user input to index of the answer
    def checkAnswer(self):
        guess = input("\nEnter your guess as a number 1-4: ")
            
        if guess.isdigit(): 
            if int(guess) == self.correctIndex + 1:
                print("correct!\n", "\n--------------------------------------------------------\n")
                self.points += 1
            else:
                print ("incorrect\n", "\n--------------------------------------------------------\n")
                self.incorrect += 1
        return guess