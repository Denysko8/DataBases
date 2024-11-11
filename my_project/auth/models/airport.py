from db_init import db

airport_flight = db.Table(
    'airport_flight',
    db.Column('airport_id', db.Integer, db.ForeignKey('airports.airport_id'), primary_key=True),
    db.Column('flight_id', db.Integer, db.ForeignKey('flights.flight_id'), primary_key=True)
)

class Airport(db.Model):
    __tablename__ = 'airports'

    airport_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), default=None)
    country = db.Column(db.String(50), default=None)
    iata_code = db.Column(db.String(3), default=None)


    def to_dict(self):
        return {
            "airport_id": self.airport_id,
            "name": self.name,
            "city": self.city,
            "country": self.country,
            "iata_code": self.iata_code
        }
