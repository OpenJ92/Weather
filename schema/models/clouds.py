from schema.config import db

class Clouds(db.Model):
    __tablename__ = "Clouds"
    __table_args__ = {"schema": "openweatherapi"}

    __id__ = db.Column(db.Integer, primary_key = True)

    lists = db.relationship('List', back_populates='clouds')

    # Cloudiness, %
    all = db.Column(db.Integer)
