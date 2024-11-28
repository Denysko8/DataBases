from flask import jsonify, request
from my_project.auth.service.airport_service import AirportService
from db_init import db
from sqlalchemy import text


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

        required_fields = ['name', 'city', 'country', 'iata_code']
        if not all(field in airport_data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        try:
            query = text("""
                CALL insert_airport(:name, :city, :country, :iata_code)
            """)

            db.session.execute(query, {
                'name': airport_data['name'],
                'city': airport_data['city'],
                'country': airport_data['country'],
                'iata_code': airport_data['iata_code']
            })
            db.session.commit()

            return jsonify({"message": "Airport successfully created"}), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_airport(airport_id: int):
        updated_data = request.json
        airport = AirportService.update_airport(db.session, airport_id, updated_data)
        return jsonify(airport.to_dict()) if airport else (jsonify({"error": "Airport not found"}), 404)

    @staticmethod
    def delete_airport(airport_id: int):
        airport = AirportService.delete_airport(db.session, airport_id)
        return jsonify({"message": "Airport deleted"}) if airport else (jsonify({"error": "Airport not found"}), 404)
