import datapoint
import postcodes_io_api


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
import codebug_tether
import codebug_tether.sprites
import time

cb = codebug_tether.CodeBug()

#cbmessage = codebug_tether.sprites.StringSprite(("A"))
#cb.draw_sprite(0, 0, cbmessage)

cbmessage = codebug_tether.sprites.StringSprite(current_timestep.weather.text)
for i in range(0,-30,-1):

    cb.draw_sprite(i, 0, cbmessage)

    time.sleep(.1)
