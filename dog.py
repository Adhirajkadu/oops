class Dog:
    species="Dog"
    def __init__(self,name,age):
        self.name = name
        self.age = age

huskey=Dog("Huskey",20)
rot_willer=Dog("Rot Willer",25)

print(f"Huskey is a {huskey.species}")
print(f"Rot Willer is a {rot_willer.species}")

print(f"{huskey.name} is {huskey.age} years old.")

print(f"{rot_willer.name} is {rot_willer.age} years old.")