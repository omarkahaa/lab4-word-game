# My Original Thinking

## States
- playing (normal mode)
- auto playing (computer guesses letters)
- won
- lost
- return to mode selection at the end

## Variables
- `secret_word`: the word to guess
- `guessed_letters`: letters that were already tried
- `wrong_guesses`: wrong letters guessed so far
- `lives`: how many tries are left
- `max_lives`: starting number of tries
- `masked_word`: what is displayed to show progress
- `mode`: whether the game is played by the user or automatically

## Rules I wanted to keep
- one guess should always be one letter
- uppercase and lowercase should be treated the same
- repeating the same guess should not remove a life again
- correct guesses reveal all matching letters in the word
- wrong guesses remove one life
- the game stops when the word is completed or when lives reach zero
- the displayed word must always match the real word length
- the auto player must never suggest a letter that was already guessed

## Bugs I wanted to avoid
- empty input
- typing more than one character
- typing something that is not a letter
- repeated guesses by the user
- repeated guesses by the auto player
- losing one life too many or too early
- letters not appearing correctly in the masked word
- the game continuing after it should have ended
- the auto mode getting stuck or guessing the same letter forever

## Design decisions
- keep the original game logic unchanged as much as possible
- add a separate auto-play mode instead of modifying the normal one
- reuse the same functions (`update_game_state`, `display_game`, etc.)
- generate automatic guesses using the alphabet and filtering already guessed letters
- return to the mode selection menu after a game ends

## Ideas from Copilot that were useful
- separate game logic from input and display
- keep `update_game_state` pure
- use helper functions like `get_masked_word`
- reuse existing functions instead of duplicating logic
- generate auto guesses from remaining letters so repeats cannot happen
- review the code structure after implementing auto-play