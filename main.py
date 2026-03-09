"""Simple demo module for Fibonacci.

Provides a straightforward recursive implementation of Fibonacci numbers.

Functions
---------
fib(n):
    Return the n-th Fibonacci number where fib(0) == 0 and fib(1) == 1.

When run as a script, prints fib(0..10).
"""

import sys


def fib(n: int) -> int:
    """Return the n-th Fibonacci number (recursive).

    Parameters
    - n: non-negative integer

    Returns
    - int: the n-th Fibonacci number

    Raises
    - ValueError: if n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def _demo():
    """Print the first 11 Fibonacci numbers."""
    for i in range(11):
        print(f"fib({i}) = {fib(i)}")


def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:
    """Update the Hangman game state.

    Parameters
    - secret_word: the word to guess
    - guessed_letters: list of letters already guessed
    - guess: the new guessed letter
    - lives: remaining lives

    Returns
    - tuple (new_guessed_letters, new_lives)
    """

    new_guessed_letters = guessed_letters.copy()

    if guess not in new_guessed_letters:
        new_guessed_letters.append(guess)

    if guess not in secret_word:
        lives -= 1

    return new_guessed_letters, lives


if __name__ == "__main__":
    # If a single integer argument is provided, print fib for that value.
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Please provide an integer.")
            sys.exit(1)

        try:
            print(fib(n))
        except ValueError as e:
            print(e)
            sys.exit(1)
    else:
        _demo()