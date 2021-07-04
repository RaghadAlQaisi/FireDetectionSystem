from app import db

class Camera(db.Model):
    __tablename__ = 'cameras'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    location = db.Column(db.Text())
    alerts = db.relationship("Alert")

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }
