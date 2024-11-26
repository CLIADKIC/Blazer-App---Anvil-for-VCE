from ._anvil_designer import Form1Template
from anvil import *
# import anvil.server
# import anvil.tables as tables
# from anvil.tables import app_tables
# import anvil.media

# Define a class to handle the weather data
class WeatherData:
    def __init__(self, location, date, max_temp, min_temp):
        self.location = location
        self.date = date
        self.max_temp = max_temp
        self.min_temp = min_temp

    def blazer_required(self):
        # Check if a blazer is required based on the max temperature
        if self.max_temp >= 28:
            return "No blazer required"
        else:
            return "Blazer required"

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    # Upload CSV and read data into class objects
    def upload_and_process_file(self, file):
        data = file.get_bytes().decode('utf-8').splitlines()
        weather_data_list = []

        # Skip the first line (headers)
        for line in data[1:]:
            location, date, max_temp, min_temp = line.split(",")
            # Create WeatherData objects and add them to the list
            weather = WeatherData(location, date, float(max_temp), float(min_temp))
            weather_data_list.append(weather)

        # Display data on the label
        display_text = ""
        for weather in weather_data_list:
            display_text += f"Location: {weather.location}, Date: {weather.date}, Max Temp: {weather.max_temp}°C, Min Temp: {weather.min_temp}°C, Blazer Required: {weather.blazer_required()}"
            alert(weather.blazer_required())
            
            
            
            
        self.lblWeatherData.text = display_text

    # FileLoader change event handler
    def fileLoader_change(self, file, **event_args):
        """This method is called when a new file is loaded into this FileLoader"""
        self.upload_and_process_file(file)
