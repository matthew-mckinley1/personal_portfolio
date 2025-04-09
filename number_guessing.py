def guessing_game():
    import random
    while True:
        guesses = 0
        #Allows the user to choose a range to guess between
        choice = input("What range would you like to guess between?\n1: 1 - 10\n2: 1 - 100\n3: 1 - 1000\n4: Leave\n").strip()
        if choice == '4':
            return
        #Sets between as a list with the range selected
        elif choice == '1':
            between = [1, 10]
        elif choice == '2':
            between = [1, 100]
        elif choice == '3':
            between = [1, 1000]
        else:
            print("Please enter 1, 2, 3, or 4.")
            continue
        #chooses a number between the selected range
        num = random.randint(between[0], between[1])
        while True:
            guess = input("What number would you like to guess?\n").strip()
            try:
                #checks if you entered a number
                int(guess)
            except:
                print(f"Please enter a number between {between[0]} and {between[1]}.")
                continue
            #checks if you entered a number within the right range
            if int(guess) <= between[1] and int(guess) >= between[0]:
                #decides if your number is too high, too low, or accurate
                if int(guess) > num:
                    print("Too high.")
                    guesses += 1
                elif int(guess) < num:
                    print("Too low.")
                    guesses += 1
                elif int(guess) == num:
                    guesses += 1
                    print(f"You got it in {guesses} tries!")
                    return guesses, between
            else:
                print(f"Please enter a number between {between[0]} and {between[1]}.")
                continue
    return