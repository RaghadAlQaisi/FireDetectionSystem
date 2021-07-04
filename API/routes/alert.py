from flask import Blueprint, request, jsonify
from models.alert import Alert


alert_bp = Blueprint('alert_bp', __name__)


@alert_bp.route('/alert/create', methods=['POST'])
# Save alert to table `alerts` in DB
def create_event():
    from app import db
    jsonData = request.get_json()
    timestamp = jsonData['timestamp']
    cameraId = int(jsonData['cameraId'])
    image = jsonData['image']
    try:
        alert = Alert(
            timestamp=timestamp,
            cameraId=cameraId,
            image=image
            )
        db.session.add(alert)
        db.session.commit()
        return jsonify(success=True, id=alert.id)
    except Exception as e:
        return(str(e))


@alert_bp.route("/alert/all", methods=['GET'])
# Get all alerts from DB
def get_all():
    try:
        alerts = Alert.query.all()
        return jsonify([a.serialize() for a in alerts])
    except Exception as e:
        return(str(e))


@alert_bp.route("/alert/<id_>", methods=['GET'])
def get_by_id(id_):
    try:
        alert = Alert.query.filter_by(id=id_).first()
        return jsonify(alert.serialize())
    except Exception as e:
        return(str(e))


@alert_bp.route("/alert/<id_>/delete", methods=['GET'])
def delete_by_id(id_):
    from app import db
    try:
        Alert.query.filter_by(id=id_).delete()
        db.session.commit()
        return jsonify(success=True)
    except Exception as e:
        return(str(e))
