class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person_name(self):
        return 'Hi, my name is ' + self.name