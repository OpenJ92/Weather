from schema.config import db

class Snow(db.Model):
    __tablename__ = "Snow"
    __table_args__ = {"schema": "OpenWeatherApi"}

    __id__ = db.Column(db.Integer, primary_key = True)

    lists = db.relationship('List', back_populates='snow')

    ## Snow volume for last hour mm -- formerly 1h
    oneh = db.Column(db.Integer) ## NOTE :: type of data unknown currently
