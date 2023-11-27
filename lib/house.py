class House():
    def __init__(self, bedrooms, bathrooms):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.persons = []

    def add(self, person):
        self.persons.append(person)
    
    def persons_names(self):
        names = []
        for person in self.persons:
            names.append(person.get_person_name())
        return names