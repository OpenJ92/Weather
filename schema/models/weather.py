from schema.config import db

class Weather(db.Model):
    __tablename__ = "Weather"
    __table_args__ = {"schema": "openweatherapi"}

    __id__ = db.Column(db.Integer, primary_key = True)

    lists = db.relationship('List', back_populates='weather')

    ## Weather condition id -- formerly id
    condition_id = db.Column(db.Integer)

    ## Group of weather parameters (Rain, Snow, Extreme etc.)
    main = db.Column(db.Text)

    ## Weather condition within the group. You can get the output 
    ## in your language. Learn more.
    description = db.Column(db.Text)

    ## Weather icon id
    icon = db.Column(db.Text)
