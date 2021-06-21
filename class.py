class Car():
    def __init__(self, speedLimit, model, company, color):
        self.speedLimit = speedLimit
        self.company = company
        self.model = model
        self.color = color

    def startTheCar (self):
        print("Car Started")

    
    def stopCar(self):
        print("Car Stopped")

    def calcMileage(self, distance, fuel):
        mileage = distance/fuel
        print(mileage)

Audi = Car(80, "Q5", "Audi", "Moonlight Blue")
Tesla = Car(140, "Model Y", "Tesla", "Red")
BMW = Car(160, "Series 5", "BMW", "Black")

Audi.startTheCar()
Tesla.calcMileage(20193,647)
