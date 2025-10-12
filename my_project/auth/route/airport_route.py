from flask import Blueprint
from my_project.auth.controller.airport_controller import AirportController

airport_bp = Blueprint('airport', __name__)

@airport_bp.route('/airports', methods=['GET'])
def get_all_airports():
        """
        Get list of all airports

        Returns a list of airports available in the system.

        ---
        tags:
            - airports
        responses:
            200:
                description: A list of airport objects
                schema:
                    type: array
                    items:
                        type: object
                        properties:
                            airport_id:
                                type: integer
                                example: 1
                            name:
                                type: string
                                example: Kyiv International Airport
                            city:
                                type: string
                                example: Kyiv
                            country:
                                type: string
                                example: Ukraine
                            iata_code:
                                type: string
                                example: KBP
        """
        return AirportController.get_all_airports()

@airport_bp.route('/airports/<int:airport_id>', methods=['GET'])
def get_airport_by_id(airport_id):
        """
        Get airport by ID

        Retrieve a single airport by its ID.

        ---
        tags:
            - airports
        parameters:
            - name: airport_id
                in: path
                type: integer
                required: true
                description: ID of the airport to retrieve
        responses:
            200:
                description: Airport object
                schema:
                    type: object
                    properties:
                        airport_id:
                            type: integer
                        name:
                            type: string
                        city:
                            type: string
                        country:
                            type: string
                        iata_code:
                            type: string
            404:
                description: Airport not found
        """
        return AirportController.get_airport_by_id(airport_id)

@airport_bp.route('/airports', methods=['POST'])
def create_airport():
        """
        Create a new airport

        Create a new airport record. Expects a JSON body with required `name` and optional `city`, `country`, `iata_code`.

        ---
        tags:
            - airports
        consumes:
            - application/json
        parameters:
            - in: body
                name: body
                required: true
                schema:
                    type: object
                    required:
                        - name
                    properties:
                        name:
                            type: string
                            example: Lviv Danylo Halytskyi
                        city:
                            type: string
                            example: Lviv
                        country:
                            type: string
                            example: Ukraine
                        iata_code:
                            type: string
                            example: LWO
        responses:
            201:
                description: Airport created successfully
            400:
                description: Invalid input
        """
        return AirportController.create_airport()

@airport_bp.route('/airports/<int:airport_id>', methods=['PUT'])
def update_airport(airport_id):
        """
        Update an existing airport

        Update airport fields by ID. Accepts JSON body with any of the airport fields to update.

        ---
        tags:
            - airports
        consumes:
            - application/json
        parameters:
            - name: airport_id
                in: path
                type: integer
                required: true
                description: ID of the airport to update
            - in: body
                name: body
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
                description: Airport updated successfully
            400:
                description: Invalid input
            404:
                description: Airport not found
        """
        return AirportController.update_airport(airport_id)

@airport_bp.route('/airports/<int:airport_id>', methods=['DELETE'])
def delete_airport(airport_id):
        """
        Delete airport by ID

        Deletes an airport resource.

        ---
        tags:
            - airports
        parameters:
            - name: airport_id
                in: path
                type: integer
                required: true
                description: ID of the airport to delete
        responses:
            200:
                description: Airport deleted successfully
            404:
                description: Airport not found
        """
        return AirportController.delete_airport(airport_id)
