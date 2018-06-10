#!/bin/usr/env python36

class Dog:
    species = 'mammal'

    def __init__(self, name , age , gender , race ,owner ):
        self.name   =   name
        self.age    = age
        self.gender =   gender
        self.race   =   race
        self.owner  =   owner

    def nothing(self):
        return "{} says {}".format(self.name, "Literally nothing")

pulki = Dog( "Pulki", "7", "f", "trash", "google-moogle")
lassy = Dog("Lassy","195","f","trash","Coli")

if pulki.species == "mammal" :
    print("{}, {}, {}, {}".format(pulki.name,pulki.age,pulki.gender,pulki.race,pulki.owner))
    print(pulki.nothing())