

class Car():

    def __init__(self, mark, Conductor):
        self.__mark = mark
        self.driver = Conductor
        self.position = -1

    # getters obtener la informacion o los atributos
    # setters modificar la informacion o los atributos

    def get_mark(self):
        return self.__mark

    def set_mark(self, new_mark):

        self.__mark = new_mark

    def get_driver(self):
        return self.driver

    def set_driver(self, new_driver):
        self.driver = new_driver

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position
