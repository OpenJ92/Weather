from schema.models.snow import Snow
from schema.models.rain import Rain
from schema.models.main import Main
from schema.models.weather import Weather
from schema.models.wind import Wind
from schema.models.clouds import Clouds
from schema.models.response import Current_Weather_Response
from schema.models.list import List

from schema.config import db

if __name__ == "__main__":
    db.create_all()
