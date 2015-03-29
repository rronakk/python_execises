__author__ = 'rray'

import ast


class Ticket(object):
    ticket_id = 1
    possible_points = {None, 0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, float('inf')}

    def __init__(self):
        self.ticket_id = Ticket.ticket_id
        Ticket.ticket_id += 1

    def get_summary(self):
        self.summary = raw_input('Summary(required) : ')
        return self.summary


    def get_is_open(self):
        """Get True or False (only) as 'is_open' state of ticket."""
        while True:
            self.is_open = raw_input('Open? (required) ')
            if self.is_open not in ['True', 'False']:
                print 'Please answer either True or False.'
            else:
                try:
                    self.is_open = ast.literal_eval(self.is_open)
                except:
                    print 'Please answer either True or False.'
                    continue
                break
        return self.is_open

    def get_points(self):
        """Get Agile point-value, validating before acceptance."""
        while True:
            self.points = raw_input('Story Points (optional): ')
            if self.points in ['None', '']:
                self.points = None
            elif self.points == '1/2':
                self.points = 0.5
            elif self.points == 'infinity':
                self.points = float('inf')
            else:
                try:
                    self.points = int(self.points)
                except:
                    print ('"{}" is not an integer and the program can\'t convert '
                    'it to one.'.format(self.points))
                    continue
            if self.points in Ticket.possible_points:
                break
            else:
                print 'Please choose a valid point value.'
                continue
        return self.points

    def get_assignee(self):
        """Get assignee, and validate it before acceptance"""
        while True:
            self.assignee = raw_input("Enter assignee : ")
            if not self.assignee.replace(' ', '').isalpha():
                print "Please enter valid name"
                continue
            else:
                break
        return self.assignee

ticket_list = []

def set_ticket():
    """Setting value of Jira ticket, and adding it to the list"""
    ticket = Ticket()
    ticket_dict = {}
    ticket_dict['id'] =  ticket.ticket_id
    ticket_dict['summary'] = ticket.get_summary()
    ticket_dict['status'] = ticket.get_is_open()
    ticket_dict['story points'] = ticket.get_points()
    ticket_dict['assignee'] = ticket.get_assignee()
    ticket_list.append(ticket_dict)

def create_ticket():
    """taking user input to create new JIRA ticket"""
    while True:
        print 'Do you want create a new JIRA ticket (yes/no) ?'
        response = raw_input( '> : ' )
        if response.lower() == 'yes' :
            set_ticket()
            while True:
                print 'do you want to create another ?'
                another_response = raw_input('> : ')
                if another_response.lower() == 'yes':
                    set_ticket()
                    continue
                elif another_response.lower() == 'no':
                    print 'Thank you for using JIRA'
                    break
                else:
                    print 'please enter valid response (yes/no) '
                    continue
            break
        elif response.lower() == 'no':
            print 'Thank you for using JIRA'
            break
        else:
            print 'please enter valid response (yes/no) '
            continue

create_ticket()
print ticket_list



