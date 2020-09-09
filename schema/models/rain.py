from schema.config import db

class Main(db.Model):
    __tablename__ = "Main"
    __table_args__ = {"schema": "OpenWeatherApi"}

    __id__ = db.Column(db.Integer, primary_key = True)

    lists = db.relationship('List', back_populates='rain')

    ## Rain volume for last hour, mm -- formerly 1h
    oneh = db.Column(db.Integer) ## NOTE :: type of data unknown currently


