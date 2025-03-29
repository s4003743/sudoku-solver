# SUDOKU SOLVER
A recursive backtracking algorithm that solves sudoku. This was for a CS50x final project, the demo video may be slightly different to the current project but all functionality remains the same.
#### [Video Demo](https://youtu.be/MEkQLvBz24E)

# USAGE
To run the website locally, type the following into the terminal: "python -m flask run". This program should now be running on port 5000. Note that this is for development use and not for official deployment.

# OVERVIEW:
As seen below, this program although relatively simple in nature does contain a deceptive amount of complexity and moving parts so to speak. In my spare time I regularly play games such as chess and the like on my mobile phone. One such game I enjoy playing despite my incompetencies at completing the more difficult challenges is sudoku. Most apps that I use to play sudoku don’t always contain a feature for the player to auto solve the original puzzle and thus see where they went wrong. Thus I sought to create a program that would aid my journey as a developing (although currently low-skilled) sudoku player. As an overview and summary of the program’s goal, it is to accept input from the user which will be a sudoku puzzle as provided by the many other websites that are similar to those that I would use. It would then use some kind of algorithm to solve the puzzle via brute force. This would only happen however, when the program has already checked that the provided puzzle’s starting layout was indeed legal by the standards and rules of traditional sudoku (that being each column, row and square must contain all the numbers 1 through 9 such that each is unique to its own row, column and square). Then the solution would be transmitted to the user via some kind of web application. If no solution can be found, report such findings to the user additionally.


# HTML:
This part of the code is rather simple if you forgo analysis on the Jinja framework. Essentially it consists of 3 major parts; the title/banner, the sudoku board itself and the submit button tucked underneath. I went for a pragmatic design/structure so as not to involve too many moving parts that could affect the efficacy of the central components of the program (as outlined in the overview. For simplicity’s sake (this will be expanded on in the CSS part of this description of the program)


# PYTHON:
This is where the majority of the logic is contained within this program. Ignoring the flask components (essentially everything tying this file to the rest of the repository) we see the fundamental algorithm designed to solve the sudoku problem as provided my the user. IT employs a recursive backtracking algorithm. In essence, it will scan from the top left right and then down each row for an empty slot (here empty slots are marked as -1 but could really be any number outside of the ones that are actually in use by the game). The main function solve_sudoku employs the aid of a couple of helper functions, here named as is_valid_guess() and fin_empty(). Both are relatively self explanatory; the former checking whether a particular guess would follow the rules of sudoku and thus give permission to the main function to mutate the original puzzle and the latter simply scanning the board until it finds an integer marking that particular spot as empty and awaiting input from the solver. The solver itself will continue calling itself (hence the descriptor of recursive) until no empty spaces are left. If it runs out of guesses for a particular square (1 - 9 all don’t work) then that must mean the program made an error in one or more of the previous steps and thus marks the current spot empty again (reverting the board by one step) and trying again hence the descriptor of backtracking. Once the function is complete, it will either render a verdict of true if it was able to solve the provided puzzle or false meaning that the puzzle is impossible to solve while conforming to the rules provided by sudoku.


# CSS:
This part of the project was relatively simple. Since I wasn’t too interested in the styling of the project. I decided that it would be more efficient as the programmer of this web-page to simply write the styling in-line rather than in its own section or another file. I used a videogame colour palette from lospec to subtly style the page while also not detracting from the utilitarian atmosphere I was seeking from the final product.


# FLASK/JINJA:
This was the trickiest part for me only because of the fact that I have never done anything like this prior to taking on this course. There was a significant learning curve however I managed to simplify it down so I could better implement the code. Essentially, if it's the first time loading the page I have designed a placeholder sudoku puzzle that will appear for the user to better understand how to interact with the program. If the user then presses the solve button, I use a for loop to capture the information into a 2 dimensional array and put that into the solve_sudoku function. In terms of the Jinja framework, it essentially involved adding all  the input fields for the sudoku grid as an iterating loop rather than me doing it by hand. The code comes out much cleaner that way.


