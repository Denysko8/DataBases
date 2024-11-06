from db_init import db

class Airport(db.Model):
    __tablename__ = 'airports'

    airport_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=True, default=None)
    country = db.Column(db.String(50), nullable=True, default=None)
    iata_code = db.Column(db.String(3), nullable=True, default=None)  # IATA code (3 characters)

    def __repr__(self):
        return f"<Airport(airport_id={self.airport_id}, name='{self.name}', city='{self.city}', country='{self.country}')>"

    def to_dict(self):
        return {
            "airport_id": self.airport_id,
            "name": self.name,
            "city": self.city,
            "country": self.country,
            "iata_code": self.iata_code
        }
