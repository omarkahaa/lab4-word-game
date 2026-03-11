# JOURNAL

## 2026-03-11 — Replay feature and state reset

### Goal
Add a replay option so the player can start a new round after the game ends.

### Prompt used with Copilot
"How can I add a replay option to a Python terminal word guessing game?"

### Copilot suggestion
Copilot suggested wrapping the game in a function and asking the user at the end whether they want to play again with a `y/n` input.

### What did not work directly
The first idea was not enough by itself because some game variables would have stayed from the previous round if they were not reset properly.

### What I changed manually
I made sure the game state was initialized again for each new round so the guessed letters, lives, and display all start fresh.

### Result
The player can now replay the game correctly without restarting the script.

---

## 2026-03-11 — Input validation

### Goal
Make sure the player enters only one valid letter at a time.

### Prompt used with Copilot
"How do I validate user input in Python so only one alphabetical character is accepted?"

### Copilot suggestion
Copilot suggested using `.strip()`, checking the length of the input, and using `isalpha()`.

### What did not work directly
The raw suggestion needed adaptation to fit the structure of my game loop and feedback messages.

### What I changed manually
I added validation before processing the guess and showed an error message when the input was empty, too long, or not alphabetical.

### Result
The game now rejects invalid input and only accepts one letter at a time.

---

## 2026-03-11 — Repeated guess handling

### Goal
Prevent the same letter from being counted multiple times.

### Prompt used with Copilot
"How can I stop the player from guessing the same letter twice in a hangman-style game?"

### Copilot suggestion
Copilot suggested storing guessed letters in a collection and checking membership before processing a new guess.

### What did not work directly
The first version needed cleaner integration with the rest of the logic so the user would get a clear message without affecting the remaining lives.

### What I changed manually
I added a check before updating the game state. If the letter was already guessed, the program informs the player and continues without changing the round incorrectly.

### Result
Repeated guesses are now handled correctly.

---

## 2026-03-11 — Word display logic

### Goal
Show the hidden word with underscores for missing letters and reveal correct guesses.

### Prompt used with Copilot
"Suggest a simple way to display a hidden word with underscores and revealed letters in Python."

### Copilot suggestion
Copilot suggested iterating through the target word and building a display string based on whether each letter had already been guessed.

### What did not work directly
The suggestion was useful, but I still had to adapt it to the format I wanted for the terminal output.

### What I changed manually
I adjusted the display generation so it matched the rest of the game and updated it after each guess.

### Result
The player can clearly see progress after each turn.

---

## 2026-03-11 — General debugging and cleanup

### Goal
Make the game run cleanly from start to finish and keep the code readable.

### Prompt used with Copilot
"Review this simple Python word guessing game and suggest possible edge cases or cleanup improvements."

### Copilot suggestion
Copilot suggested reviewing replay flow, invalid input cases, repeated guesses, and separation of logic into simpler blocks.

### What did not work directly
Some suggestions were broader than needed for this assignment and had to be simplified.

### What I changed manually
I kept only the parts that were useful for this small lab project and avoided adding unnecessary complexity.

### Result
The final version stayed simple while covering the main gameplay cases.

---

## Reflection

Copilot was useful mainly for giving quick starting ideas for replay logic, validation, repeated guesses, and display handling. However, the suggestions were not enough on their own. I still had to adapt them, simplify them, and test them manually so the final result matched the expected behavior of the assignment.