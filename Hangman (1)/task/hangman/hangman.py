import random

words = ["python", "java", "kotlin", "javascript"]
number_of_tries = 0
dash_line = []
already_guessed_letters = []

print("H A N G M A N\n")
random_selected_word = words[random.randint(0, len(words) - 1)]
random_selected_word = list(random_selected_word)
len_rand_select_word = len(random_selected_word)

while True:
    start_quit_game = input("Type \"play\" to play the game, \"exit\" to quit:")
    if start_quit_game == "exit":
        exit(0)
        break

    while start_quit_game != "play" and start_quit_game != "exit":
        start_quit_game = input("Type \"play\" to play the game, \"exit\" to quit:")
        if start_quit_game == "exit":
            exit(0)
            break

    dash_line.clear()
    already_guessed_letters.clear()
    number_of_tries = 8

    for letters in range(0, len_rand_select_word):
        dash_line += "-"

    while 0 < number_of_tries < 9:
        print(''.join(str(i) for i in dash_line))
        guess_letter = input("Input a letter:").strip()

        if len(guess_letter) > 1 or len(guess_letter) == 0:
            print("You should input a single letter")
            print()
        elif guess_letter.isupper() or guess_letter.isnumeric() or not guess_letter.isalnum():
            print("Please enter a lowercase English letter")
            print()

        else:
            if guess_letter in random_selected_word:
                if guess_letter in dash_line:
                    print("You've already guessed this letter")
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
                if guess_letter in already_guessed_letters:
                    print("You've already guessed this letter")
                    print()
                else:
                    number_of_tries -= 1
                    already_guessed_letters.append(guess_letter)
                    print("That letter doesn't appear in the word")
                if number_of_tries == 0:
                    print("You lost!")
                print()





