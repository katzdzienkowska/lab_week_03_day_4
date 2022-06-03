from flask import render_template, request, redirect
from app import app
from models.events import event_list, add_new_event, delete_event
from models.event import *
import datetime

@app.route("/events")
def index():
    return render_template("index.html", title="Events", events=event_list)

@app.route("/events", methods=["post"])
def add_event():
    event_date = request.form["date"]
    # split_date = date.split("-")
    # date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    event_name = request.form["name"]
    event_guests = request.form["guests"]
    event_location = request.form["location"]
    event_description = request.form["description"]
    # event_recurring = request.form["recurring"]
    # if "recurring" in request.form:
    #   event_recurring = True
    # else:
    #   event_recurring = False
    event_recurring = "recurring" in request.form
    new_event = Event(event_date, event_name, event_guests, event_location, event_description, event_recurring)
    add_new_event(new_event)
    return redirect("/events")

@app.route('/events/delete/<name>', methods=['POST'])
def delete(name):
  delete_event(name)
  return redirect('/events')
  