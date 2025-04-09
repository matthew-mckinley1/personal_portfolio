from number_guessing import guessing_game as numguess
from pig_latin import start as piglatin
from rock_paper_scissors import rps
from cipher import cipher_changed as cipher
from calculator import calcs
from tictactoe import game as tictactoer

print("This is a portfolio of some programming projects that I have done!\nYou use it by choosing which project you want to see, it gives you information and then asks if you want to play it.")

def main():
    choice = input("Press 1 to go to the number guessing game\nPress 2 to go to the Pig Latin Converter\nPress 3 to go to the Rock, Paper, Scissors game\nPress 4 to go to the Cipher\nPress 5 to go to the Simple Calculator\nPress 6 to go to the Tic Tac Toe game\nPress 7 to exit\n:")
    if choice == "1":
        input("This is a Number Guessing game where you guess the number after choosing the range you want to play in. You start by saying the range you want to go in, and then guessing a number, then it tells you if it is higher or lower than that number. You then have to input another number until you get the correct number! The programming process for this one was pretty easy, but it used quite a few conditionals to compare the numbers. I learned how to use conditionals better to check information and do stuff based off of that information.")
        choice2 = input("Would you like to play this game? (Y/N)").lower()
        if choice2 == "y":
            numguess()
        elif choice2 == "n":
            main()
        else:
            print("That isn't a Y or an N! Try again.")
            main()
    elif choice == "2":
        input("This is a Pig Latin Converter where you put something in and it tells you what that is in pig latin. You input a word or multiple words, and then it tells you what those would be in pig latin. The programming process for this one was a bit tough, because you have to rearrange the word a bit to get it to work. I learned how you can manipulate words and you can really change an input how you want to.")
        choice2 = input("Would you like to play this game? (Y/N)").lower()
        if choice2 == "y":
            piglatin()
        elif choice2 == "n":
            main()
    elif choice == "3":
        input("This is a Rock Paper Scissors game, where you say rock, paper, or scissors, and the computer randomly chooses one and tells you who won. You start by inputting one of the options, and then it tells you what the computer chose and tells you who won. The programming process for this one was a bit annoying, because you have to compare every possible outcome and see who would win. I learned more about using conditionals to check information and compare different things.")
        choice2 = input("Would you like to play this game? (Y/N)").lower()
        if choice2 == "y":
            rps()
        elif choice2 == "n":
            main()
    elif choice == "4":
        input("This is a Cipher that changes words that you put in and shifts them with a value you give. You put in the word or phrase that you want shifted, and then you put in how much you want to shift it by. It also has a feature where you can unshift a word or phrase by an amount if you have a message that is shifted and you want to unshift it. The programming process for this one was interesting. I learned about using ASCII characters to shift and unshift the words, which made the process a bit harder.")
        choice2 = input("Would you like to play this game? (Y/N)").lower()
        if choice2 == "y":
            cipher()
        elif choice2 == "n":
            main()
    elif choice == "5":
        input("This is a Simple Calculator that does simple calculations. You input two numbers and how you want to calculate them together, and calculates that. The programming process for this one was pretty easy, because the math operators that we used are built into python. I learned how to do things to different integers to change them or do math to them.")
        choice2 = input("Would you like to play this game? (Y/N)").lower()
        if choice2 == "y":
            calcs()
        elif choice2 == "n":
            main()
    elif choice == "6":
        input("This is a Tic-Tac-Toe Game that allows you to play Tic-Tac-Toe. You choose what column and row to put your X, and then it puts one in a random place for the O. It checks if someone won, if they didn't then it makes the people go again. The programming process for this one was tough, because you had to see if the board was full, and if people won in any combination of spaces. I learned how to edit lists and used a lot of conditionals to check if somebody had one, and if so, who won.")
        choice2 = input("Would you like to play this game? (Y/N)").lower()
        if choice2 == "y":
            tictactoer()
        elif choice2 == "n":
            main
    elif choice == "7":
        exit()
    else:
        print("That isn't a correct option! Try again.")
        main()

main()