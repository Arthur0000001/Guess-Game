n=65
print("I'm thinking of a number! Try to guess the number I'm thinking of")
while True:
    m=int(input("Enter your Guess: "))
    if n==m:
        print("BINGO! You Won")
        break
    elif m>n-3 and m<n+3:
        print("Almost There")
    elif m>n-10 and m<n+10:
        print("Very close! Keep guessing")
    elif n<m:
        print("Too High! Guess again")
        l=(input("Would you like to play again (y/n)"))
        if l=='n':
            print("Thank you for playing")
            break
    elif n>m:
        print("Too Low! Guess again")
        l=(input("Would you like to play again (y/n)"))
        if l=='n':
            print("Thank you for playing")
            break
input()    
