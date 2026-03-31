class Vehicle:
    def __init__(self,name,speed,milage):
        self.name = name
        self.speed = speed
        self.milage = milage

modelX = Vehicle("BMW",240,10)
modely = Vehicle("Mercides",250,8)

print("The model name is :",modelX.name)
print("The model maximum speed is :",modelX.speed)
print("The model milage is :",modelX.milage)
print("The model name is :",modely.name)
print("The model maximum speed is :",modely.speed)
print("The model milage is :",modely.milage)