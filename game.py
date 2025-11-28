import json
import os
import random
import time

GAME_STATE = {}

LEADERBOARD_FILE = "leaderboard.json"


def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_leaderboard(data):
    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def start_game(chat_id):
    GAME_STATE[chat_id] = {
        "number": random.randint(1, 100),
        "attempts": 0,
        "start_time": time.time()
    }


def stop_game(chat_id):
    if chat_id in GAME_STATE:
        del GAME_STATE[chat_id]


def is_playing(chat_id):
    return chat_id in GAME_STATE


def process_guess(chat_id, guess):
    state = GAME_STATE[chat_id]
    state["attempts"] += 1

    number = state["number"]

    if guess < number:
        return "Більше"
    elif guess > number:
        return "Менше"
    else:
        duration = round(time.time() - state["start_time"], 2)

        result = {
            "attempts": state["attempts"],
            "time": duration
        }

        stop_game(chat_id)
        return result


def update_leaderboard(username, attempts, time_spent):
    data = load_leaderboard()
    data.append({
        "user": username,
        "attempts": attempts,
        "time": time_spent
    })

    data.sort(key=lambda x: (x["attempts"], x["time"]))

    save_leaderboard(data)
