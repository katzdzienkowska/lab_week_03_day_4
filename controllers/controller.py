from flask import render_template, request
from app import app
from models.events import event_list, add_new_event
from models.event import Event

@app.route("/events")
def index():
    return render_template("index.html", title="Events", events=event_list)

@app.route("/events", methods=["post"])
def add_event():
    print(request.form)
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_guests = request.form["guests"]
    event_location = request.form["location"]
    event_description = request.form["description"]
    event_recurring = "recurring" in request.form
    # event_recurring = request.form["recurring"]
    new_event = Event(event_date, event_name, event_guests, event_location, event_description, event_recurring)
    add_new_event(new_event)
    return render_template("index.html", title="Events", events=event_list)

