from schema.config import db

from schema.models.main import Main

class List(db.Model)
    __tablename__ = "List"
    __table_args__ = {"schema": "OpenWeatherApi"}

    __id__ = db.Column(db.Integer, primary_key = True)

    dt = db.Column(db.Integer)

    ## main
    __MAIN__ = db.Column(db.Integer, db.ForeignKey('OpenWeatherApi.Main.__id__'))
    main = db.relationship('Main', back_populates='lists')

    ## weather
    __WEATHER__ = db.Column(db.Integer, db.ForeignKey('OpenWeatherApi.Weather.__id__'))
    weather = db.relationship('Weather', back_populates='lists')

    ## clouds
    ## wind
    ## rain
    ## snow

    visibility = db.Column(db.Integer)
    pop = db.Column(db.Float)

    ## sys
    dt_text = db.Column(db.Text)
