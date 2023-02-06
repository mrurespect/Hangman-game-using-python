import random
print('H A N G M A N\n')
list=["python","java","swift","javascript"]
word= random.choice(list)
size = len(word)
str = "-"
str = str*size
print(str)
attempt = 8
compteur =0
Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while word != str :
    letter = input('Input a letter:')
    if len(letter) != 1:
        print("Please, input a single letter.")
    elif letter not in Alphabet:
        print("Please, enter a lowercase letter from the English alphabet.")
    elif letter not in word and letter not in str :
            attempt-=1
            print("That letter doesn't appear in the word.")
    elif letter  in str :
        attempt-=1
        print("You've already guessed this letter.")
    else :
        for j in range(size):
            if word[j]== letter :
                pos = j
                str = str[:pos] + letter + str[pos + 1:]
    if attempt ==0 :
                print()
                print("You lost!")
                break
    print()
    print(str)
else :
    print(f"You guessed the word {word}!\nYou survived!")
