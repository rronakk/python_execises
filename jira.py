__author__ = 'rray'
import jira_io_support

class Ticket(object):
    ticket_id = 1
    def __init__(self,summary, status, assignee = None , story_point = None ):
        self.ticket_id = Ticket.ticket_id
        Ticket.ticket_id += 1
        self.summary = summary
        self.status = status
        self.assignee = assignee
        self.story_point = story_point

    def get_ticket_id(self):
        return self.ticket_id

    def get_ticket_details(self):
        detail_list = self.summary, self.status, self.assignee, self.story_point
        return detail_list

ticket_list = []

def set_data(summary, status, assignee = None, story_point = None ):
    data = Ticket(summary ,status , assignee, story_point)
    ticket_list.append(data)

s1 = set_data("summary is this", "open", "ray", "100")
s2 = set_data("summary is this", "open", "ray", "100")
s3 = set_data("summary is this", "open", "ray", "100")


ticket_dict={}
for t in ticket_list:
    ticket_dict[t.get_ticket_id()] = t.get_ticket_details()
print ticket_dict
"""
jira_io_support.save_bundle(ticket_dict)

ticket = [Ticket("summary1", "status", "open", "100"), Ticket("summary1", "status", "open")]
print ticket
ticket_dict={}
for t in ticket:
    ticket_dict[t.get_ticket_id()] = t.get_ticket_details()
print ticket_dict


"""