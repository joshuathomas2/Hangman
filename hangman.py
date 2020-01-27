import random
import string


class Hangman:
    def __init__(self):
        self.user_input = ""
        self.secret_word = ""
        self.word_file = ""
        self.hangman_file = ""
        self.word_progress = []
        self.lives = 0
        self.words = []
        self.used_letters = []
        self.available_letters = list(string.ascii_lowercase)
        self.in_game = False
        self.complete_word = False

    def start(self):
        self.in_game = True
        self.lives = 10
        self.word_file = open("text_files/words.txt", "r")
        self.words = self.word_file.readlines()
        self.secret_word = random.choice(self.words)[:-1]
        self.word_file.close()

        for x in range(len(self.secret_word)):
            self.word_progress.append("_")

        while self.in_game:
            print("========================================")
            print(f"Available letters: {self.available_letters}")
            print(f"Used letters: {self.used_letters}")
            print(f"Secret word: {self.secret_word}")
            print(f"Progress: {self.word_progress}")
            print(f"You have {self.lives} lives remaining.")
            print("========================================")
            self.user_input = input("What letter would you like to guess? ")

            if self.user_input.isalpha() and len(self.user_input) == 1 and self.user_input in self.available_letters:
                print("That input was valid.")
                self.available_letters.remove(self.user_input)
                self.used_letters.append(self.user_input)

                if self.user_input in self.secret_word:
                    print("That letter was in the secret word!")
                    self.hangman_file = open(f"text_files/hangman_{self.lives}.txt", "r")
                    for line in self.hangman_file:
                        print(line)
                    self.hangman_file.close()
                else:
                    self.lives -= 1
                    print("That letter was not in the secret word. You lost a life!")
                    self.hangman_file = open(f"text_files/hangman_{self.lives}.txt", "r")
                    for line in self.hangman_file:
                        print(line)
                    self.hangman_file.close()

                for x in range(len(self.secret_word)):
                    if self.user_input == self.secret_word[x]:
                        self.word_progress[x] = self.user_input
            else:
                print("That input was not valid. Please enter one letter that has not been used.")

            if "_" not in self.word_progress:
                self.complete_word = True

            if self.complete_word:
                print(f"You guessed the word! The word was {self.secret_word}. You win!")
                self.user_input = input("Would you like to play again? (Y/N) ").upper()
                if self.user_input == "N" or self.user_input == "NO":
                    self.in_game = False
                else:
                    self.restart()

            if self.lives == 0:
                print(f"The secret word was {self.secret_word}")
                self.user_input = input("You ran out of lives! Would you like to play again? (Y/N) ").upper()
                if self.user_input == "N" or self.user_input == "NO":
                    self.in_game = False
                else:
                    self.restart()

    def restart(self):
        self.user_input = ""
        self.secret_word = ""
        self.word_file = ""
        self.word_progress = []
        self.lives = 0
        self.words = []
        self.used_letters = []
        self.available_letters = list(string.ascii_lowercase)
        self.in_game = False
        self.complete_word = False
        self.start()


def main():
    hangman = Hangman()
    hangman.start()


if __name__ == "__main__":
    main()
