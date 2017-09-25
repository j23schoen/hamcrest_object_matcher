from hamcrest import assert_that, is_
from datetime import datetime, date
from src.hamcrest.object_matcher import the_same_object

def test_objects_match():
    map_1 = {
        'item': 5,
        'value': 10,
        'name': 'Hamcrest'
    }

    map_2 = {
        'item': 5,
        'value': 10,
        'name': 'Hamcrest'
    }

    assert_that(map_1, is_(the_same_object(map_2)))

def test_objects_have_different_keys():
    map_1 = {
        'name': 'Jimmy',
        'hobby': 'Surfing',
        'age': 23
    }

    map_2 = {
        'name': 'Jimmy'
    }

    assert_that(map_1, is_(the_same_object(map_2)))