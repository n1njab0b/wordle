from english_words import english_words_lower_set
import random

def testGuess(guess,seed):
    allwords = sorted([x for x in english_words_lower_set if len(x)==5])
    
    random.seed(seed)    
    magicWord = allwords[random.randint(0,len(allwords))]

    feedBack = ['Green' if magicWord[index] == guess[index] else 'Black' for index in range(5)]
    remaining = [magicWord[index] for index in range(5) if feedBack[index] == 'Black']

    return ['Gold' if feedBack[index] == 'Black' and guess[index] in remaining else feedBack[index] for index in range(5)]      
