# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.  
  The game is a Streamlit number-guesser where players choose a difficulty, guess a secret number within a range, receive higher/lower feedback, and try to win within a limited number of attempts while tracking score.

- [x] Detail which bugs you found.  
  I found multiple gameplay bugs: high/low hint directions were reversed, guesses could be compared against a string secret on some turns (causing misleading feedback), `Attempts left` could increase after `New Game` due to inconsistent attempt baseline, and `Show Hint` would disappear after reruns because hint text was not persisted.

- [x] Explain what fixes you applied.  
  I refactored core logic into `logic_utils.py` (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`), fixed hint direction mapping, removed mixed-type secret comparison in app flow, aligned attempt init/reset to `0`, reset round state consistently on `New Game`, and persisted hint text in `st.session_state` so hints survive reruns. I also added `tests/conftest.py` for stable pytest imports and added a regression test for hint direction in `tests/test_game_logic.py`.

## 📸 Demo

- ![Demo](https://cleanshot.com/share/pyqy0q7T+)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
