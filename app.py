import os
from dotenv import load_dotenv
from flask import Flask
from db_init import db
from my_project.auth.route.airport_route import airport_bp
from my_project.auth.route.plane_route import plane_bp
from my_project.auth.route.flight_route import flight_bp
from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ.get('USER')}:{os.environ.get('PASSWORD')}@127.0.0.1:3306/{os.environ.get('DB_NAME')}"


db.init_app(app)

app.register_blueprint(airport_bp, url_prefix='/api')
app.register_blueprint(plane_bp, url_prefix='/api')
app.register_blueprint(flight_bp, url_prefix='/api')


@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check
    ---
    tags:
      - Health
    responses:
      200:
        description: OK
        schema:
          type: object
          properties:
            status:
              type: string
              example: healthy
    """
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)