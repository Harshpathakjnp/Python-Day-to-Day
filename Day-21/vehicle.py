class Vehicles:
    def __init__(self,color,maxspeed):
        self.color = color
        self.maxspeed = maxspeed

class Car(Vehicles):
    def __init__(self,color,maxspeed,noofgear,isconvertible):
        super().__init__(color,maxspeed)
        self.noofgear = noofgear
        self.isconvertible = isconvertible

    def PrintCar(self):
        print("Color :",self.color)
        print("Maxspeed :",self.maxspeed)
        print("No.ofGear :",self.noofgear)
        print("Is Convertible :", self.isconvertible)




c = Car("red",250,3,"False")
c.PrintCar()
