class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        array = []
        kelvin =  celsius + 273.15
        array.append(kelvin)
        fahrenheit = celsius * 1.80 + 32.00
        array.append(fahrenheit)
        return array
        