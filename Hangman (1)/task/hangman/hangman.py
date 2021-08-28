import random

words = ["python", "java", "kotlin", "javascript"]
number_of_tries = 8
dash_line = []

print("H A N G M A N")
print()
random_selected_word = words[random.randint(0, len(words) - 1)]
random_selected_word = list(random_selected_word)
len_rand_select_word = len(random_selected_word)

for letters in range(0, len_rand_select_word):
    dash_line += "-"

# print()
while 0 < number_of_tries < 9:
    for x in dash_line:
        print(x, end="")
    print()

    guess_letter = input("Input a letter: ")

    if guess_letter in random_selected_word:
        print()
        for x in range(len_rand_select_word):
            if guess_letter == random_selected_word[x]:
                dash_line[x] = guess_letter
        number_of_tries -= 1
    else:
        number_of_tries -= 1
        print("That letter doesn't appear in the word")
        print()

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
