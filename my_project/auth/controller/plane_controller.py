from flask import jsonify, request
from my_project.auth.service.plane_service import PlaneService
from db_init import db

class PlaneController:
    @staticmethod
    def get_all_planes():
        planes = PlaneService.get_all_planes(db.session)
        return jsonify([plane.to_dict() for plane in planes])

    def get_planes_with_maintenances():
        planes = PlaneService.get_all_planes(db.session)
        planes_data = []

        for plane in planes:
            plane_data = plane.to_dict()
            plane_data['maintenance'] = [maintenance.to_dict() for maintenance in plane.maintenances]
            planes_data.append(plane_data)

        return jsonify(planes_data)

    @staticmethod
    def get_planes_with_airline():
        planes = PlaneService.get_all_planes(db.session)
        planes_data = []

        for plane in planes:
            plane_data = plane.to_dict()
            plane_data['airline'] = plane.airline.to_dict() if plane.airline else None
            planes_data.append(plane_data)

        return jsonify(planes_data)

    @staticmethod
    def get_plane_by_id(plane_id: int):
        plane = PlaneService.get_plane_by_id(db.session, plane_id)
        return jsonify(plane.to_dict()) if plane else (jsonify({"error": "Plane not found"}), 404)

    @staticmethod
    def create_plane():
        plane_data = request.json
        plane = PlaneService.create_plane(db.session, plane_data)
        return jsonify(plane.to_dict()), 201

    @staticmethod
    def update_plane(plane_id: int):
        updated_data = request.json
        plane = PlaneService.update_plane(db.session, plane_id, updated_data)
        return jsonify(plane.to_dict()) if plane else (jsonify({"error": "Plane not found"}), 404)

    @staticmethod
    def delete_plane(plane_id: int):
        plane = PlaneService.delete_plane(db.session, plane_id)
        return jsonify({"message": "Plane deleted"}) if plane else (jsonify({"error": "Plane not found"}), 404)
