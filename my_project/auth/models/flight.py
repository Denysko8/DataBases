from db_init import db
#from my_project.auth.models.passenger import Passenger  # Import Passenger model

# In Flight model
class Flight(db.Model):
    __tablename__ = 'flight'

    flight_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flight_number = db.Column(db.String(20), nullable=False)
    departure_time = db.Column(db.DateTime, default=None)
    arrival_time = db.Column(db.DateTime, default=None)
    route_id = db.Column(db.Integer, db.ForeignKey('route.route_id'), default=None)

    # Remove backref from Flight model
    passengers = db.relationship('Passenger', lazy=True)

    def __repr__(self):
        return f"<Flight(flight_id={self.flight_id}, flight_number='{self.flight_number}', departure_time='{self.departure_time}')>"

    def to_dict(self):
        return {
            "flight_id": self.flight_id,
            "flight_number": self.flight_number,
            "departure_time": self.departure_time.isoformat() if self.departure_time else None,
            "arrival_time": self.arrival_time.isoformat() if self.arrival_time else None,
            "route_id": self.route_id,
            "passengers": [passenger.to_dict() for passenger in self.passengers]
        }
