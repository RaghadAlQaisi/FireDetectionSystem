from flask import Blueprint, request, jsonify
from models.camera import Camera

camera_bp = Blueprint('camera_bp', __name__)


@camera_bp.route('/camera/create', methods=['POST'])
def create_event():
    from app import db
    jsonData = request.get_json()
    # data = json.loads(jsonData)
    name = jsonData['name']
    location = jsonData['location']
    try:
        camera = Camera(
            # slug=slugify(name),
            name=name,
            location=location
            )
        db.session.add(camera)
        db.session.commit()
        return jsonify(success=True, data={
            'id': camera.id,
            'name': camera.name,
            'location': camera.location
        })
    except Exception as e:
        return(str(e))


@camera_bp.route("/camera/all", methods=['GET'])
def get_all():
    try:
        cameras = Camera.query.all()
        return jsonify([a.serialize() for a in cameras])
    except Exception as e:
        return(str(e))


@camera_bp.route("/camera/<id_>", methods=['GET'])
def get_by_id(id_):
    try:
        camera = Camera.query.filter_by(id=id_).first()
        return jsonify(camera.serialize())
    except Exception as e:
        return(str(e))


@camera_bp.route("/camera/<id_>/delete", methods=['GET'])
def delete_by_id(id_):
    from app import db
    try:
        Camera.query.filter_by(id=id_).delete()
        db.session.commit()
        return jsonify(success=True)
    except Exception as e:
        return(str(e))


@camera_bp.route("/camera/<id_>/edit", methods=['POST'])
def edit_by_id(id_):
    from app import db
    try:
        jsonData = request.get_json()
        camera = Camera.query.filter_by(id=id_).first()
        # camera.slug=slugify(jsonData['name']),
        camera.name = jsonData['name']
        camera.location = jsonData['location']
        db.session.commit()
        return jsonify(success=True, data={
            'id': camera.id,
            'name': camera.name,
            'location': camera.location
        })
    except Exception as e:
        return(str(e))
