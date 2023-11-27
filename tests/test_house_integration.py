from lib.house import *
from lib.person import *

def test_house_can_print_person_name():
    house = House(1, 2)
    person = Person('Hunor', 35)
    person2 = Person('Jenny', 40)

    house.add(person)
    house.add(person2)

    actual = house.persons_names()
    expected = ['Hi, my name is Hunor', 'Hi, my name is Jenny']

    assert actual == expected