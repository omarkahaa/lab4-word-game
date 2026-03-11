"""Guess The Word game.

Console Hangman-style game for the EPITA lab.
"""

from __future__ import annotations

import random


WORDS = [
    "python",
    "epita",
    "variable",
    "function",
    "computer",
    "testing",
    "program",
    "random",
]


def choose_secret_word(words: list[str]) -> str:
    """Return a random word from the given list."""
    return random.choice(words)


def normalize_guess(guess: str) -> str:
    """Normalize user input to a single lowercase string."""
    return guess.strip().lower()


def is_valid_guess(guess: str) -> bool:
    """Return True if guess is a single alphabetical character."""
    return len(guess) == 1 and guess.isalpha()


def update_game_state(
    secret_word: str,
    guessed_letters: list[str],
    guess: str,
    lives: int,
) -> tuple[list[str], int]:
    """Return updated guessed letters and lives.

    Pure function:
    - does not mutate the input guessed_letters list
    - does not use globals
    - does not perform any I/O
    """
    new_guessed_letters = guessed_letters.copy()

    if guess not in new_guessed_letters:
        new_guessed_letters.append(guess)

    new_lives = lives
    if guess not in secret_word and guess not in guessed_letters:
        new_lives -= 1

    return new_guessed_letters, new_lives


def get_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    """Return the masked version of the secret word."""
    chars: list[str] = []
    for letter in secret_word:
        if letter in guessed_letters:
            chars.append(letter.upper())
        else:
            chars.append("_")
    return " ".join(chars)


def get_incorrect_guesses(secret_word: str, guessed_letters: list[str]) -> list[str]:
    """Return guessed letters that are not in the secret word."""
    wrong: list[str] = []
    for letter in guessed_letters:
        if letter not in secret_word:
            wrong.append(letter)
    return wrong


def is_won(secret_word: str, guessed_letters: list[str]) -> bool:
    """Return True if all letters of the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def is_lost(lives: int) -> bool:
    """Return True if the player has no lives left."""
    return lives <= 0


def should_continue(secret_word: str, guessed_letters: list[str], lives: int) -> bool:
    """Return True while the current game should continue."""
    return not is_won(secret_word, guessed_letters) and not is_lost(lives)


def display_game(secret_word: str, guessed_letters: list[str], lives: int) -> None:
    """Display the current game state."""
    wrong = get_incorrect_guesses(secret_word, guessed_letters)
    print()
    print(f"Word:   {get_masked_word(secret_word, guessed_letters)}")
    print(f"Lives:  {lives}")
    print(f"Wrong:  {', '.join(wrong) if wrong else '-'}")
    print(f"Guessed:{', '.join(guessed_letters) if guessed_letters else '-'}")
    print()


def ask_guess() -> str:
    """Ask the user for a guess and return the normalized value."""
    return normalize_guess(input("Guess a letter: "))


def play_one_game(words: list[str], max_lives: int = 6) -> None:
    """Play one full game."""
    secret_word = choose_secret_word(words)
    guessed_letters: list[str] = []
    lives = max_lives

    while should_continue(secret_word, guessed_letters, lives):
        display_game(secret_word, guessed_letters, lives)
        guess = ask_guess()

        if not is_valid_guess(guess):
            print("Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters, lives = update_game_state(
            secret_word,
            guessed_letters,
            guess,
            lives,
        )

        if guess in secret_word:
            print("Correct!")
        else:
            print("Wrong!")

    display_game(secret_word, guessed_letters, lives)

    if is_won(secret_word, guessed_letters):
        print(f"You won! The word was '{secret_word.upper()}'.")
    else:
        print(f"You lost! The word was '{secret_word.upper()}'.")


def ask_replay() -> bool:
    """Ask the user whether they want to replay."""
    answer = input("Play again? (y/n): ").strip().lower()
    return answer == "y"


def run_game() -> None:
    """Run the application and support replay."""
    keep_playing = True
    while keep_playing:
        play_one_game(WORDS, 6)
        keep_playing = ask_replay()
    print("Goodbye!")


if __name__ == "__main__":
    run_game()

