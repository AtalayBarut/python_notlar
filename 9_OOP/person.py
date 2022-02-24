class Person:

    # Class attribute - can be also accessed via the class itself
    nationality = "Turkish"

    def __init__(self, name, age, gender):
        # # Instance attributes - can be only accessed via instances
        self.name = name
        self.age = age
        self.gender = gender

        # In Python, the constructor method for an object is named __init__().
        # As its name suggests, it is called when initializing an object of a class.
        # Because of this, you can use it to pass the initial attributes you want your object to be constructed with.

    def speak(self):
        print("Merhaba, ben {}. {} yaşındayım. Tanıştığımıza memnun oldum.".format(
            self.name, self.age))

        # The syntax for defining an instance method is familiar.
        # We pass the argument self which, as in the __init__ method, refers to the current object at hand.
        # Passing self will allow us to get or set the object's attributes inside our function.
        # It is always the first argument of an instance method.

    def greet(self, person):
        print(f"Merhaba {person.name}, nasılsın? ")

    def make_older(self):
        self.age += 1

    def talk(self, sentence):
        print(sentence)

osman = Person(age=24, gender="male", name="Osman")
print(osman.name, osman.age, osman.gender)
print("-"*100)

atalay = Person("Atalay", 36, "Male")
print(atalay.name, atalay.gender, atalay.age)
print(atalay.nationality)

ipek = Person("İpek", 30, "Female")
print(ipek.name, ipek.gender, ipek.age)
print(ipek.nationality)
print("-"*100)

ipek.speak()
atalay.speak()
atalay.greet(ipek)

print("-"*100)
print(atalay.age)
atalay.make_older()
print(atalay.age)

print("-"*100)
atalay.talk("Bu ne biçim hikaye böyle?")


