from lib.house import *
from lib.person import *
import pytest

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