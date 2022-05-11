import wordle
import datetime

def main():
    seed = int(((datetime.datetime.utcnow()) - datetime.datetime(1970,1,1,0,0,0)) / datetime.timedelta(hours=1))
    success=False
    while (not success):
        guess=input("What is your wordle guess? ")
        response=wordle.testGuess(guess,seed)
        print(response)
        success=all(i=='Green' for i in response)
    print("Congratulations!")

main()