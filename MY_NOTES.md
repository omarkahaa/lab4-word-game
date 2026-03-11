

## `MY_NOTES.md`
```md
# My Original Thinking

## App States
- Playing
- Won
- Lost
- Replay choice after game ends

## App Variables
- `secret_word`: chosen word
- `guessed_letters`: all guessed letters
- `wrong_guesses`: guessed letters not in the word
- `lives`: remaining turns
- `max_lives`: starting number of turns
- `masked_word`: visible version of the word

## App Rules and Invariants
- One guess must be one letter
- Input should be case-insensitive
- Duplicate guesses should not reduce lives twice
- Correct guesses reveal all matching positions
- Wrong guesses reduce lives by one
- The game ends on full word reveal or zero lives
- The visible word length must always match the secret word length

## App Bugs
- Empty input
- More than one character
- Non-letter input
- Repeated guesses
- Off-by-one error on lives
- Incorrect handling of repeated letters in the secret word
- Guess accepted after game already ended

# Copilot Suggestions

- Separate logic and UI functions
- Keep `update_game_state` pure
- Use a helper function to build the masked word
- Validate input before updating the game state
- Track incorrect guesses separately from display logic
- Ask Copilot for review and test ideas after writing the minimal core