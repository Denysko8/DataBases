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

swagger = Swagger(app)

app.register_blueprint(airport_bp, url_prefix='/api')
app.register_blueprint(plane_bp, url_prefix='/api')
app.register_blueprint(flight_bp, url_prefix='/api')

@app.route('/api/test-db', methods=['GET'])
def test_db():
    """
    Тест з'єднання з базою даних
    ---
    responses:
      200:
        description: Успішне з'єднання
      500:
        description: Помилка підключення
    """
    try:
        # Виконаємо простий запит до БД
        result = db.session.execute('SELECT NOW();')
        timestamp = list(result)[0][0]
        return jsonify({"status": "connected", "timestamp": str(timestamp)})
    except Exception as e:
        return jsonify({"status": "error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)