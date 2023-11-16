class House():
    def __init__(self, bedrooms, bathrooms):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.persons = []

    def add(self, person):
        self.persons.append(person)