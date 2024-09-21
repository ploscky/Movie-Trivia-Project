from database import Database
from titleScreen import TitleScreen
from game import Game

class Play:
    def __init__(self):
       self.data = Database()
       self.title = TitleScreen()

    # Matches the decade number in the parameter to one of the decades lists
    def matchDecade(self, decade):
        list = self.data.createDataList()
        self.data.separateList(list)
        if decade == 3:
            return self.data.thirties
        elif decade == 4:
            return self.data.fourties
        elif decade == 5:
            return self.data.fifties
        elif decade == 6:
            return self.data.sixties
        elif decade == 7:
            return self.data.seventies
        elif decade == 8:
            return self.data.eighties
        elif decade == 9:
            return self.data.nineties
        elif decade == 0:
            return self.data.aughts
        elif decade == 1:
            return self.data.tens

    # Keeps track of number of points earned and incorrect answers
    def pointSystem(self):
        # Create Game object
        play = Game()
        category = self.title.printCategory()
        decade = self.title.printDecades()

        # Keep giving questions depending on category on decade until user gets 3 incorrect
        while play.incorrect < 3:
            if category == 1:
                play.movieToQuote(self.matchDecade(decade))
                play.printMovieToQuote()
            else:
                play.quoteToMovie(self.matchDecade(decade))
                play.printQuoteToMovie()
            play.checkAnswer()
            # Print out number of incorrect answers so far
            print(f"Incorrect Answers: {play.incorrect}\n")
        print("3 Incorrect. Game Over!")
        print("Points Earned:", play.points)