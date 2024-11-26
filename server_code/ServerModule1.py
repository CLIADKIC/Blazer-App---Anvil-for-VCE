import anvil.server
import xml.etree.ElementTree as ET

# Server function to process XML
@anvil.server.callable
def process_xml(file):
    data = file.get_bytes().decode('utf-8')
    root = ET.fromstring(data)
    weather_data_list = []

    # Iterate over each element in XML that represents a weather record
    for element in root.findall('weather'):
        location = element.find('location').text
        date = element.find('date').text
        max_temp = float(element.find('max_temp').text)
        min_temp = float(element.find('min_temp').text)

        # Add the weather data as a dictionary to the list
        weather_data = {
            "location": location,
            "date": date,
            "max_temp": max_temp,
            "min_temp": min_temp
        }
        weather_data_list.append(weather_data)

    return weather_data_list
