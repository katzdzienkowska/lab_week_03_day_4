from models.event import *

event1 = Event("2022, 06, 01", "Bank Holiday", 10, "United Kingdom", "Bank holiday for Platinum Jubilee")
event2 = Event("2022, 06, 01", "Class Lab", 2, "Room 6", "creating events page thing")
event3 = Event("2022, 06, 01", "Monday Standup", 19, "Zoom classroom", "Morning standup")

event_list = [event1, event2, event3]

def add_new_event(event):
    event_list.append(event)