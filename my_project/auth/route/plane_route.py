from flask import Blueprint
from my_project.auth.controller.plane_controller import PlaneController

plane_bp = Blueprint('plane', __name__)

@plane_bp.route('/planes', methods=['GET'])
def get_all_planes():
    return PlaneController.get_all_planes()

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
