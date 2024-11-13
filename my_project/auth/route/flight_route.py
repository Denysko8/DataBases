from flask import Blueprint
from my_project.auth.controller.flight_controller import FlightController
from flask import Blueprint, jsonify
from my_project.auth.models.flight import Flight
from my_project.auth.models.airport import Airport
from my_project.auth.models.flight_has_route import flight_route

flight_bp = Blueprint('flight', __name__)

@flight_bp.route('/flights', methods=['GET'])
def get_all_flights():
    flights = Flight.query.all()
    flights_data = [flight.to_dict() for flight in flights]
    return jsonify(flights_data)


# @flight_bp.route('/flights_with_airports', methods=['GET'])
# def get_flights_with_airports():
#     flights = Flight.query.all()
#     flights_data = []
#
#     for flight in flights:
#         flight_data = flight.to_dict()
#         # Додаємо інформацію про аеропорти відправлення і прибуття
#         flight_data['departure_airport'] = flight.departure_airport.to_dict() if flight.departure_airport else None
#         flight_data['arrival_airport'] = flight.arrival_airport.to_dict() if flight.arrival_airport else None
#         flights_data.append(flight_data)
#
#     return jsonify(flights_data)

@flight_bp.route('/flights/<int:flight_id>', methods=['GET'])
def get_flight_by_id(flight_id):
    return FlightController.get_flight_by_id(flight_id)

@flight_bp.route('/flights', methods=['POST'])
def create_flight():
    return FlightController.create_flight()

@flight_bp.route('/flights/<int:flight_id>', methods=['PUT'])
def update_flight(flight_id):
    return FlightController.update_flight(flight_id)

@flight_bp.route('/flights/<int:flight_id>', methods=['DELETE'])
def delete_flight(flight_id):
    return FlightController.delete_flight(flight_id)
