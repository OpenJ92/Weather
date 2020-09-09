from schema.config import db

class Four_Day_Forecast(db.Model):
    __tablename__ = "Four_Day_Forcast"
    __table_args__ = {"schema": "openweatherapi"}

    __id__ = db.Column(db.Integer, primary_key = True)

    cod = db.Column(db.Text)
    message = db.Column(db.Float)

    ## list
    ## city
