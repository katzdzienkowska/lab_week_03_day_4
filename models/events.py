from models.event import *

event1 = Event("2022, 06, 03", "Bank Holiday", 10, "United Kingdom", "Bank holiday for Platinum Jubilee", False)
event2 = Event("2022, 06, 02", "Class Lab", 2, "Room 6", "creating events page thing", True)
event3 = Event("2022, 06, 07", "Monday Standup", 19, "Zoom classroom", "Morning standup", True)

event_list = [event1, event2, event3]

def add_new_event(event):
    event_list.append(event)

def delete_event(event_name):
    event_to_delete = None
    for event in event_list:
        if event.name == event_name:
            event_to_delete = event
            break
    
    event_list.remove(event_to_delete)

