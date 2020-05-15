import random
def hangman():
    word = random.choice(["apple","banana","mango","tiger","rohan","arpit","roop","sanat","jay","vraj"])
    validletter = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "-"+ ""
            if main == word:
                print(main)
                print("You win!!!")
                break
            print("Guess the word:",main)
            guess = input()
             
        if guess in validletter:
            guessmade = guessmade + guess
        else:
            print("Enter the valid charcter")
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 truns left")
                print("----------")
            if turns == 8:
                print("8 truns left")
                print("----------")
                print("    0     ")
            if turns == 7:
                print("7 truns left")
                print("----------")
                print("    0     ")
                print("    |     ")
            if turns == 6:
                print("6 truns left")
                print("----------")
                print("    0     ")
                print("    |     ")
                print("   /     ")
            if turns == 5:
                print("5 truns left")
                print("----------")
                print("    0     ")
                print("    |     ")
                print("   / \    ")
                
            if turns == 4:
                print("4 truns left")
                print("----------")
                print("  \ 0     ")
                print("    |     ")
                print("   / \    ")
            if turns == 3:
                print("3 truns left")
                print("----------")
                print("  \ 0 /    ")
                print("    |     ")
                print("   / \    ")
            if turns == 2:
                print("2 truns left")
                print("----------")
                print("  \ 0 /|    ")
                print("    |     ")
                print("   / \    ")
            if turns == 1:
                print("1 truns left")
                print("Last breath counting,Take care!")
                print("----------")
                print("  \ 0 _|/    ")
                print("    |     ")
                print("   / \    ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("    0 _|    ")
                print("  / | \    ")
                print("   / \    ")
                break








name = input("Enter the name")
print("Welcome",name)
print("----------")
print("Try to guess the word in less than 10 attemps")
hangman()
print() 
