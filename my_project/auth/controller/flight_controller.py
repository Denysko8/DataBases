from flask import jsonify, request
from my_project.auth.service.flight_service import FlightService
from db_init import db

class FlightController:
    @staticmethod
    def get_all_flights():
        flights = FlightService.get_all_flights(db.session)
        return jsonify([flight.to_dict() for flight in flights])

    @staticmethod
    def get_flight_by_id(flight_id: int):
        flight = FlightService.get_flight_by_id(db.session, flight_id)
        return jsonify(flight.to_dict()) if flight else (jsonify({"error": "Flight not found"}), 404)

    @staticmethod
    def create_flight():
        flight_data = request.json
        flight = FlightService.create_flight(db.session, flight_data)
        return jsonify(flight.to_dict()), 201

    @staticmethod
    def update_flight(flight_id: int):
        updated_data = request.json
        flight = FlightService.update_flight(db.session, flight_id, updated_data)
        return jsonify(flight.to_dict()) if flight else (jsonify({"error": "Flight not found"}), 404)

    @staticmethod
    def delete_flight(flight_id: int):
        flight = FlightService.delete_flight(db.session, flight_id)
        return jsonify({"message": "Flight deleted"}) if flight else (jsonify({"error": "Flight not found"}), 404)
