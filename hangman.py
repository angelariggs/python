import random

def get_random_word():
    words = ["pizza", "burgers", "chocolate"]
    word = words[random.randint(0, len(words)-1)]
    return word

def show_word(word):
    for character in word:
        print(character, " ", end="")
    print("")

def get_guess():
    print("Enter a letter: ")
    return input()

def process_letter(letter, secret_word, blanked_word):
    result = False

    # range is 0-indexed
    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            result = True
            blanked_word[i] = letter

    return result

def print_strikes(number_of_strikes):
    for i in range (0, number_of_strikes):
        print ("X ", end="")
    print("")

def play_word_game():
    strikes = 0
    max_strikes = 3
    playing = True

    word = get_random_word()
        # list() converts a string to a list; e.g. "word" > ["w", "o", "r", "d"[
    blanked_word = list("_" * len(word))

    while playing:
        show_word(blanked_word)
        letter = get_guess()
        # NOTE: 'word' refers to the var within play_word_game
        found = process_letter(letter, word, blanked_word)

        if not found:
            strikes +=1
            print_strikes(strikes)

        if strikes >= max_strikes:
            playing = False

        if not "_" in blanked_word:
            playing = False

    if strikes >= max_strikes:
        print("You didn't guess the word.")
    else:
        print("You won!")

print ("Game started")
play_word_game()
print("Game over")