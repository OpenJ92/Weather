from schema.config import db

class Clouds(db.Model):
    __tablename__ = "Main"
    __table_args__ = {"schema": "OpenWeatherApi"}

    __id__ = db.Column(db.Integer, primary_key = True)

    lists = db.relationship('List', back_populates='clouds')

    # Cloudiness, %
    all = db.Column(db.Integer)
