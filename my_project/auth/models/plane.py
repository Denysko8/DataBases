from db_init import db
from my_project.auth.models.others import MaintenanceRecord
from my_project.auth.models.plane_and_maintenance import plane_maintenance

class Plane(db.Model):
    __tablename__ = 'plane'

    plane_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registration_number = db.Column(db.String(20), nullable=False, unique=True)
    model = db.Column(db.String(50), default=None)
    airline_id = db.Column(db.Integer, db.ForeignKey('airline.airline_id'), default=None)
    total_flight_hours = db.Column(db.Integer, default=None)

    maintenances = db.relationship('MaintenanceRecord', secondary=plane_maintenance, back_populates='planes')
    airline = db.relationship('Airline', backref='planes')

    def __repr__(self):
        return f"<Plane(plane_id={self.plane_id}, registration_number='{self.registration_number}', model='{self.model}')>"

    def to_dict(self):
        return {
            "plane_id": self.plane_id,
            "registration_number": self.registration_number,
            "model": self.model,
            "airline_id": self.airline_id,
            "total_flight_hours": self.total_flight_hours,
        }

