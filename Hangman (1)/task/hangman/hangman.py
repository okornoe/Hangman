import random

words = ["python", "java", "kotlin", "javascript"]
number_of_tries = 8
dash_line = []

print("H A N G M A N\n")
random_selected_word = words[random.randint(0, len(words) - 1)]
random_selected_word = list(random_selected_word)
len_rand_select_word = len(random_selected_word)

for letters in range(0, len_rand_select_word):
    dash_line += "-"

while 0 < number_of_tries < 9:
    print(''.join(str(i) for i in dash_line))
    guess_letter = input("Input a letter:")

    if guess_letter in random_selected_word:
        if guess_letter in dash_line:
            number_of_tries -= 1
            print("No improvements")
            if number_of_tries == 0:
                print("You lost!")
            print()

        else:
            print()
            for x in range(len_rand_select_word):
                if guess_letter == random_selected_word[x]:
                    dash_line[x] = guess_letter
                if dash_line == random_selected_word and number_of_tries > 0:
                    number_of_tries = 0
                    print(''.join(str(i) for i in dash_line))
                    print("You guessed the word!")
                    print("You survived!")

    else:
        number_of_tries -= 1
        print("That letter doesn't appear in the word")
        if number_of_tries == 0:
            print("You lost!")
        print()
