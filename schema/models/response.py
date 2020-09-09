from schema.config import db

class Current_Weather_Response(db.Model):
    __tablename__ = "Current_Weather_Response"
    __table_args__ = {"schema": "OpenWeatherApi"}

    __id__ = db.Column(db.Integer, primary_key = True)

    cod = db.Column(db.Text)
    message = db.Column(db.Float)

    ## list
    ## city
