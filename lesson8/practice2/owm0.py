from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('e828a2e0ac8f6d650f845af746c9866a')
mgr = owm.weather_manager()

observation = mgr.weather_at_place(str(input('Print location you interested: ')))
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

print(w.detailed_status )