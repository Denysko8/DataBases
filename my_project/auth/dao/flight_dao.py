from my_project.auth.models.flight import Flight
from sqlalchemy.orm import Session

class FlightDAO:
    @staticmethod
    def get_all_flights(session: Session):
        return session.query(Flight).all()

    @staticmethod
    def get_flight_by_id(session: Session, flight_id: int):
        return session.query(Flight).filter(Flight.idFlight == flight_id).first()

    @staticmethod
    def create_flight(session: Session, flight_data: dict):
        new_flight = Flight(**flight_data)
        session.add(new_flight)
        session.commit()
        return new_flight

    @staticmethod
    def update_flight(session: Session, flight_id: int, updated_data: dict):
        flight = session.query(Flight).filter(Flight.idFlight == flight_id).first()
        if flight:
            for key, value in updated_data.items():
                setattr(flight, key, value)
            session.commit()
        return flight

    @staticmethod
    def delete_flight(session: Session, flight_id: int):
        flight = session.query(Flight).filter(Flight.idFlight == flight_id).first()
        if flight:
            session.delete(flight)
            session.commit()
        return flight
