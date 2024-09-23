# Define the Person class
class Person:
    # Constructor method to initialize attributes
    def __init__(self, name, age, heigth):
        self.name = name
        self.age = age
        self.height = heigth

    # Method to display information about the person
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Method to simulate a birthday
    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! You are now {self.age} years old.")

    def check_heigth(self):
        if  self.height < 160:
            print(f"Your heigth is not enough lil bro")
        else:
            print("tall enough.")

# Create an instance of the Person class
person1 = Person("Alice", 30, 150)
person1.display_info()  
person1.have_birthday()  
person1.check_heigth()

person2 = Person("Panke", 19, 161)
person2.display_info()
person2.have_birthday()
person2.check_heigth()
