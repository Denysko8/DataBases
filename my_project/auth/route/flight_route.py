from flask import Blueprint, jsonify
from my_project.auth.controller.flight_controller import FlightController
from my_project.auth.models.flight import Flight
from sqlalchemy import text
from my_project.auth.models.airport import Airport
from db_init import db# Assuming db is your SQLAlchemy instance

flight_bp = Blueprint('flight', __name__)

# Get all flights
@flight_bp.route('/flights', methods=['GET'])
def get_all_flights():
    flights = Flight.query.all()
    flights_data = [flight.to_dict() for flight in flights]
    return jsonify(flights_data)

# Get flight by ID
@flight_bp.route('/flights/<int:flight_id>', methods=['GET'])
def get_flight_by_id(flight_id):
    return FlightController.get_flight_by_id(flight_id)

# Create a new flight
@flight_bp.route('/flights', methods=['POST'])
def create_flight():
    return FlightController.create_flight()

# Update a flight
@flight_bp.route('/flights/<int:flight_id>', methods=['PUT'])
def update_flight(flight_id):
    return FlightController.update_flight(flight_id)

# Delete a flight
@flight_bp.route('/flights/<int:flight_id>', methods=['DELETE'])
def delete_flight(flight_id):
    return FlightController.delete_flight(flight_id)

# New route to get flight hour stats
@flight_bp.route('/flights/stats', methods=['GET'])
def get_flight_hours_stats():
    try:
        # Prepare the SQL query to call the stored procedure
        sql_query = text("CALL GetStatsForTotalFlightHours()")

        # Execute the query using SQLAlchemy's connection
        result = db.session.execute(sql_query)

        # Fetch all rows to check what is returned
        stats = result.fetchall()  # This will return a list of tuples

        # Check if any rows were returned
        if stats:
            return jsonify({"stats": stats[0][0]})  # Assuming the first element of the first tuple is your result
        else:
            return jsonify({"error": "No data returned from stored procedure"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@flight_bp.route('/random_tables', methods=['GET'])
def random_tables():
    try:
        # Prepare the SQL query to call the CreateDynamicTables procedure
        sql_query = text("CALL CreateDynamicTables()")

        # Execute the query using SQLAlchemy
        db.session.execute(sql_query)

        # Commit the transaction (if needed)
        db.session.commit()

        return jsonify({"message": "Dynamic tables created successfully!"}), 200
    except Exception as e:
        # If any exception occurs, return a 500 error with the error message
        return jsonify({"error": str(e)}), 500