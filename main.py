import random
import requests
import time
from art import logo

print(logo)
print("\nWelcome to Stream Supreme!\n\n")
time.sleep(1)
print("In each round you'll get 2 artists. Guess which has the most plays on last.fm - the supreme streamer.")
time.sleep(2)
print("The winning artist is pulled to the next round.")
time.sleep(2)
print("Score high enough and you'll earn a spot on the scoreboard!\n")
time.sleep(2)

player_name = input("Start by entering your name: ").capitalize()
print(f"\nGood luck {player_name}!\n")

with open("api_key.txt") as key:
    API_Key = key.read().strip()
URL = "https://ws.audioscrobbler.com/2.0/"

def get_top_artists():
    difficulty = input("Choose your difficulty, 'Easy', 'Medium' or 'Hard': ").lower().strip()
    if difficulty == "easy":
        limit = 100
        print("\nOk, if you lose here, blame your Wi-Fi 🛜\n")
    elif difficulty == "medium":
        limit = 60
        print("\nOk, a mix of hits and 'who's that?' 👩‍🎤\n")
    else:
        limit = 20
        print("\nOk, hard mode, let's go 💪\n")
    params = {
        "method" : "chart.gettopartists",
        "api_key" : API_Key,
        "format" : "json",
        "limit" : {limit},
        "page" : 1
    }

    response = requests.get(URL, params = params)
    artist_data = response.json()
    return artist_data

data = get_top_artists()

artist_list = []
for artist in data["artists"]["artist"]:
    (artist_list.append({
        "name" : artist["name"],
        "playcount" : int(artist["playcount"])
    }))

def com(number):
    string_num = str(number)
    length = len(string_num)
    set_of_3 = []
    while length > 3:
        set_of_3.insert(0, string_num[length-3:length])
        length -= 3
    set_of_3.insert(0, string_num[:length])
    return ",".join(set_of_3)


def play_game(artists_data):
    artists = artist_list
    random.shuffle(artists)
    artist_a = artists.pop(0)
    artist_b = artists.pop(0)

    score = 0
    round_number = 1
    game_over = False

    while not game_over:
        print(f"\nRound {round_number}:")
        print(f"A: {artist_a["name"]}\nB: {artist_b["name"]}")

        guess = (input("Who has the higher playcount on last.fm, A or B?: ").upper().strip())

        if artist_a["playcount"] > artist_b["playcount"]:
            winner = artist_a
            loser = artist_b
            correct_answer = "A"
        else:
            winner = artist_b
            loser = artist_a
            correct_answer = "B"

        if guess == correct_answer:
            print(f"Yes! {winner["name"]} won with {com(winner["playcount"])} plays over "
                  f"{loser["name"]}'s {com(loser["playcount"])}")
            score += 1
        elif guess == "A" or guess == "B":
            print(f"Nope! {loser["name"]} has {com(loser["playcount"])} playcount but "
                  f"{winner["name"]} has {com(winner["playcount"])}.")
        else:
            print("You didn't guess correctly, make sure to answer A or B!")

        artist_a = winner
        artist_b = artists.pop(0)

        time.sleep(1)

        round_number += 1
        if round_number >10:
            game_over = True

    print(f"\nGame over {player_name}!\nYour final score: {score}/10")
    print(f"\nThe most played artist this game was {artist_a["name"]}!")

    return score

score = (play_game(artist_list))

def load_scoreboard(file="scoreboard.txt"):
    scoreboard = []
    with open(file, "r") as f:
        for line in f:
            name, score = line.strip().split(",")
            scoreboard.append((name, int(score)))
    return scoreboard

def save_and_update_scoreboard(scoreboard, player_name, score, file="scoreboard.txt"):
    scoreboard.append((player_name+" ", score))
    scoreboard.sort(key=lambda x: x[1], reverse=True)
    with open(file, "w") as f:
        for name, score in scoreboard:
            f.write(f"{name},{score}\n")
    return scoreboard

def print_scoreboard(scoreboard):
    print("\n🏆 Scoreboard 🏆")
    position = 1
    for row in scoreboard[:5]:
        name, score = row
        print(f"{position}. {name}: {score}")
        position += 1

scoreboard = load_scoreboard()
scoreboard = save_and_update_scoreboard(scoreboard,player_name, score)

if score == 10:
    print("10/10 Amazing! 🤩")

print("\nLet's see if you made it onto the scoreboard...")
time.sleep(3)

print_scoreboard(scoreboard)

top_5 = [name.strip() for name, score in scoreboard[:5]]
if player_name in top_5:
    print("\nI can see you're on there, well done!")
else:
    print(f"\nOh no {player_name}, better luck next time!")