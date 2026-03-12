# My Original Thinking

## States
- playing
- won
- lost
- replay choice at the end

## Variables
- `secret_word`: the word to guess
- `guessed_letters`: letters the player already tried
- `wrong_guesses`: wrong letters
- `lives`: how many tries are left
- `max_lives`: starting number of tries
- `masked_word`: what the player sees

## Rules I wanted to keep
- one guess should be one letter only
- uppercase and lowercase should be treated the same
- repeating the same guess should not remove a life again
- correct guesses should reveal every matching letter
- wrong guesses should remove one life
- the game should stop when the word is complete or lives reach zero
- the displayed word should always match the real word length

## Bugs I wanted to avoid
- empty input
- typing more than one character
- typing something that is not a letter
- repeated guesses
- losing one life too many or too early
- repeated letters not showing correctly
- still accepting guesses after the game is over

## Ideas from Copilot that were useful
- separate the game logic from input and display
- keep `update_game_state` pure
- use a helper function to build the masked word
- validate input before changing the game state
- keep wrong-guess tracking separate from display
- use Copilot again later to review the structure