# Testing script for the API

import DiscordBotsAPI
import json

try:
    with open('config.json') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Cannot run tests: config.json does not exist")
    exit(1)

try:
    print("1. Correct usage")
    DiscordBotsAPI.update_counter(config['discord_bot_key'], config['discord_bot_id'], 50)
    print("Pass")
except RuntimeError as e:
    assert (False == True), "Error: " + e



try:
    print("2. Incorrect auth key")
    DiscordBotsAPI.update_counter('incorrect_key', config['discord_bot_id'], 50)
    assert (False == True), "Error: Should raise Runtime exception"
except RuntimeError as e:
    print("Pass")



try:
    print("3. Incorrect discord bot ID")
    DiscordBotsAPI.update_counter(config['discord_bot_key'], 'incorrect', 50)
    assert (False == True), "Error: Should raise Runtime exception"
except RuntimeError as e:
    print("Pass")
