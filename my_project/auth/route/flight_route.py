from flask import Blueprint
from my_project.auth.controller.flight_controller import FlightController

flight_bp = Blueprint('flight', __name__)

@flight_bp.route('/flights', methods=['GET'])
def get_all_flights():
    return FlightController.get_all_flights()

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
