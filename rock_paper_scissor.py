
import random

items = ['rock', 'paper', 'scissors']


def com_choice(items):
    # choose random values from the list of items : rock, paper, scissors.
    selection = random.choice(items)
    print " Computer selected %s " % selection
    return selection

def usr_choice(items):
    # Getting user selection.
    print "Choose one of the following %s" % items
    user_selection = raw_input('>')
    print "You selected %s" % user_selection
    return user_selection


def result(user_choice, comp_choice):
    # Computing the winner
    print (" ------------Press enter to see the result ------------")
    raw_input()
    if user_choice == comp_choice:
        print "This is a Tie, Try again"
    else:
        if user_choice == "rock" and comp_choice == "scissors":
            print "You Win !!"
        elif user_choice == "scissors" and comp_choice == "paper":
            print "You Win !!"
        elif user_choice == "paper" and comp_choice == "rock":
            print "You Win !!"
        else:
            print "Better Luck Next Time, Computer has better luck !! "


user_choice = usr_choice(items)
comp_choice = com_choice(items)
result(user_choice, comp_choice)