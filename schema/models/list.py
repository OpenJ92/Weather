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
    __CLOUDS__ = db.Column(db.Integer, db.ForeignKey('OpenWeatherApi.Clouds.__id__'))
    clouds =  db.relationship('Clouds', back_populates='lists')

    ## wind
    __WIND__ = db.Column(db.Integer, db.ForeignKey('OpenWeatherApi.Wind.__id__'))
    wind = db.relationship('Wind', back_populates='lists')

    ## rain
    __RAIN__ = db.Column(db.Integer, db.ForeignKey('OpenWeatherApi.Rain.__id__'))
    rain = db.relationship('Rain', back_populates='lists')

    ## snow
    __SNOW__ = db.Column(db.Integer, db.ForeignKey('OpenWeatherApi.Snow.__id__'))
    snow = db.relationship('Snow', back_populates='lists')

    visibility = db.Column(db.Integer)
    pop = db.Column(db.Float)

    ## sys
    dt_text = db.Column(db.Text)
