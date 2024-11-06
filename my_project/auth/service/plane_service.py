from my_project.auth.dao.plane_dao import PlaneDAO
from sqlalchemy.orm import Session

class PlaneService:
    @staticmethod
    def get_all_planes(session: Session):
        return PlaneDAO.get_all_planes(session)

    @staticmethod
    def get_plane_by_id(session: Session, plane_id: int):
        return PlaneDAO.get_plane_by_id(session, plane_id)

    @staticmethod
    def create_plane(session: Session, plane_data: dict):
        return PlaneDAO.create_plane(session, plane_data)

    @staticmethod
    def update_plane(session: Session, plane_id: int, updated_data: dict):
        return PlaneDAO.update_plane(session, plane_id, updated_data)

    @staticmethod
    def delete_plane(session: Session, plane_id: int):
        return PlaneDAO.delete_plane(session, plane_id)
