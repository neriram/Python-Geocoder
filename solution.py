import geocoder
import requests

API_BASE_URL = "https://api.darksky.net/forecast/c73c375afbedccd447f98b4e275bb84c/"

destinations = [
    'Space Needle',
    'Crater Lake',
    'Golden Gate Bridge',
    'Yosemite National Park',
    'Las Vegas, Nevada',
    'Grand Canyon National Park',
    'Aspen, Colorado',
    'Mount Rushmore',
    'Yellowstone National Park',
    'Sandpoint, Idaho',
    'Banff National Park',
    'Capilano Suspension Bridge'
]

for point in destinations:
    g = geocoder.arcgis(point)
    location = geocoder.arcgis(point)
    result = requests.request('GET', API_BASE_URL).json()
    currently = result['currently']['summary']
    temperature = result['currently']['temperature']
    print(f"{point} is located at {g.lat:4f}, {g.long: .4f})\nAt {point}, it is {currently}, {temperature:2f}")