class Car(object):
    def __init__(self, modal, colour, company, speedLimit) :
        self.colour = colour
        self.modal = modal
        self.company = company
        self.speedLimit = speedLimit

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelarate(self):
        print("accelarated")

    def change_gear(self, gear_type):
        print('Gear Changed')

audi = Car("a6", "black", "audi", "80")
audi.start()
print(audi.company)
