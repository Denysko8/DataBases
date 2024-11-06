from my_project.auth.dao.flight_dao import FlightDAO
from sqlalchemy.orm import Session

class FlightService:
    @staticmethod
    def get_all_flights(session: Session):
        return FlightDAO.get_all_flights(session)

    @staticmethod
    def get_flight_by_id(session: Session, flight_id: int):
        return FlightDAO.get_flight_by_id(session, flight_id)

    @staticmethod
    def create_flight(session: Session, flight_data: dict):
        return FlightDAO.create_flight(session, flight_data)

    @staticmethod
    def update_flight(session: Session, flight_id: int, updated_data: dict):
        return FlightDAO.update_flight(session, flight_id, updated_data)

    @staticmethod
    def delete_flight(session: Session, flight_id: int):
        return FlightDAO.delete_flight(session, flight_id)
