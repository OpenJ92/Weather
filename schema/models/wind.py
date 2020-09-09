from schema.config import db

class Wind(db.Model):
    __tablename__ = "Wind"
    __table_args__ = {"schema": "OpenWeatherApi"}

    __id__ = db.Column(db.Integer, primary_key = True)

    lists = db.relationship('List', back_populates='wind')

    ## Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
    speed  = db.Column(db.Float)
    ## Wind direction, degrees (meteorological)
    deg = db.Column(db.Integer)
