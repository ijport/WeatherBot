import datapoint
import postcodes_io_api
import codebug_tether
import codebug_tether.sprites
from codebug_tether.sprites import Sprite
import time

def build_sprite(rows):
  s = Sprite(5, 5)
  for i in range(5):
    s.set_row(i, rows[i])
  return s

# Create connection to DataPoint with your API key
conn = datapoint.Manager(api_key="a3447661-0e61-4826-b59d-2cd1a9a613c2")

# Get longitude and latitude from postcode
postcodes_conn = postcodes_io_api.Api()
postcode = postcodes_conn.get_postcode('SK8 1ES')
latitude = postcode['result']['latitude']
longitude = postcode['result']['longitude']

# Get the nearest site for my latitude and longitude
site = conn.get_nearest_forecast_site(latitude, longitude)
print(site.name)

# Get a forecast for my nearest site with 3 hourly timesteps
forecast = conn.get_forecast_for_site(site.id, "3hourly")

# Get the current timestep from the forecast
current_timestep = forecast.now()

# Print out the site and current weather
print(site.name + "-" + current_timestep.weather.text)
print(current_timestep.temperature.value,current_timestep.temperature.units)
print(current_timestep.wind_direction.value)
print(current_timestep.wind_speed.value,current_timestep.wind_speed.units)

cb = codebug_tether.CodeBug()

#cbmessage = codebug_tether.sprites.StringSprite(("A"))
#cb.draw_sprite(0, 0, cbmessage)

msg_txt = current_timestep.weather.text + " " + current_timestep.wind_direction.value + " " + str(current_timestep.wind_speed.value) + " " + current_timestep.wind_speed.units
cbmessage = codebug_tether.sprites.StringSprite(msg_txt)
for i in range(0,-70,-1):

    cb.draw_sprite(i, 0, cbmessage)

    time.sleep(0.15)

weather_value = int(current_timestep.weather.value)
if weather_value > 9 and weather_value < 13:
    for count in range(3):
        # light rain
        cb.scroll_sprite(build_sprite([0b00100,0b01110,0b01110,0b00100,0b00100]), 100/1000, 'D')
if weather_value > 12 and weather_value < 16:
    # heavy rain
    for count2 in range(3):
        cb.scroll_sprite(build_sprite([0b01110,0b11111,0b11111,0b01110,0b00100]), 100/1000, 'D')
if weather_value > 27:
    # Thunder!
    for count3 in range(3):
        cb.scroll_sprite(build_sprite([0b00100,0b01000,0b00100,0b00010,0b00100]), 100/1000, 'D')
if weather_value == 1:
    # sunny!
    for count4 in range(3):
        cb.draw_sprite(0, 0, build_sprite([0b01100,0b11110,0b11110,0b01100,0b00000]));
        time.sleep(250/1000);
        cb.draw_sprite(0, 0, build_sprite([0b01101,0b11110,0b11111,0b01100,0b10101]));
        time.sleep(250/1000);
if weather_value == 7:
    # cloudy
    for count5 in range(3):
        cb.scroll_sprite(build_sprite([0b00000,0b11111,0b11111,0b01010,0b00000]), 100/1000, 'L')
if weather_value == 8:
    # overcast
    for count6 in range(3):
        cb.draw_sprite(0, 0, build_sprite([0b11111,0b11111,0b01010,0b00011,0b00011]));
        time.sleep(250/1000);
        cb.draw_sprite(0, 0, build_sprite([0b11111,0b11111,0b01111,0b00011,0b00111]));
        time.sleep(250/1000);
cb.clear()
