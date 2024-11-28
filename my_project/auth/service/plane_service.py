from flask import jsonify, request
from datetime import datetime
from db_init import db
from my_project.auth.dao.plane_dao import PlaneDAO
from sqlalchemy.orm import Session
from my_project.auth.models.plane import Plane
from my_project.auth.models.others import MaintenanceRecord
from my_project.auth.models.plane_and_maintenance import plane_maintenance

class PlaneService:
    @staticmethod
    def get_all_planes(session: Session):
        return PlaneDAO.get_all_planes(session)

    @staticmethod
    def get_plane_by_id(session: Session, plane_id: int):
        return PlaneDAO.get_plane_by_id(session, plane_id)

    @staticmethod
    def create_plane(session, plane_data):
        plane = Plane(
            registration_number=plane_data['registration_number'],
            model=plane_data['model'],
            airline_id=plane_data['airline_id'],
            total_flight_hours=plane_data['total_flight_hours']
        )
        session.add(plane)
        session.commit()
        return plane

    @staticmethod
    def create_maintenance_record(session, maintenance_data):
        # Create the maintenance record
        maintenance_record = MaintenanceRecord(
            details=maintenance_data['details']  # Add maintenance details
        )

        # Add the plane to the maintenance record (since it's a many-to-many relationship)
        plane = Plane.query.get(maintenance_data['plane_id'])  # Fetch the plane from the DB
        if not plane:
            raise ValueError("Plane not found")

        maintenance_record.planes.append(plane)  # Associate the plane with the maintenance record

        session.add(maintenance_record)
        session.commit()
        return maintenance_record

    @staticmethod
    def create_plane_with_maintenance():
        data = request.json
        plane_data = data.get("plane")
        maintenance_data = data.get("maintenance")

        if not plane_data or not maintenance_data:
            return jsonify({"error": "Plane and maintenance data are required"}), 400

        # Create the plane
        plane = PlaneService.create_plane(db.session, plane_data)

        # Ensure the maintenance data contains a maintenance_date
        if 'maintenance_date' not in maintenance_data:
            return jsonify({"error": "Maintenance date is required"}), 400

        # Add the plane's ID to maintenance data
        maintenance_data['plane_id'] = plane.plane_id

        # Create the maintenance record and associate it with the plane
        PlaneService.create_maintenance_record(db.session, maintenance_data)

        return jsonify({
            "plane": plane.to_dict(),
            "maintenance": maintenance_data
        }), 201

    @staticmethod
    def create_maintenance_association(session: Session, plane_id: int, maintenance_id: int,
                                       maintenance_date: str):
        # Parse the maintenance_date string to a datetime object
        maintenance_date = datetime.strptime(maintenance_date, '%Y-%m-%d').date()

        # Make sure the plane and maintenance record exist
        plane = Plane.query.get(plane_id)
        maintenance_record = MaintenanceRecord.query.get(maintenance_id)

        if not plane or not maintenance_record:
            raise ValueError("Plane or Maintenance Record not found")

        # Insert into the plane_maintenance association table
        association_entry = plane_maintenance.insert().values(
            plane_id=plane_id,
            maintenance_id=maintenance_id,
            maintenance_date=maintenance_date
        )

        session.execute(association_entry)
        session.commit()

        return {
            "plane_id": plane_id,
            "maintenance_id": maintenance_id,
            "maintenance_date": maintenance_date
        }

    @staticmethod
    def update_plane(session: Session, plane_id: int, updated_data: dict):
        return PlaneDAO.update_plane(session, plane_id, updated_data)

    @staticmethod
    def delete_plane(session: Session, plane_id: int):
        return PlaneDAO.delete_plane(session, plane_id)
