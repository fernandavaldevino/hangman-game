import random
from os import system, name

import words, constants, hangman_draw

# screen cleaning function after each run
def clean_screen():
    if name == 'nt':        # Windows
        _ = system('cls')
    else:                   # Linux and MacOS
        _ = system('clear')


def hangman():
    clean_screen()
    print(constants.WELCOME_TEXT)

    word = random.choice(words.WORDS).upper()
    discovered_letters = ['_' for letter in word]
    attempts = 5
    wrong_letters = []
    wrong_level = 0

    print(f'\n{hangman_draw.draw_level[wrong_level]}\n')

    while attempts > 0:
        print(' '.join(discovered_letters))
        print(f'\nRemaining attempts: {attempts}')
        print('\nWrong letters: ', ' '.join(wrong_letters))

        attempt = input('\nEnter a letter: ').upper()

        if attempt in word:
            print(f'\n{hangman_draw.draw_level[wrong_level]}\n')
            index = 0
            for letter in word:
                if attempt == letter:
                    discovered_letters[index] = letter
                index += 1
        else:
            wrong_level += 1
            print(f'\n{hangman_draw.draw_level[wrong_level]}\n')
            print
            attempts -= 1
            wrong_letters.append(attempt)

        if '_' not in discovered_letters:
            print('\nY O U   W I N !')
            print(f'\nThe word was {word.upper()}\n\n')
            break
            

    if '_' in discovered_letters:
        print('\nY O U   L O S E !')
        print(f'\nThe word was {word.upper()}\n\n')



if __name__ == '__main__':
    hangman()