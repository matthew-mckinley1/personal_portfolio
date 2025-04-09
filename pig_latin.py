def start():
    def piggy(word):
        firstlet=word[0]+"ay"
        word = word[1:]
        return(word+firstlet).title()
    print(piggy(word = input("What would you like to convert to pig latin?")))