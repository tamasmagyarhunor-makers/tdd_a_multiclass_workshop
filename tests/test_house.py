from lib.house import *
from lib.person import *
import pytest
from unittest.mock import Mock


def test_house_can_be_instantiated():
    actual = House(2, 3)

    assert isinstance(actual, House)

def test_initialises_with_number_of_bedrooms_and_bathrooms():
    # situation
    house = House(2, 3)
    
    # action
    actual_bedrooms = house.bedrooms
    actual_bathrooms = house.bathrooms

    expected_bedrooms = 2
    expected_bathrooms = 3

    # assertion
    assert actual_bedrooms == expected_bedrooms
    assert actual_bathrooms == expected_bathrooms

def test_house_instantiates_with_ability_to_store_persons():
    house = House(1, 1)

    actual = house.persons

    expected = []

    assert actual == expected

def test_house_can_add_a_person():
    house = House(2, 2)
    person = Person('Jordan', 23)

    house.add(person)

    actual = house.persons
    expected = [person]

    assert actual == expected

def test_house_can_print_person_name():
    house = House(1, 2)
    person = Mock()
    person2 = Mock()
    # mocking
    # we instruct the Mock object to expect get_person_name function to be called on it
    # and then to return 'Hunor'
    person.get_person_name.return_value = 'Hi, my name is Hunor'
    # we instruct the Mock object to expect get_person_name function to be called on it
    # and then to return 'Hunor'
    person2.get_person_name.return_value = 'Hi, my name is Jenny'

    house.add(person)
    house.add(person2)

    actual = house.persons_names()
    expected = ['Hi, my name is Hunor', 'Hi, my name is Jenny']

    assert actual == expected

    