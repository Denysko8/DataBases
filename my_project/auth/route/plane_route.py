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
    return PlaneController.get_all_planes()

@plane_bp.route('/planes_with_maintenances', methods=['GET'])
def get_planes_with_maintenances():
    return PlaneController.get_planes_with_maintenances()

@plane_bp.route('/planes_with_airline', methods=['GET'])
def get_planes_with_airline():
    return PlaneController.get_planes_with_airline()

@plane_bp.route('/planes_with_maintenances', methods=['POST'])
def create_plane_with_maintenance():
    return PlaneController.create_plane_with_maintenance()

@plane_bp.route('/planes/<int:plane_id>', methods=['GET'])
def get_plane_by_id(plane_id):
    return PlaneController.get_plane_by_id(plane_id)

@plane_bp.route('/planes', methods=['POST'])
def create_plane():
    return PlaneController.create_plane()

@plane_bp.route('/planes/<int:plane_id>', methods=['PUT'])
def update_plane(plane_id):
    return PlaneController.update_plane(plane_id)

@plane_bp.route('/planes/<int:plane_id>', methods=['DELETE'])
def delete_plane(plane_id):
    return PlaneController.delete_plane(plane_id)
