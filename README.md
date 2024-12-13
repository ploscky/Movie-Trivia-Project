# Movie Trivia Project
 
 Authors: [Nada Salib](https://github.com/nadasalib), [Selina Wu](https://github.com/ploscky)

## Project Description

### Motivation
The development of a movie trivia project is compelling because of the opportunity to learn how to connect a database to a working program. This project also appeals to our personal interests and hobbies in film and media; we want to develop something that will have those interests intersect with programming.

### Languages, Tools, and Technologies
The project will primarily use Python for programming the game. We will use SQL for database management and a csv file for the movie data set. Beyond that, GitHub and Visual Studio Code will be used to create this program.
 
### Features
* Categories: User will be given the choice between guessing which movie a quote is from or which character said a quote from one particular movie. For the first category, there are sub-categories for genre.
* Multiple Choice: User will have multiple options for each question to make it easier. 
* Point System Management: Game will stop once a user gets three questions wrong. For each question correct, they get a point and the total points scored will be displayed at the end.
* Graphical User Interface:


### Navigation Diagram
The navigation diagram shows the process of a user 

<img src="navigationDiagram.jpg?raw=true" width="700">


## Class Diagram
<img src="classDiagram.jpg?raw=true" width="700">

Our game will be comprised of 4 main classes, the database, the title screen, the game logic, and the overall gameplay. The Databse class reads data from the csv file and separates it into lists by decade in accordance with the game. The TitleScreen class prints the initial starting page, instructions, and the decade and mode menus. It also returns the decade number and mode that will be used in other classes. The Game class inherits from Database and TitleScreen and essentially matches the correct answer for both modes as well as generates random incorrect options for each question. The Play class inherits from Database, TitleScreen, and Game and organizes the whole game. It also establishes the point system and ends the game when the user gets three questions incorrect.
