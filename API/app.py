import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    from routes.main import main_bp
    from routes.alert import alert_bp
    from routes.camera import camera_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(alert_bp)
    app.register_blueprint(camera_bp)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, threaded=True)
