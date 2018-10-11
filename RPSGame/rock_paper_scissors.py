from flask import Flask
from flask import render_template
from random import randint

app = Flask(__name__)

roundID = 0
player_score = 0
computer_score = 0
player = []
computer = []


def computer_play():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0, 2)]


def game_over():
    if computer_score == 2 or player_score == 2:
        is_over = True
    else:
        is_over = False
    return is_over


def to_be_played():
    if player_score > computer_score:
        to_play = 2 - player_score
    elif player_score < computer_score:
        to_play = 2 - computer_score
    elif (player_score == computer_score) and (player_score or computer_score != 0):
        to_play = 1
    else:
        to_play = 2
    return to_play


def get_round_winner(player_choice, computer_choice):
    winner = "Computer"

    if player_choice == computer_choice:
        winner = "Friendship, I guess at least!"
    if player_choice == "rock" and computer_choice == "scissors":
        winner = "You"
    if player_choice == "scissors" and computer_choice == "paper":
        winner = "You"
    if player_choice == "paper" and computer_choice == "rock":
        winner = "You"
    global roundID
    global player_score, computer_score

    if winner == "You":
        player_score += 1
    elif winner == "Computer":
        computer_score += 1

    roundID += 1
    return winner


def to_string(player_choice, computer_choice, who_won, to_play):
    if (player_score == 2 and computer_score != 2) or (player_score != 2 and computer_score == 2):
        return "You have selected: " + player_choice.__str__()\
               + "\nComputer Selected: " + computer_choice.__str__() + "\nthe Winner of this Round is: " \
               + who_won.__str__() + "\nRounds to be Played: " + to_play.__str__() + "\nScore is: " \
               + player_score.__str__() + "vs" + computer_score.__str__() + "\n" + who_won + " WON!!!"
    else:
        return "You have selected: " + player_choice.__str__()\
               + "\nComputer Selected: " + computer_choice.__str__() + "\nthe Winner of this Round is: " \
               + who_won.__str__() + "\nRounds to be Played: " + to_play.__str__() + "\nScore is: " \
               + player_score.__str__() + "vs" + computer_score.__str__()


@app.route('/rps/<choice>')
def rps(choice):

    while not game_over():
        player_choice = choice.lower()
        player.append(player_choice)
        computer_choice = computer_play()
        computer.append(computer_choice)
        who_won = get_round_winner(player_choice, computer_choice)
        remain = to_be_played()
        print(to_string(player_choice, computer_choice, who_won, remain))
        return render_template("rps.html", winner=who_won, player_choice=player_choice, computer_choice=computer_choice,
                               rounds_to_play=remain, player_score=player_score, computer_score=computer_score,
                               roundid=roundID, playerarray=player, computerarray=computer)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
