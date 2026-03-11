# REPORT

## First Impressions
At first, the project looked simple, but it quickly became clearer that even a small Hangman game needs clear state management, input validation, and separation between logic and UI. The instructions also required careful use of Copilot instead of blindly generating code.

## Key Learnings
I learned how to model a small console game with:
- a clear game state
- pure helper functions
- input validation
- win / lose detection
- replay support

I also learned that it is useful to design the state and invariants before coding because it makes the implementation simpler and reduces bugs.

## Copilot Prompting Experience
Copilot was most useful during:
- brainstorming app states
- identifying variables
- listing rules and invariants
- suggesting possible bugs and tests
- reviewing code structure

The most useful prompts were focused and specific. Broad prompts were less useful because they tended to overcomplicate the solution.

## Limitations and Reliability
Copilot could sometimes suggest solutions that were more complex than needed for this assignment. It also needed close supervision to make sure the solution respected the teacher's constraints, especially around purity, code simplicity, and the staged workflow.

Because of that, I used Copilot more as an assistant for review and ideas than as a direct code writer for the minimal core.

## Overall Reflection
This project showed that AI can speed up thinking, review, and documentation, but it does not replace understanding the problem. The most important part was still deciding the structure of the game and checking whether the implementation matched the requirements.

I felt more in control when I used Copilot for targeted support rather than for full automatic generation. For future projects, I would keep using AI as a support tool for design, debugging, testing ideas, and documentation.