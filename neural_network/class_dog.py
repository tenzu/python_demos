# class for a dog object
class Dog:
    # initialisation method with internal data
    def __init__(self, petname, temp):
        self.name = petname
        self.temperature = temp

    # get status
    def status(self):
        print("dog name is ", self.name)
        print("dog temperature is ", self.temperature)

    # set temperature
    def setTemperature(self, temp):
        self.temperature = temp
        pass

    # dogs can bark()
    def bark(self):
        print("woof!")
        pass

    pass


lassie = Dog("Lassie", 37)
lassie.status()
lassie.setTemperature(40)
lassie.status()
