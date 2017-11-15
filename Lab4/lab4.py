#problam 1:

class Animal(object):
    def __init__(self,sound,name,age,favorite_color):
        self.sound = sound
        self.name = name
        self.age = age
        self.favorite_color = favorite_color

    def eat(self,food):
        print("yummy!!" + self.name + "is eating" + food)

    def description(self):
        print(self.name  +  "is"  +  str(self.age) +"years old and loves the color" +  self.favorite_color)

    #problam 2:

    def make_sound(self):
        print((self.sound +" ")*3)


d = Animal("bark", "charlie", 7, "blue")
d.eat("fish")
d.description()
#problam 2:
d.make_sound()


class Person(object):
    def __init__(self,name,age,city,gender,favorite_color):
        self.name = name
        self.age = age 
        self.city = city
        self.gender = gender
        self.favorite_color = favorite_color

    def eat(self,food):
        print("Yummy!!" + self.name +" " + "is eating"+" " + food)

    def favorite_song(self,song):
        print (self.name+" " + "is listening to"+ " " + song)

s = Person("Shir", 15, "Merhavia", "Female", "Purple")
s.eat("salad")
s.favorite_song("Let It Be")

    



        
