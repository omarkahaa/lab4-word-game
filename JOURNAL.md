# JOURNAL

## 2026-03-11 - Project setup and preparation
- Opened the `lab4-word-game` repository.
- Updated the `.github` folder using the material from `lab1-hello-world`.
- Activated the journal logger and instruction workflow in Copilot.

## 2026-03-11 - Design thinking before coding
- Wrote initial notes in `MY_NOTES.md`.
- Identified game states: playing, won, lost.
- Listed key variables such as secret word, guessed letters, and lives.
- Thought about rules, invariants, and edge cases before implementation.

## 2026-03-11 - Copilot ask phase
- Asked Copilot about:
  - app states
  - app variables
  - app rules and invariants
  - possible bugs in Hangman implementations
- Reviewed the suggestions and kept only the ideas that matched the exercise.

## 2026-03-11 - Minimal core implementation
- Removed the old Fibonacci demo from `main.py`.
- Implemented the minimal core function:
  - `update_game_state(secret_word, guessed_letters, guess, lives)`
- Kept the function pure and without global variables.

## 2026-03-11 - Review and documentation
- Reviewed the code structure and improved readability.
- Added concise documentation to functions in `main.py`.
- Updated README and report files to match the current state of the project.

## 2026-03-11 - Testing and validation
- Manually tested:
  - correct guesses
  - incorrect guesses
  - repeated guesses
  - invalid input
  - win / lose behavior
  - replay without restarting
- Confirmed the game runs from `python3 main.py`.
