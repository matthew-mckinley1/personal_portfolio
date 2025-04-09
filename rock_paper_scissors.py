import random
def rps():
    score = 0
    cpuscore = 0
    userChoice = input("Rock, Paper, or Scissors?")
    cpuChoice = random.randint(1, 3)
    if cpuChoice == 1:
        cpuChoice = "rock"
    if cpuChoice == 2:
        cpuChoice = "paper"
    if cpuChoice == 3:
        cpuChoice = "scissors"
    print(cpuChoice)
    if cpuChoice == userChoice:
        print("You tied!")
        return
    elif cpuChoice == "rock" and userChoice == "paper":
        print("You won!")
        score += 1
        return
    elif cpuChoice == "rock" and userChoice == "scissors":
        print("You lost.")
        cpuscore += 1
        return
    elif cpuChoice == "paper" and userChoice == "rock":
        print("You lost.")
        cpuscore += 1
        return
    elif cpuChoice == "paper" and userChoice == "scissors":
        print("You won!")
        score += 1
        return
    elif cpuChoice == "scissors" and userChoice == "rock":
        print("You won!")
        score += 1
        return
    elif cpuChoice == "scissors" and userChoice == "paper":
        print("You lost.")
        cpuscore += 1

        return
    else:
        print("Sorry, please enter an input in all lowercase.")
        rps()
    print("Your score is", score)
    print("CPU score is", cpuscore)