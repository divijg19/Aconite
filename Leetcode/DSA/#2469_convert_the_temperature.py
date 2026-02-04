# 2469. Convert the Temperature
# https://leetcode.com/problems/convert-the-temperature/

def convert_temperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = celsius * 9 / 5 + 32
    return [kelvin, fahrenheit]
