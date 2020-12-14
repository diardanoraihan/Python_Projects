# Define the
class Vehicle:
    def __init__(self, make, model, year, weight, NeedsMaintenance = False, TripsSinceMaintencance = 0):
        self.Make = make
        self.Model = model
        self.Year = year
        self.Weight = weight # in kg
        self.NeedsMaintanance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintencance

    # Set methods
    def setMake(self, make):
        self.Make = make
    def setModel(self, model):
        self.Model = model
    def setYear(self, year):
        self.Year = year
    def setWeight(self, weight):
        self.Weight = weight

    # Print the current status of the vehicle
    def __str__(self):
        string1 = "Make: " + self.Make + "\nModel: " + self.Model + "\nYear: " + str(self.Year) + "\nWeight: " + str(self.Weight)
        string2 = "\nNeed Maintanance: " + str(self.NeedsMaintanance) + "\nTrips Since Maintanance: " + str(self.TripsSinceMaintenance)
        return string1 + string2 + "\n"

class Cars(Vehicle):
    def __init__(self, make, model, year, weight, NeedsMaintenance = False,
                 TripsSinceMaintencance = 0, is_driving=False):
        Vehicle.__init__(self, make, model, year, weight, NeedsMaintenance, TripsSinceMaintencance)
        self.isDriving = is_driving

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        self.isDriving = False
        self.TripsSinceMaintenance+=1
        if (self.TripsSinceMaintenance ==100):
            self.NeedsMaintanance = True

    def Repair(self):
        # Resets the trip and maintanance record
        self.TripsSinceMaintenance = 0
        self.NeedsMaintanance = False

myCar = Cars("Honda", "CR-V", 2018, 1500)
yourCar = Cars("Toyota", "Avanza", 2006, 1045)
hisCar = Cars("Kia", "Picanto", 2011, 1350)

# Drive myCar for 105 trips
for _ in range(105):
    myCar.Drive()
    myCar.Stop()
# Check the status of myCar
print(myCar)

# Drive yourCar for 50 trips
for _ in range(50):
    yourCar.Drive()
    yourCar.Stop()
# Check the status of yourCar
print(yourCar)

# Drive hisCar for 110 trips
for _ in range(110):
    hisCar.Drive()
    hisCar.Stop()
# Check the status of hisCar
print(hisCar)

'''
---------- Extra Credit ---------
'''

class Plane(Vehicle):
    def __init__(self, make, model, year, weight, NeedsMaintenance = False,
                 TripsSinceMaintencance = 0, is_flying=False):
        Vehicle.__init__(self, make, model, year, weight, NeedsMaintenance, TripsSinceMaintencance)
        self.isFlying = is_flying

    def Fly(self):
        if self.NeedsMaintanance!= True:
            self.isFlying = True
        else:
            print("The plane can't fly until it's repaired.\n")
            return False

    def Land(self):
        self.isFlying = False
        self.TripsSinceMaintenance +=1
        if (self.TripsSinceMaintenance == 100):
            self.NeedsMaintanance = True

ourPlane = Plane("Boeing", "747-8F", 2006, 64727.631)
# print(ourPlane)

# Drive ourPlane for 100 trips
for _ in range(100):
    ourPlane.Fly()
    ourPlane.Land()
# Check the status of hisCar
print(ourPlane)

# Check if ourPlane still can fly
ourPlane.Fly()

# Check to proof the current status of ourPlane doesn't change if it cannot fly
print(ourPlane)
