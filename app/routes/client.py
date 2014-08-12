from flask import Blueprint, render_template, abort
from app.models import Event

client = Blueprint('client', __name__)

@client.route('/')
def index():
    return render_template('index.html', events=Event.objects())

@client.route('/events')
def events():
    return render_template('events/events.html', events=Event.objects())

@client.route('/events/<event_id>')
def event(event_id):
    if Event.objects(id=event_id).count() != 1:
        abort(404) # Either invalid event ID or duplicate IDs.

    e = Event.objects().get(id=event_id)
    return render_template('events/event.html', event=e)
