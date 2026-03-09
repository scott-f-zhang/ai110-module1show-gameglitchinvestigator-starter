# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- On the first run, the UI said to guess 1-10, but when I entered `1`, it still told me to go lower, which suggests a boundary or feedback logic bug.  
- After clicking `New Game`, `Attempts left` increased instead of resetting, so round state was being accumulated incorrectly.  
- When I clicked `Show Hint`, the hint appeared on the first click, but a second click made it disappear, so hint visibility state was unstable across repeated clicks.  

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---

## 2. How did you use AI as a teammate?

I used an AI coding agent as a debugging teammate to inspect the Streamlit state flow and refactor logic into `logic_utils.py`.  
One correct suggestion was to persist hint text in `st.session_state` and render it after reruns, which fixed the issue where the hint disappeared after toggling `Show Hint`; I verified this by clicking the checkbox multiple times after submitting a guess.  
Another correct suggestion was to add a regression test for hint direction (`Too High` -> `LOWER`, `Too Low` -> `HIGHER`) so the bug would not come back.  
One misleading suggestion was when the AI said it could not run tests in my environment; the real issue was that it was not using my `conda` environment `ai110`, where `pytest` was available.  
I verified that by running `pytest` directly in `ai110`, which reproduced and then validated the test fixes.
To verify results in both code and gameplay, I first ran `pytest` and executed `python -m py_compile tests/test_game_logic.py` to confirm the logic and test file were valid.  
Then I opened the Streamlit app manually and repeated the bug scenarios (guess feedback direction, `New Game` attempts reset, and `Show Hint` behavior) to confirm the fixes worked in the actual UI.

---

## 3. Debugging and testing your fixes

I considered a bug fixed only after I could pass both automated checks and a manual gameplay check for the same scenario.  
In code, I ran `pytest` and `python -m py_compile tests/test_game_logic.py`; this verified imports, syntax, and the regression assertions for guess outcome and hint direction.  
In the app, I manually tested each repaired behavior: I checked that high/low feedback matched the guess, `New Game` reset attempts correctly, and `Show Hint` no longer disappeared on rerun.  
AI helped by suggesting where to add a targeted regression test, and I used that to confirm the specific bug did not return after refactoring.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
