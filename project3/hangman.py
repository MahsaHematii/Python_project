import random

words_bank = ["tree", "book", "blue", "train", "fish", "woman", "life", "freedome", "iran", "sky"]
users_mistakes = 0

good_chars = []
bad_chars = []
x = random.randint(0, len(words_bank)-1)


word = words_bank[x]
word = word.lower()
# word = random.choice(words_bank)
while users_mistakes < 6:
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i], end=" ")
            
        else:
            print("- ", end="")

        if len(word) == len(good_chars):
            print("You win")
            break

    user_char = input("please write tour guess: ")
    user_char = user_char.lower()

    if len(user_char) == 1:
        if user_char in word:
            good_chars.append(user_char)
            print("✅")
        else:
            bad_chars.append(user_char)
            users_mistakes += 1
            print("❌")

    else:
        print("mse adam vard kon")


if users_mistakes == 6:
    print("Game Over 💀")
