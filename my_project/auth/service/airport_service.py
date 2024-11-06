from my_project.auth.dao.airport_dao import AirportDAO
from sqlalchemy.orm import Session

class AirportService:
    @staticmethod
    def get_all_airports(session: Session):
        return AirportDAO.get_all_airports(session)

    @staticmethod
    def get_airport_by_id(session: Session, airport_id: int):
        return AirportDAO.get_airport_by_id(session, airport_id)

    @staticmethod
    def create_airport(session: Session, airport_data: dict):
        return AirportDAO.create_airport(session, airport_data)

    @staticmethod
    def update_airport(session: Session, airport_id: int, updated_data: dict):
        return AirportDAO.update_airport(session, airport_id, updated_data)

    @staticmethod
    def delete_airport(session: Session, airport_id: int):
        return AirportDAO.delete_airport(session, airport_id)
