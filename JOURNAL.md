# JOURNAL

I decided to restart the project process because I wanted the journal to reflect more clearly how I used Copilot while building the game.

I did not want to ask for the whole game in one shot, so I started with a very small prompt.

Prompt:
Help me build a simple Python terminal word guessing game for a beginner. Only do the first step for now: create a small list of words, choose one random secret word, create a masked version of it using underscores, and print it. Keep it simple and do not add input, loops, or full game logic yet.

Copilot gave me a basic starting point with:
- a small word list
- a random secret word
- a masked version with underscores

That was enough to get started. I kept that general idea in the final code with the `WORDS` list and the `choose_secret_word()` function.

---

After that, I wanted the game to actually ask the player for something.

Prompt:
Add the next step to word_game.py: ask the player to enter one letter, store it in a variable, normalize it to lowercase, and print it back to confirm the input. Do not add loops or full game logic yet.

Copilot added one guessed-letter input and normalized the input to lowercase.

This was useful because the program stopped being just a display and became interactive. Later, that idea became `normalize_guess()` and `ask_guess()` in the final code.

---

Next, I wanted the game to react to the guess instead of only printing it back.

Prompt:
Extend the Python word guessing game so that it checks if the guessed letter is in the secret word. If the letter exists in the word, print a message saying it is correct. Otherwise print that the guess is wrong. Do not implement loops or full game mechanics yet.

Copilot added a simple check to see whether the guessed letter was in the secret word, and it printed either a correct or wrong message.

This was a good next step, but it was still basic because the game only gave text feedback. The final version kept this idea with the `"Correct!"` and `"Wrong!"` messages.

---

Then I wanted the visible word itself to change when the player guessed correctly.

Prompt:
Extend word_game.py so that when the guessed letter is in the secret word, the masked word is updated to reveal that letter in all the correct positions. Keep it simple and still limited to one guess for now. Do not add loops for repeated turns yet.

Copilot pushed the code in that direction by updating the visible word after a correct guess.

That was important because the program started to feel more like a real word guessing game. In the final version, I handled this more cleanly with `get_masked_word(secret_word, guessed_letters)`.

---

Once the word could update, I needed the game to continue for more than one turn.

Prompt:
Extend word_game.py so the game can handle multiple guesses in a loop. Keep asking the player for a letter until the whole word is guessed. Do not add lives or lose conditions yet.

Copilot added a loop so the player could keep guessing until the whole word was revealed.

This made it feel like an actual playable round. Later, I cleaned that logic up in the final version by using `should_continue(secret_word, guessed_letters, lives)` inside `play_one_game()`.

---

After that, I wanted better state tracking.

Prompt:
Improve word_game.py by tracking guessed letters so the player can see what was already tried, and make sure repeated guesses do not reduce lives twice or create inconsistent state. Keep the structure simple.

Copilot added guessed-letter tracking, duplicate detection, and safer handling for repeated guesses.

This was one of the more useful steps because the game now had to deal with actual state and not only simple input/output. In the final version, I kept `guessed_letters`, duplicate checks, and also separated incorrect guesses with `get_incorrect_guesses()`.

---

Next I wanted the player to be able to lose, not only win.

Prompt:
Extend word_game.py by adding a lives system for wrong guesses. Start with a fixed number of lives, decrease lives only when the guessed letter is not in the secret word, and stop the game when lives reach zero. Keep the existing guessed-letter tracking.

Copilot added a fixed number of lives and reduced lives only for wrong guesses.

This completed the basic game flow. In the final version, I kept `lives`, added `is_lost()`, and made the update cleaner in `update_game_state()`.

---

At that point the game worked, but the code was getting messy, so I wanted to clean it up.

Prompt:
Refactor word_game.py to make the structure cleaner by separating game logic from display and input. Keep the same behavior, but introduce small helper functions where useful, especially for masked-word display, input normalization/validation, win/lose checks, and replay handling.

Copilot suggested splitting the code into smaller helper functions with clearer roles.

This strongly influenced the final structure. The final code ended up with separate functions for:
- choosing the word
- normalizing and validating input
- updating the game state
- building the masked word
- checking incorrect guesses
- checking win / lose conditions
- displaying the game state
- asking for replay
- running one game and replaying again

This was probably the most useful structural step, because it made the program easier to read and easier to control.

---

After that, I used Copilot more as a reviewer than as a generator.

Prompt:
Review word_game.py and improve it for reliability and assignment quality. Focus on: keeping helper functions simple, avoiding inconsistent state, making repeated guesses harmless, making input case-insensitive, and ensuring the game can replay cleanly without leftover state from the previous round.

Copilot reviewed the code and confirmed that the important reliability points were already there:
- normalized input
- safe handling of repeated guesses
- fresh state for each round
- simpler helper functions

That matched the final structure well. Each round starts fresh in `play_one_game()`, and replay is handled separately in `run_game()`.

---

Finally, I asked Copilot for a short summary of the design choices.

Prompt:
Now review word_game.py one more time specifically for the project journal. Summarize in a few points what the main development decisions were, what problems were avoided by the current structure, and why separating helper functions improved the quality of the final game.

Copilot highlighted the main decisions:
- building the game step by step
- validating input early
- separating one-game logic from replay
- using helper functions with single responsibilities

That matched the final result well.

In the end, Copilot was most useful when I used it in small steps and later for review, instead of asking it to generate everything at once.

The final game includes:
- random word selection
- masked word display
- input normalization
- input validation
- guessed-letter tracking
- wrong-letter tracking
- win / lose checks
- replay support

The last important addition was the auto play mode required for the lab update.

Prompt:
Add an auto-play mode to the Python word guessing game. The computer should automatically choose letters that have not been guessed yet, and it should never suggest the same letter twice. Also add a simple mode selection so the user can choose between normal play and auto play.

Copilot suggested using the alphabet as a pool of possible letters and filtering out the letters that were already guessed.

This was useful because it matched the lab requirement and also let me reuse most of the same game structure instead of making a completely separate program.

In the final version, I added `get_auto_guess()` so the computer can choose a new unused letter, and `play_auto_game()` so the game can run by itself until it wins or loses.

I also added `ask_mode()` and updated `run_game()` so the player can choose between normal play, auto play, or quit.

This was the last step that made the project match the Lab 4 update more clearly.
