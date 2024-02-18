from flask import Flask, request
from datetime import  datetime

from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime, func

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    start_time = Column(DateTime(timezone=True))
    end_time = Column(DateTime(timezone=True))
    
    def __repr__(self):
        return self.title
    

class CreateEvents(Resource):
    def post(self):
        data = request.json
        date_format = '%Y-%m-%d %H:%M:%S%z'

        start_time = datetime.strptime(data['start_time'], date_format)
        end_time = datetime.strptime(data['end_time'], date_format)
        event = Events(id=data['id'],title=data['title'], description=data['description'], start_time=start_time, end_time=end_time)
        db.session.add(event)
        db.session.commit()


        return {"response": "Success", "response code": 200}
    
class GetEvents(Resource):
    def get(self):
        events = Events.query.all()
        return_list = []
        for event in events:
            event_dict = {
                "title": event.title,
                "description": event.description,
                "start_time": str(event.start_time),
                "end_time": str(event.end_time),
            }
            return_list.append(event_dict)
        return return_list
    
class UpdateEvents(Resource):
    def put(self, pk):
        data = request.json
        event = Events.query.filter_by(id=pk).first()
        if data["title"]:
            event.title = data['title']
        if data["description"]:
            event.description = data['description']
        if data["start_time"]:
            event.name = data['start_time']
        if data["end_time"]:
            event.name = data['end_time']
        db.session.commit()
        event = Events.query.filter_by(id=pk).first()
        event_dict = {
            "title": event.title,
            "description": event.description,
            "start_time": str(event.start_time),
            "end_time": str(event.end_time),
        }
        return event_dict
            
    
class DeleteEvents(Resource):
    def delete(self, pk):
        if not Events.query.filter_by(id=pk):
            return {"response": "Not Found", "response code": 404}
        try:
            event = Events.query.filter_by(id=pk).first()
            db.session.delete(event)
            db.session.commit()
            return {"response": "Success", "response code": 200}
        except Exception as exe:
            return {"response": str(exe), "response code": 400}
        


api.add_resource(CreateEvents, '/create_event/')
api.add_resource(DeleteEvents, '/delete_event/<int:pk>')
api.add_resource(GetEvents, '/get_event/')
api.add_resource(UpdateEvents, '/update_event/<int:pk>')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)