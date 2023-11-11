class Solution(object):
    def convertTemperature(self, celsius):
        result = []
        kelvin = celsius + 273.15
        fahrenheit = (celsius * 1.80) + 32.00
        result.append(kelvin)
        result.append(fahrenheit)
        return result
        