
class TitleScreen:
    def __init__(self):
        self.decadeNum = None
        self.mode = None
    
    def printTitleScreen(self):
        print("\n---------- Movie & TV Show Quote Trivia ----------\n")
        print ("1) Instructions\n2) Start game")
        menuInput = input("Enter 1 or 2: ")
        if (menuInput == '1'):
            self.printInstructions()
        elif (menuInput == '2'):
            self.printDecades()

    def printInstructions(self):
        print("\n------------------- Instructions ------------------\n")
        print("- Choose a decade of movies and TV shows to play (1930s - 2010s)")
        print("- Choose a game mode: matching a given movie to the correct quote -OR- matching a given quote to the correct movie")
        print("- The game ends when you get 3 incorrect. You earn 1 point per question, the total will be displayed at the end")
        print("- You can type 'q' at any point to see your points and end the game\n")
        userQuit = input("Type 'q' to quit -OR- any key to begin the game: ")

        if userQuit == 'q':
            self.printTitleScreen()
        else:
            self.printDecades()
    
    # takes in user input as a unique integer to represent each genre
    def printDecades(self):
        print("\n------------------ Decade Menu ------------------\n")

        print("              30s      40s      50s")
        print("              60s      70s      80s")
        print("              90s      00s      10s\n")

        decade = input("Choose a decade as shown above: ")
        decadeNum = decade[0]
        
        # handle negative number exception
        while decadeNum == '-':
            decade = input("Sorry, no numbers below zero. Try again.\n")
            decadeNum = decade[0]
        
        if decadeNum == 'q':
            quit()

        self.printMode()

        # convert first char into int to use as unique decade identifier
        self.decadeNum = int(decadeNum)

    # takes user input (int) for category choice
    def printMode(self):
        print("\n-------------------- Game Mode ------------------\n")
        mode = input("1) Match the movie to the quote?\n2) Match the quote to the movie?\n")
        
        if mode == 'q':
            quit()

        self.mode = int(mode)
        print("\n")