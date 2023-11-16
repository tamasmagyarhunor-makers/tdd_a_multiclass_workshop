from lib.person import *

def test_person_can_be_instantiated():
    actual = Person('Jordan', 23)

    assert isinstance(actual, Person)

def test_instantiates_with_name_and_age():
    actual = Person('Jordan', 23)

    expected_name = 'Jordan'
    expected_age = 23

    actual_name = actual.name
    actual_age = actual.age

    assert actual_name == expected_name
    assert actual_age == expected_age