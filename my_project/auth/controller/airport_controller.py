from flask import jsonify, request
from my_project.auth.service.airport_service import AirportService
from db_init import db

class AirportController:
    @staticmethod
    def get_all_airports():
        airports = AirportService.get_all_airports(db.session)
        return jsonify([airport.to_dict() for airport in airports])

    @staticmethod
    def get_airport_by_id(airport_id: int):
        airport = AirportService.get_airport_by_id(db.session, airport_id)
        return jsonify(airport.to_dict()) if airport else (jsonify({"error": "Airport not found"}), 404)

    @staticmethod
    def create_airport():
        airport_data = request.json
        airport = AirportService.create_airport(db.session, airport_data)
        return jsonify(airport.to_dict()), 201

    @staticmethod
    def update_airport(airport_id: int):
        updated_data = request.json
        airport = AirportService.update_airport(db.session, airport_id, updated_data)
        return jsonify(airport.to_dict()) if airport else (jsonify({"error": "Airport not found"}), 404)

    @staticmethod
    def delete_airport(airport_id: int):
        airport = AirportService.delete_airport(db.session, airport_id)
        return jsonify({"message": "Airport deleted"}) if airport else (jsonify({"error": "Airport not found"}), 404)
