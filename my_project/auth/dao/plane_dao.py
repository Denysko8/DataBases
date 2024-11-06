from my_project.auth.models.plane import Plane
from sqlalchemy.orm import Session

class PlaneDAO:
    @staticmethod
    def get_all_planes(session: Session):
        return session.query(Plane).all()

    @staticmethod
    def get_plane_by_id(session: Session, plane_id: int):
        return session.query(Plane).filter(Plane.idPlane == plane_id).first()

    @staticmethod
    def create_plane(session: Session, plane_data: dict):
        new_plane = Plane(**plane_data)
        session.add(new_plane)
        session.commit()
        return new_plane

    @staticmethod
    def update_plane(session: Session, plane_id: int, updated_data: dict):
        plane = session.query(Plane).filter(Plane.idPlane == plane_id).first()
        if plane:
            for key, value in updated_data.items():
                setattr(plane, key, value)
            session.commit()
        return plane

    @staticmethod
    def delete_plane(session: Session, plane_id: int):
        plane = session.query(Plane).filter(Plane.idPlane == plane_id).first()
        if plane:
            session.delete(plane)
            session.commit()
        return plane
