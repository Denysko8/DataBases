from flask import Blueprint, jsonify, request
from sqlalchemy import text
from db_init import db
from my_project.auth.controller.plane_controller import PlaneController
from my_project.auth.models.plane import Plane
from my_project.auth.models.others import MaintenanceRecord
from my_project.auth.models.plane_and_maintenance import plane_maintenance

plane_bp = Blueprint('plane', __name__)


@plane_bp.route('/planes_noname', methods=['POST'])
def bulk_insert_planes():
    """
    Bulk insert planes using stored procedure

    Calls the `bulk_insert_planes` stored procedure to insert multiple plane records in bulk.

    ---
    tags:
      - planes
      - admin
    responses:
      200:
        description: Planes inserted successfully
      500:
        description: Server error
    """
    try:
        # Execute the stored procedure using text()
        db.session.execute(text("CALL bulk_insert_planes()"))
        db.session.commit()
        return jsonify({"message": "Planes inserted successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@plane_bp.route('/planes', methods=['GET'])
def get_all_planes():
        """
        Get all planes

        Returns a list of all planes in the system.

        ---
        tags:
            - planes
        responses:
            200:
                description: A list of plane objects
                schema:
                    type: array
                    items:
                        type: object
                        properties:
                            plane_id:
                                type: integer
                            model:
                                type: string
                            airline_id:
                                type: integer
        """
        return PlaneController.get_all_planes()

@plane_bp.route('/planes_with_maintenances', methods=['GET'])
def get_planes_with_maintenances():
        """
        Get planes with maintenances

        Returns a list of planes together with their maintenance records.

        ---
        tags:
            - planes
        responses:
            200:
                description: A list of planes with maintenance records
        """
        return PlaneController.get_planes_with_maintenances()

@plane_bp.route('/planes_with_airline', methods=['GET'])
def get_planes_with_airline():
        """
        Get planes with airline information

        Returns a list of planes with associated airline details.

        ---
        tags:
            - planes
        responses:
            200:
                description: A list of planes with airline data
        """
        return PlaneController.get_planes_with_airline()

@plane_bp.route('/planes_with_maintenances', methods=['POST'])
def create_plane_with_maintenance():
        """
        Create a plane with maintenance records

        Create a plane resource along with initial maintenance records. Expects a JSON body describing the plane and maintenance entries.

        ---
        tags:
            - planes
        consumes:
            - application/json
                parameters:
                        - in: body
                            name: body
                            required: true
                            schema:
                                type: object
                                properties:
                                    model:
                                        type: string
                                    airline_id:
                                        type: integer
                                    maintenances:
                                        type: array
                                        items:
                                            type: object
                                            properties:
                                                date:
                                                    type: string
                                                    format: date
                                                description:
                                                    type: string
        responses:
            201:
                description: Plane with maintenances created
            400:
                description: Invalid input
        """
        return PlaneController.create_plane_with_maintenance()

@plane_bp.route('/planes/<int:plane_id>', methods=['GET'])
def get_plane_by_id(plane_id):
        """
        Get plane by ID

        Retrieve a single plane by its ID.

        ---
        tags:
            - planes
        parameters:
            - name: plane_id
              in: path
              type: integer
              required: true
              description: ID of the plane to retrieve
        responses:
            200:
                description: Plane object
            404:
                description: Plane not found
        """
        return PlaneController.get_plane_by_id(plane_id)

@plane_bp.route('/planes', methods=['POST'])
def create_plane():
        """
        Create a new plane

        Create a new plane resource. Expects JSON body with required fields (e.g., model, airline_id).

        ---
        tags:
            - planes
        consumes:
            - application/json
                parameters:
                        - in: body
                            name: body
                            required: true
                            schema:
                                type: object
                                required:
                                    - model
                                properties:
                                    model:
                                        type: string
                                    airline_id:
                                        type: integer
        responses:
            201:
                description: Plane created successfully
            400:
                description: Invalid input
        """
        return PlaneController.create_plane()

@plane_bp.route('/planes/<int:plane_id>', methods=['PUT'])
def update_plane(plane_id):
        """
        Update a plane

        Update plane fields by ID. Accepts JSON body with any plane fields to update.

        ---
        tags:
            - planes
        consumes:
            - application/json
                parameters:
                        - name: plane_id
                            in: path
                            type: integer
                            required: true
                            description: ID of the plane to update
                        - in: body
                            name: body
                            schema:
                                type: object
                                properties:
                                    model:
                                        type: string
                                    airline_id:
                                        type: integer
        responses:
            200:
                description: Plane updated successfully
            400:
                description: Invalid input
            404:
                description: Plane not found
        """
        return PlaneController.update_plane(plane_id)

@plane_bp.route('/planes/<int:plane_id>', methods=['DELETE'])
def delete_plane(plane_id):
        """
        Delete a plane

        Delete a plane by its ID.

        ---
        tags:
            - planes
        parameters:
            - name: plane_id
              in: path
              type: integer
              required: true
              description: ID of the plane to delete
        responses:
            200:
                description: Plane deleted successfully
            404:
                description: Plane not found
        """
        return PlaneController.delete_plane(plane_id)
