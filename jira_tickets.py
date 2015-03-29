__author__ = 'rray'

# data structure i want : list = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]  where each dict will be a jira ticket

import jira_io_support



class Jira_ticket(object):
    ticket_id = 1
    def __init__(self,summary, state, assignee = None , story_point = None ):
        self.ticket_id = Jira_ticket.ticket_id
        Jira_ticket.ticket_id += 1
        self.summary = summary
        self.status = state
        self.assignee = assignee
        self.story_point = story_point

    def get_summary(self):
        return self.summary

    def get_status(self):
        return self.summary

    def get_assignee(self):
        return self.assignee

    def get_story_point(self):
        return self.story_point

    def get_ticket_id(self):
        return self.ticket_id


def set_value(summary = None, state = None, assignee = None , story_point = None):
    j_ticket = Jira_ticket(summary, state, assignee, story_point)
    return j_ticket

def set_key(summary = None, state = None, assignee = None , story_point = None):
    ticket = Jira_ticket(summary, state, assignee, story_point)
    jira_ticket_id.keys = ticket.get_ticket_id()
    return jira_ticket_id.keys

def find_ticket_id():
    t1 = Jira_ticket("summary", "state").get_ticket_id()
    return t1

t1 = create_ticket("this is summary", "open", "ronak")
print t1

def ticket_detail():
    return Jira_ticket.ticket_id, Jira_ticket.summary, Jira_ticket.status, Jira_ticket.assignee, Jira_ticket.story_point





first = Jira_ticket("this is my ticket", "open", "ronak", 2)
print first.ticket_id, first.assignee
print first.get_ticket_id()
print first.__dict__

second = Jira_ticket("this is my second ticker", "open")
print second.ticket_id
