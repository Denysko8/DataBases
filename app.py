from flask import Flask
from db_init import db  # Ensure you have the correct initialization for your db
from my_project.auth.route.airport_route import airport_bp
from my_project.auth.route.plane_route import plane_bp
from my_project.auth.route.flight_route import flight_bp

app = Flask(__name__)

# Database URI to connect to MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:denysko@localhost/mydb'

# Initialize the database (only once)
db.init_app(app)

# Register blueprints for routes
app.register_blueprint(airport_bp, url_prefix='/api')
app.register_blueprint(plane_bp, url_prefix='/api')
app.register_blueprint(flight_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
