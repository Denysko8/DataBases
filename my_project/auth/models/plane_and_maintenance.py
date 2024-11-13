from db_init import db

plane_maintenance = db.Table(
    'plane_maintenance',
    db.Column('plane_id', db.Integer, db.ForeignKey('plane.plane_id'), primary_key=True),
    db.Column('maintenance_id', db.Integer, db.ForeignKey('maintenance_record.maintenance_id'), primary_key=True),
    db.Column('maintenance_date', db.Date, nullable=True, default=None)
)