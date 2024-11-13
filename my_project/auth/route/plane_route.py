from flask import Blueprint, jsonify
from my_project.auth.controller.plane_controller import PlaneController
from my_project.auth.models.plane import Plane
from my_project.auth.models.others import MaintenanceRecord
from my_project.auth.models.plane_and_maintenance import plane_maintenance

plane_bp = Blueprint('plane', __name__)

@plane_bp.route('/planes', methods=['GET'])
def get_all_planes():
    return PlaneController.get_all_planes()

@plane_bp.route('/planes_with_maintenances', methods=['GET'])
def get_planes_with_maintenances():
    planes = Plane.query.all()
    planes_data = []

    for plane in planes:
        plane_data = plane.to_dict()
        plane_data['maintenance'] = [maintenance.to_dict() for maintenance in plane.maintenances]
        planes_data.append(plane_data)

    return jsonify(planes_data)

@plane_bp.route('/planes_with_airline', methods=['GET'])
def get_planes_with_airline():
    planes = Plane.query.all()
    planes_data = []

    for plane in planes:
        # Convert plane data to a dictionary
        plane_data = plane.to_dict()
        
        # Add airline details to plane data
        plane_data['airline'] = plane.airline.to_dict() if plane.airline else None
        
        planes_data.append(plane_data)

    return jsonify(planes_data)



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
