
import random

items = ['rock', 'paper', 'scissors']


def com_choice(items):
    # choose random values from the list of items : rock, paper, scissors.
    selection = random.choice(items)
    return selection


def user_choice(items):
    print "Enter select any one of the following %s" %items
    user_selection = raw_input('>')
    print " you selected %s" % user_selection

print com_choice(items)
user_choice(items)
#test comment

