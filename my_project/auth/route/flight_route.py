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
        """
        Get all flights

        Returns a list of all flights in the system.

        ---
        tags:
            - flights
        responses:
            200:
                description: A list of flight objects
                schema:
                    type: array
                    items:
                        type: object
                        properties:
                            flight_id:
                                type: integer
                            flight_number:
                                type: string
                            departure_airport_id:
                                type: integer
                            arrival_airport_id:
                                type: integer
                            departure_time:
                                type: string
                                format: date-time
                            arrival_time:
                                type: string
                                format: date-time
        """
        flights = Flight.query.all()
        flights_data = [flight.to_dict() for flight in flights]
        return jsonify(flights_data)

# Get flight by ID
@flight_bp.route('/flights/<int:flight_id>', methods=['GET'])
def get_flight_by_id(flight_id):
        """
        Get flight by ID

        Retrieve a single flight by its ID.

        ---
        tags:
            - flights
        parameters:
            - name: flight_id
                in: path
                type: integer
                required: true
                description: ID of the flight to retrieve
        responses:
            200:
                description: Flight object
            404:
                description: Flight not found
        """
        return FlightController.get_flight_by_id(flight_id)

# Create a new flight
@flight_bp.route('/flights', methods=['POST'])
def create_flight():
        """
        Create a new flight

        Create a new flight record. Expects JSON body with required fields (e.g., flight_number, departure_airport_id, arrival_airport_id, departure_time, arrival_time).

        ---
        tags:
            - flights
        consumes:
            - application/json
        parameters:
            - in: body
                name: body
                required: true
                schema:
                    type: object
                    required:
                        - flight_number
                        - departure_airport_id
                        - arrival_airport_id
                        - departure_time
                        - arrival_time
                    properties:
                        flight_number:
                            type: string
                            example: PS123
                        departure_airport_id:
                            type: integer
                            example: 1
                        arrival_airport_id:
                            type: integer
                            example: 2
                        departure_time:
                            type: string
                            format: date-time
                        arrival_time:
                            type: string
                            format: date-time
        responses:
            201:
                description: Flight created successfully
            400:
                description: Invalid input
        """
        return FlightController.create_flight()

# Update a flight
@flight_bp.route('/flights/<int:flight_id>', methods=['PUT'])
def update_flight(flight_id):
        """
        Update a flight

        Update flight fields by ID. Accepts JSON body with any flight fields to update.

        ---
        tags:
            - flights
        consumes:
            - application/json
        parameters:
            - name: flight_id
                in: path
                type: integer
                required: true
                description: ID of the flight to update
            - in: body
                name: body
                schema:
                    type: object
                    properties:
                        flight_number:
                            type: string
                        departure_airport_id:
                            type: integer
                        arrival_airport_id:
                            type: integer
                        departure_time:
                            type: string
                            format: date-time
                        arrival_time:
                            type: string
                            format: date-time
        responses:
            200:
                description: Flight updated successfully
            400:
                description: Invalid input
            404:
                description: Flight not found
        """
        return FlightController.update_flight(flight_id)

# Delete a flight
@flight_bp.route('/flights/<int:flight_id>', methods=['DELETE'])
def delete_flight(flight_id):
        """
        Delete a flight

        Delete a flight by its ID.

        ---
        tags:
            - flights
        parameters:
            - name: flight_id
                in: path
                type: integer
                required: true
                description: ID of the flight to delete
        responses:
            200:
                description: Flight deleted successfully
            404:
                description: Flight not found
        """
        return FlightController.delete_flight(flight_id)

# New route to get flight hour stats
@flight_bp.route('/flights/stats', methods=['GET'])
def get_flight_hours_stats():
        """
        Get flight hours statistics

        Calls a stored procedure `GetStatsForTotalFlightHours` to retrieve aggregated flight hours statistics.

        ---
        tags:
            - flights
            - stats
        responses:
            200:
                description: Statistics for total flight hours
                schema:
                    type: object
                    properties:
                        stats:
                            type: string
                            description: Aggregated stats returned by the stored procedure (format depends on procedure)
            404:
                description: No data returned from stored procedure
            500:
                description: Server error
        """
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
    """
    Create dynamic tables

    Calls the stored procedure `CreateDynamicTables` which creates dynamic tables in the database.

    ---
    tags:
        - flights
        - admin
    responses:
        200:
            description: Dynamic tables created successfully
        500:
            description: Server error
    """
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