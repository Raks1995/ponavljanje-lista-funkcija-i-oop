import random
import json
import datetime

time = datetime.datetime.now()

secret = random.randint(1, 30)
attempts = 0

with open("score_file.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

new_score_list = sorted(score_list, key=lambda k: k["attempts"][:3])

for score_dict in new_score_list:
    print("Top score: {0}, time: {1}, players name: {2}, secret number: {3}, wrong guesses: {4}".format(score_dict.get("attempts"), score_dict.get("time"), score_dict.get("name"), score_dict.get("secret_number"), score_dict.get("wrong_guesses")))

name = input("Name:")
wrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1
    wrong_guesses.append(guess)
    if guess == secret:
        score_list.append({"attempts": str(attempts), "time": str(time), "name": name, "secret_number": str(secret), "wrong_guesses": str(wrong_guesses[:-1])})
        with open("score_file.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")