import random
from database import Database
from titleScreen import TitleScreen

class Game:
    def __init__(self):
        self.quote = ""
        self.randomMovie = []
        self.correctIndex = 0

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
    
    # Print quote and answer choices
    def printQuoteToMovie(self):
        print (f"\"{self.quote}\"", "\n")

        for i in range(4):
            print (f"{i + 1})", self.randomMovie[i])

    # Compare user input to index of the answer
    def checkAnswer(self):
        guess = int(input("\nEnter your guess as a number 1-4: "))
        if guess == self.correctIndex + 1:
            print("correct!\n", "\n--------------------------------------------------------\n")
            return True
        else:
            print ("incorrect\n", "\n--------------------------------------------------------\n")
            return False