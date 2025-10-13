from flask import Blueprint
from my_project.auth.controller.airport_controller import AirportController

airport_bp = Blueprint('airport', __name__)


@airport_bp.route('/airports', methods=['GET'])
def get_all_airports():
        """
        Get all airports
        ---
        tags:
            - Airports
        responses:
            200:
                description: A list of airports
                schema:
                    type: array
                    items:
                        type: object
        """
        return AirportController.get_all_airports()


@airport_bp.route('/airports/<int:airport_id>', methods=['GET'])
def get_airport_by_id(airport_id):
        """
        Get airport by ID
        ---
        tags:
            - Airports
        parameters:
            - name: airport_id
                in: path
                type: integer
                required: true
                description: ID of the airport
        responses:
            200:
                description: Airport object
                schema:
                    type: object
            404:
                description: Airport not found
        """
        return AirportController.get_airport_by_id(airport_id)


@airport_bp.route('/airports', methods=['POST'])
def create_airport():
        """
        Create airport
        ---
        tags:
            - Airports
        consumes:
            - application/json
        parameters:
            - in: body
                name: body
                required: true
                schema:
                    type: object
                    properties:
                        name:
                            type: string
                        city:
                            type: string
                        country:
                            type: string
                        iata_code:
                            type: string
        responses:
            201:
                description: Created
                schema:
                    type: object
            400:
                description: Invalid input
        """
        return AirportController.create_airport()


@airport_bp.route('/airports/<int:airport_id>', methods=['PUT'])
def update_airport(airport_id):
        """
        Update airport
        ---
        tags:
            - Airports
        parameters:
            - name: airport_id
                in: path
                type: integer
                required: true
                description: ID of the airport
            - in: body
                name: body
                required: true
                schema:
                    type: object
                    properties:
                        name:
                            type: string
                        city:
                            type: string
                        country:
                            type: string
                        iata_code:
                            type: string
        responses:
            200:
                description: Updated
            400:
                description: Invalid input
            404:
                description: Airport not found
        """
        return AirportController.update_airport(airport_id)


@airport_bp.route('/airports/<int:airport_id>', methods=['DELETE'])
def delete_airport(airport_id):
        """
        Delete airport
        ---
        tags:
            - Airports
        parameters:
            - name: airport_id
                in: path
                type: integer
                required: true
                description: ID of the airport to delete
        responses:
            204:
                description: Deleted
            404:
                description: Airport not found
        """
        return AirportController.delete_airport(airport_id)
