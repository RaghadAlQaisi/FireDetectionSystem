from app import db

class Alert(db.Model):
    __tablename__ = 'alerts'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String())
    cameraId = db.Column(db.Integer, db.ForeignKey('cameras.id'))
    image = db.Column(db.Text())

    def __init__(self, timestamp, cameraId, image):
        self.timestamp = timestamp
        self.cameraId = cameraId
        self.image = image


    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'cameraId': self.cameraId,
            'image': self.image
        }
