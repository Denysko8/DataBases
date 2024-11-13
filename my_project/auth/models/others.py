from db_init import db
from datetime import datetime
from my_project.auth.models.plane_and_maintenance import plane_maintenance

class Airline(db.Model):
    __tablename__ = 'airline'

    airline_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=True, default=None)
    founded_date = db.Column(db.Date, nullable=True, default=None)

    def __repr__(self):
        return f"<Airline(airline_id={self.airline_id}, name='{self.name}')>"

    def to_dict(self):
        return {
            "airline_id": self.airline_id,
            "name": self.name,
            "country": self.country,
            "founded_date": self.founded_date,
            "planes": [plane.registration_number for plane in self.planes]
        }



class Route(db.Model):
    __tablename__ = 'route'

    route_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    origin_airport_id = db.Column(db.Integer, db.ForeignKey('airport.airport_id', ondelete="SET NULL"), nullable=True)
    destination_airport_id = db.Column(db.Integer, db.ForeignKey('airport.airport_id', ondelete="SET NULL"), nullable=True, default=None)
    distance = db.Column(db.Integer, nullable=True, default=None)

    def __repr__(self):
        return f"<Route(route_id={self.route_id}, distance={self.distance})>"

    def to_dict(self):
        return {
            "route_id": self.route_id,
            "origin_airport_id": self.origin_airport_id,
            "destination_airport_id": self.destination_airport_id,
            "distance": self.distance,
            #"flights": [flight.flight_number for flight in self.flights]
        }


class Pilot(db.Model):
    __tablename__ = 'pilot'

    pilot_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(50), nullable=True, default=None)
    experience_years = db.Column(db.Integer, nullable=True, default=None)

    def __repr__(self):
        return f"<Pilot(pilot_id={self.pilot_id}, name='{self.name}')>"

    def to_dict(self):
        return {
            "pilot_id": self.pilot_id,
            "name": self.name,
            "license_number": self.license_number,
            "experience_years": self.experience_years
        }


class FlightCrew(db.Model):
    __tablename__ = 'flight_crew'

    flight_id = db.Column(db.Integer, db.ForeignKey('flight.flight_id', ondelete="SET NULL"), primary_key=True, nullable=False)
    pilot_id = db.Column(db.Integer, db.ForeignKey('pilot.pilot_id', ondelete="SET NULL"), primary_key=True, nullable=False)
    role = db.Column(db.String(50), nullable=True, default=None)

    def __repr__(self):
        return f"<FlightCrew(flight_id={self.flight_id}, pilot_id={self.pilot_id}, role='{self.role}')>"

    def to_dict(self):
        return {
            "flight_id": self.flight_id,
            "pilot_id": self.pilot_id,
            "role": self.role
        }


class MaintenanceRecord(db.Model):
    __tablename__ = 'maintenance_record'

    maintenance_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    details = db.Column(db.Text, nullable=True, default=None)

    planes = db.relationship('Plane', secondary=plane_maintenance, back_populates='maintenances')

    def __repr__(self):
        return f"<MaintenanceRecord(maintenance_id={self.maintenance_id})>"

    def to_dict(self):
        return {
            "maintenance_id": self.maintenance_id,
            "details": self.details,
            "planes": [plane.registration_number for plane in self.planes]
        }

class PlaneHistory(db.Model):
    __tablename__ = 'plane_history'

    history_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('planes.plane_id', ondelete="SET NULL"), nullable=True, default=None)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.flight_id', ondelete="SET NULL"), nullable=True, default=None)
    flight_date = db.Column(db.Date, nullable=True, default=None)

    def __repr__(self):
        return f"<PlaneHistory(history_id={self.history_id})>"

    def to_dict(self):
        return {
            "history_id": self.history_id,
            "plane_id": self.plane_id,
            "flight_id": self.flight_id,
            "flight_date": self.flight_date
        }


class PlanePosition(db.Model):
    __tablename__ = 'plane_position'

    position_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('planes.plane_id', ondelete="SET NULL"), nullable=True, default=None)
    latitude = db.Column(db.Numeric(9, 6), nullable=True, default=None)
    longitude = db.Column(db.Numeric(9, 6), nullable=True, default=None)
    altitude = db.Column(db.Integer, nullable=True, default=None)
    speed = db.Column(db.Integer, nullable=True, default=None)
    timestamp = db.Column(db.TIMESTAMP, nullable=True, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<PlanePosition(position_id={self.position_id})>"

    def to_dict(self):
        return {
            "position_id": self.position_id,
            "plane_id": self.plane_id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "altitude": self.altitude,
            "speed": self.speed,
            "timestamp": self.timestamp
        }
