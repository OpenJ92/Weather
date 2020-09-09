from schema.config import db

class Main(db.Model):
    __tablename__ = "Main"
    __table_args__ = {"schema": "OpenWeatherApi"}

    __id__ = db.Column(db.Integer, primary_key = True)

    lists = db.relationship('List', back_populates='main')

    ## Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
    temp = db.Column(db.Integer)

    ## This temperature parameter accounts for the human 
    ## perception of weather. Unit Default: Kelvin, Metric: Celsius, 
    ## Imperial: Fahrenheit.
    feels_like = db.Column(db.Float)

    ## Minimum temperature at the moment of calculation. This is minimal 
    ## forecasted temperature (within large megalopolises and urban areas), 
    ## use this parameter optionally. Unit Default: Kelvin, Metric: Celsius, 
    ## Imperial: Fahrenheit.
    temp_min = db.Column(db.Float)

    ## Maximum temperature at the moment of calculation. This is maximal 
    ## forecasted temperature (within large megalopolises and urban areas), 
    ## use these parameter optionally. Unit Default: Kelvin, Metric: Celsius, 
    ## Imperial: Fahrenheit.
    temp_max = db.Column(db.Float)

    ## Atmospheric pressure on the sea level by default, hPa
    pressure = db.Column(db.Integer)

    ## Atmospheric pressure on the sea level, hPa
    sea_level = db.Column(db.Integer)

    ## Atmospheric pressure on the ground level, hPa
    grnd_level = db.Column(db.Integer)

    ## Humidity, %
    humidity = db.Column(db.Integer)

    ## Internal parameter
    temp_kf = db.Column(db.Integer)
