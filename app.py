import os
from dotenv import load_dotenv
from flask import Flask
from flasgger import Swagger
from flask import jsonify
from db_init import db
from my_project.auth.route.airport_route import airport_bp
from my_project.auth.route.plane_route import plane_bp
from my_project.auth.route.flight_route import flight_bp

app = Flask(__name__)

load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ.get('USER')}:{os.environ.get('PASSWORD')}@{os.environ.get('PUBLIC_IP')}:3306/{os.environ.get('DB_NAME')}"


db.init_app(app)

# Initialize Swagger but don't crash the app if spec generation fails —
# this lets the server run so you can isolate which blueprint/docstring causes errors.
try:
    swagger = Swagger(app)
except Exception as e:
    # Log exception to console; Swagger UI will show errors but server stays up
    print('Warning: Swagger initialization failed:', e)

# Register blueprints selectively using ENABLED_BLUEPRINTS env var.
# Set ENABLED_BLUEPRINTS to a comma-separated list like 'airport,plane' to register only those.
enabled = os.environ.get('ENABLED_BLUEPRINTS', '').strip()
enabled_set = set([p.strip().lower() for p in enabled.split(',') if p.strip()]) if enabled else None

def should_register(name: str) -> bool:
    if enabled_set is None:
        return True
    return name.lower() in enabled_set

if should_register('airport'):
    app.register_blueprint(airport_bp, url_prefix='/api')
if should_register('plane'):
    app.register_blueprint(plane_bp, url_prefix='/api')
if should_register('flight'):
    app.register_blueprint(flight_bp, url_prefix='/api')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)