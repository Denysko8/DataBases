from db_init import db

# Association table for the many-to-many relationship between flights and routes
flight_route = db.Table(
    'flight_has_route',
    db.Column('flight_id', db.Integer, db.ForeignKey('flight.flight_id', ondelete="CASCADE"), primary_key=True),
    db.Column('route_id', db.Integer, db.ForeignKey('route.route_id', ondelete="CASCADE"), primary_key=True)
)