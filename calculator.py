def calcs():
    choice = int(input("What operation do you want? Type 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for modulo, 6 for exponents, or 7 for rounded division."))
    number = int(input("Which is the first number you want to do your operations on?"))
    numberTwo = int(input("Which is the second number you want to do your operations on?"))

    if choice == 1:
        answer = number + numberTwo
    elif choice == 2:
        answer = number - numberTwo
    elif choice == 3:
        answer = number * numberTwo
    elif choice == 4:
        answer = number / numberTwo
    elif choice == 5:
        answer = number % numberTwo
    elif choice == 6:
        answer = number ** numberTwo
    elif choice == 7:
        answer = number // numberTwo
    else: 
        answer = "That's not a number, you buffalo!"
    print("The answer is", answer, "why couldn't you do that yourself?")
    return