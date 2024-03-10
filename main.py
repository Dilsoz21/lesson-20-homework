#Task_1
class Person_compare:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        if self.age < other.age:
            return f"{other.name} is older than me"

        elif self.age > other.age:
            return f"{other.name} is younger than me"

        elif self.age == other.age:
            return f"same age"


p1 = Person_compare("Samuel", 24)
p2 = Person_compare("Joel", 36)
p3 = Person_compare("Lily", 24)

print(p1.compare_age(p2))
print(p2.compare_age(p1))
print(p1.compare_age(p3))

#Task_2
inp = input("enter add or subtract or multiply or divide:")
result_for_add = 0
result_for_subtract = 0
result_for_multiply = 1
result_for_divide = 1
string = "10", "5"
for num in string:
    intgr = int(num)
    if inp == "add":
        result_for_add += intgr
        print(result_for_add)
    elif inp == "subtract":
        result_for_subtract -= intgr
        print(result_for_subtract)
    elif inp == "multiply":
        result_for_multiply *= intgr
        print(result_for_multiply)
    elif inp == "divide":
        result_for_divide /= intgr
        print(result_for_divide)
    else:
        print("it isn't maths")


#task_4


class Futbol_player:


    def __init__(self, name, age, height, weight, inp):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.input = inp

    def get_name_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is {self.height}"

    def get_weight(self):
        return f"{self.name} weighs {self.weight}kg"



obj = Futbol_player(name="David Jones", age=25, height=175, weight=75, inp=inp)
if inp == "get_age":
    print(obj.get_name_age())

elif inp == "get_height":
    print(obj.get_weight())

elif inp == "get_weight":
    print(obj.get_weight())


#Task_5
inp = input("enter employee: ")
class Person:
    def __init__(self, name, username, inp):
        self.name = name
        self.username = username
        self.input = inp

    def fullname(self):
        return f"{self.name} {self.username}"

    def email(self):
        return f"{self.name}.{self.username}@company.com"

    def firstname(self):
        return f"{self.name}"



obj = Person("Dilso'z", "Abduxoliqova", inp=inp)
if inp == "fullname":
    print(obj.fullname())

elif inp == "email":
    print(obj.email())

elif inp == "firstname":
    print(obj.firstname())


#Task_6
inp = input("enter name: ")
class Person:
    def __init__(self, fname, lname, fullname, initials, inp):
        self.fname = fname
        self.lname = lname
        self.fullname = fullname
        self.initials = initials
        self.input = inp

    def first_name(self):
        return f"{self.fname}"

    def last_name(self):
        return f"{self.lname}"

    def full_name(self):
        return f"{self.fname} {self.lname}"

    def short_forms(self):
        return f"{self.initials}"


obj = Person("Dilso'z", "Abduxoliqova", "Dilso'z Abduxoliqova", "D.M", inp=inp)
if inp == "fname":
    print(obj.fname())

elif inp == "lname":
    print(obj.lname())

elif inp == "fullname":
    print(obj.fullname())

elif inp == "initials":
    print(obj.initials())

else:
    print("error")


#Task_7