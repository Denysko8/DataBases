from db_init import db
from datetime import datetime
from my_project.auth.models.airport import Airport
from my_project.auth.models.routes import Route  # Assuming there is a Route model

class Flight(db.Model):
    __tablename__ = 'flights'

    flight_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flight_number = db.Column(db.String(20), nullable=False)
    departure_airport_id = db.Column(db.Integer, db.ForeignKey('airports.airport_id', ondelete="SET NULL"), nullable=True, default=None)
    arrival_airport_id = db.Column(db.Integer, db.ForeignKey('airports.airport_id', ondelete="SET NULL"), nullable=True, default=None)
    departure_time = db.Column(db.DateTime, nullable=True, default=None)
    arrival_time = db.Column(db.DateTime, nullable=True, default=None)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.route_id', ondelete="SET NULL"), nullable=True, default=None)

    # Relationships
    departure_airport = db.relationship('Airport', foreign_keys=[departure_airport_id], back_populates='departing_flights', lazy=True)
    arrival_airport = db.relationship('Airport', foreign_keys=[arrival_airport_id], back_populates='arriving_flights', lazy=True)
    route = db.relationship('Route', back_populates='flights', lazy=True)

    def __repr__(self):
        return f"<Flight(flight_id={self.flight_id}, flight_number='{self.flight_number}')>"

    def to_dict(self):
        return {
            "flight_id": self.flight_id,
            "flight_number": self.flight_number,
            "departure_airport_id": self.departure_airport_id,
            "arrival_airport_id": self.arrival_airport_id,
            "departure_time": self.departure_time.isoformat() if isinstance(self.departure_time, datetime) else self.departure_time,
            "arrival_time": self.arrival_time.isoformat() if isinstance(self.arrival_time, datetime) else self.arrival_time,
            "route_id": self.route_id
        }
