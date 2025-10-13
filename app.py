import os
try:
    # dotenv is optional in some environments
    from dotenv import load_dotenv
except Exception:
    load_dotenv = lambda *a, **k: None

from flask import Flask
from flasgger import Swagger
from db_init import db
from my_project.auth.route.airport_route import airport_bp
from my_project.auth.route.plane_route import plane_bp
from my_project.auth.route.flight_route import flight_bp

app = Flask(__name__)

# Initialize Swagger (Flasgger)
Swagger(app)

load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ.get('USER')}:{os.environ.get('PASSWORD')}@{os.environ.get('PUBLIC_IP')}:3306/{os.environ.get('DB_NAME')}"

db.init_app(app)

import traceback, sys
from flask import jsonify, make_response

swagger = Swagger(app)


@app.errorhandler(Exception)
def _handle_exception(e):
    """Return JSON with traceback for debugging purposes."""
    tb = traceback.format_exc()
    # Print to stderr so it also appears in server logs
    print(tb, file=sys.stderr)
    payload = {"error": str(e), "traceback": tb}
    return make_response(jsonify(payload), 500)

app.register_blueprint(airport_bp, url_prefix='/api')
app.register_blueprint(plane_bp, url_prefix='/api')
app.register_blueprint(flight_bp, url_prefix='/api')

if __name__ == '__main__':
    # Bind to all interfaces so the VM can access it
    app.run(host='0.0.0.0', debug=True)