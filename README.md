# 🎵 Last.fm API Game 🎵

## Overview
I have made a console game using the **Last.fm API** 
to get artist data and turn it into a higher or lower game.

Over 10 rounds, the player guesses which artist has more plays on last.fm.

The winning artist stays on in the next round.

Scores are added to a scoreboard and the top 5 are displayed.


---

## Project Structure
Root folder
- requirements.txt = edited to include this projects requirements
- .gitignore = edited to include api_key.txt

Assignment-2/
- README.md = _This file!_ ☺️
- main.py = _Main game code_
- art.py = _ASCII logo art_
- scoreboard.txt = _A game scores file to read from and write to_

---

## Setup Instructions
1. **Install dependencies:**

The required packages are listed in `requirements.txt`.  
To install them, run:

`pip install -r requirements.txt`


2. **API Key Setup:**

- Get an API key from: https://www.last.fm/api/account/create
- Get an API account (it's free but needs to be email verified)
- Continue to create api account, url doesn't matter here
- Once registered you'll get your API key
- Create a file called `api_key.txt` in the assignment-2 folder.
- Place your API key in this file. (just the key)
- The key is read in `main.py` here:
`with open("api_key.txt") as key:
    API_KEY = key.read().strip()`

---

## The Game!
- Run the game with `main.py`
- Follow the prompts to play the game.
- Scores are saved to `scoreboard.txt` and the top 5 are displayed at the end of the game.

---