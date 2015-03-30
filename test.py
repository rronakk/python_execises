__author__ = 'rray'
import ast

class Ticket(object):
    ticket_id = 1
    def __init__(self):
        self.ticket_id = Ticket.ticket_id
        Ticket.ticket_id += 1

    def get_summary(self):
        self.summary = raw_input('please enter your ticket summary: ')
        return self.summary

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



def get_ticket():
    tic = Ticket()
    summary = tic.get_summary()
    id = tic.ticket_id
    assignee = tic.get_assignee()
    return  summary, id, assignee

print get_ticket()
print get_ticket()




"""
    def __init__(self,summary):
        self.ticket_id = Ticket.ticket_id
        Ticket.ticket_id += 1
        self.summary = summary

def get_summary():
    summary = raw_input('please enter your ticket summary: ')
    ticket = Ticket(summary)
    return ticket

print get_summary().summary
"""




