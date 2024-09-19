
class TitleScreen:
    def __init__(self) -> None: pass
    
    # takes in user input as a unique integer to represent each genre
    def printDecades(self):
        print("--------------- Movie Quote Trivia ---------------\n")

        print("              30s      40s      50s")
        print("              60s      70s      80s")
        print("              90s      00s      10s\n")

        decade = input("Choose a decade as shown above: ")
        decadeNum = decade[0]
        
        # handle negative number exception
        while decadeNum == '-':
            decade = input("Sorry, no numbers below zero. Try again.\n")
            decadeNum = decade[0]
        
        # convert first char into int to use as unique decade identifier
        decadeNum = int(decadeNum)
        
        print("\n")
        return decadeNum

    # takes user input (int) for category choice
    def printCategory(self):
        print("------------------ Category Menu -----------------\n")
        category = int(input("1) Match the movie to the quote?\n2) Match the quote to the movie?\n"))
        return category