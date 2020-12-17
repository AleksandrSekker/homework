from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('e828a2e0ac8f6d650f845af746c9866a')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(str(input('Print location you interested: ')))
w = observation.weather
temp = w.temperature('celsius')
print('Maximum temperature: ', temp['temp_max'])
print('Minimum temperature: ', temp['temp_min'])
print('Middle temperature: ', temp['temp'])
print('Fells like: ', temp['feels_like'])
