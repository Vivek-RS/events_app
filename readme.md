# Flask Events application

Simple Flask application that allows users to add, view, update, and delete events

#### Installation

- Clone repo

```
git clone https://github.com/Vivek-RS/events_app.git
```

- 2 - create a virtual environment and activate

```
cd events_app
python3 -m venv event_env
.event_env/Script/activate
pip install -r requiremets.txt
```

- 3 - Run flask server

```
python app.py

database initialization will be happened during app initialization
postman collection is added in the repositry (EventsApi.postman_collection.json)
```


#### Features

- Create Event
- Read Event
- Update Event
- Delete Event

#### Tech Stack

- Flask
- flask-restful
- flask-sqlalchemy
- sqlite3
