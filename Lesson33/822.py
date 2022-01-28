class Animal:
    def __init__(self,view,sound):
        self.view=view
        self.sound=sound
    def infor_an(self):
        print("Im an - ordinary animal")
class Cat(Animal):
    def __init__(self,view,sound,cat,sound_cat):
        super().__init__(view,sound)
        self.cat=cat
        self.sound_cat=sound_cat
    def show_species(self):
        if self.cat == self.cat:
            print(f"Im an - {self.cat}")
    def make_sound(self):
        if self.cat == self.cat:
            print(f"{self.sound_cat}")
class Dog(Animal):
    def __init__(self,view,sound,dog,sound_dog):
        super().__init__(view,sound)
        self.dog=dog
        self.sound_dog=sound_dog
    def show_species_2(self):
        if self.dog == self.dog:
            print(f"Im an - {self.dog}")
        else :
            print("Book this is not an animal!")
    def make_sound_2(self):
        if self.dog == self.dog:
            print(f"{self.sound_dog}")
        else :
            print("Book this is not an animal!")


special=Animal("ordinarily","Meow!Woof!")
special.infor_an()
special_cat = Cat("ordinarily","Meow","Cat","Meow!")
special_cat.make_sound()
special_cat.show_species()
special_cat.make_sound()
special_dog = Dog("ordinarily","Woof!","Dog","Woof!")
special_dog.show_species_2()
special_dog.make_sound_2()
special_dog.make_sound_2()
