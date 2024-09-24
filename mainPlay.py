from database import Database
from titleScreen import TitleScreen
from game import Game

class Play:
    def __init__(self):
       self.data = Database()
       self.title = TitleScreen()
       self.play = Game()

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

        self.title.printTitleScreen()
        mode = self.title.mode
        decade = self.title.decadeNum

        # Keep giving questions depending on mode on decade until user gets 3 incorrect
        while self.play.incorrect < 3:
            if mode == 1:
                self.play.movieToQuote(self.matchDecade(decade))
                self.play.printMovieToQuote()
            else:
                self.play.quoteToMovie(self.matchDecade(decade))
                self.play.printQuoteToMovie()
            
            isQuit = self.play.checkAnswer()
            if isQuit == 'q':
                self.printPoints()
            # Print out number of incorrect answers so far
            print(f"Incorrect Answers: {self.play.incorrect}\n")
        print("3 Incorrect. Game Over!")
        self.printPoints()
        
    def printPoints(self):
        print("\n------------------ Total Points ------------------")
        print("Points Earned:", self.play.points)
        userQuit = input("Press 'q' to quit or any key to play again\n")
        
        if userQuit == 'q':
            quit()
        else:
            self.play.incorrect = 0
            self.pointSystem()


play1 = Play()
play1.pointSystem()