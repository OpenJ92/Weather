from schema.config import db

## This is a 4-day forcast
class Current_Weather_Response(db.Model):
    __tablename__ = "Current_Weather_Response"
    __table_args__ = {"schema": "openweatherapi"}

    __id__ = db.Column(db.Integer, primary_key = True)

    cod = db.Column(db.Text)
    message = db.Column(db.Float)

    ## list
    ## city
