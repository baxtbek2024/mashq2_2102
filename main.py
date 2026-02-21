class Sensor:
    def __init__(self, location, temperature):
        self.location = location
        self.temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        self.__temperature = value
        if value < -90 or value > 60:
            self.__status = "xavfli"
        else:
            self.__status = "normal"

    def get_fahrenheit(self):
        return self.__temperature * 9/5 + 32

    def get_kelvin(self):
        return self.__temperature + 273.15

    @property
    def status(self):
        return self.__status
