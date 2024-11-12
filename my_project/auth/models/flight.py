from db_init import db
from my_project.auth.models.others import Route  # Import Route model if needed
from my_project.auth.models.flight_has_route import flight_route

class Flight(db.Model):
    __tablename__ = 'flight'

    flight_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flight_number = db.Column(db.String(20), nullable=False)
    departure_airport_id = db.Column(db.Integer, db.ForeignKey('airport.airport_id'), default=None)
    arrival_airport_id = db.Column(db.Integer, db.ForeignKey('airport.airport_id'), default=None)
    departure_time = db.Column(db.DateTime, default=None)
    arrival_time = db.Column(db.DateTime, default=None)
    route_id = db.Column(db.Integer, db.ForeignKey('route.route_id'), default=None)

    departure_airport = db.relationship('Airport', foreign_keys=[departure_airport_id], backref='departing_flights')
    arrival_airport = db.relationship('Airport', foreign_keys=[arrival_airport_id], backref='arriving_flights')

    routes = db.relationship('Route', secondary=flight_route, back_populates='flights')

    def __repr__(self):
        return f"<Flight(flight_id={self.flight_id}, flight_number='{self.flight_number}', departure_time='{self.departure_time}')>"

    def to_dict(self):
        return {
            "flight_id": self.flight_id,
            "flight_number": self.flight_number,
            "departure_airport_id": self.departure_airport_id,
            "arrival_airport_id": self.arrival_airport_id,
            "departure_time": self.departure_time.isoformat() if self.departure_time else None,
            "arrival_time": self.arrival_time.isoformat() if self.arrival_time else None,
            "route_id": self.route_id,
            "departure_airport": self.departure_airport.name if self.departure_airport else None,
            "arrival_airport": self.arrival_airport.name if self.arrival_airport else None,
        }
