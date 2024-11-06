from my_project.auth.models.airport import Airport
from sqlalchemy.orm import Session

class AirportDAO:
    @staticmethod
    def get_all_airports(session: Session):
        return session.query(Airport).all()

    @staticmethod
    def get_airport_by_id(session: Session, airport_id: int):
        return session.query(Airport).filter(Airport.idAirport == airport_id).first()

    @staticmethod
    def create_airport(session: Session, airport_data: dict):
        new_airport = Airport(**airport_data)
        session.add(new_airport)
        session.commit()
        return new_airport

    @staticmethod
    def update_airport(session: Session, airport_id: int, updated_data: dict):
        airport = session.query(Airport).filter(Airport.idAirport == airport_id).first()
        if airport:
            for key, value in updated_data.items():
                setattr(airport, key, value)
            session.commit()
        return airport

    @staticmethod
    def delete_airport(session: Session, airport_id: int):
        airport = session.query(Airport).filter(Airport.idAirport == airport_id).first()
        if airport:
            session.delete(airport)
            session.commit()
        return airport
