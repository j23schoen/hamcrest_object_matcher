from hamcrest import assert_that, equal_to
from datetime import datetime, date
from src.hamcrest.object_matcher import is_the_same_object

def test_objects_match():
    map_1 = {
        'item': 5,
        'value': 1,
        'name': 'Hamcrest'
    }

    map_2 = {
        'item': 5,
        'value': 10,
        'name': 'bill'
    }

    assert_that(map_1, not is_the_same_object(map_2))

def test_first_object_has_additional_fields():
    map_1 = {
        'name': 'Jimmy',
        'hobby': 'Surfing',
        'age': 23
    }

    map_2 = {
        'name': 'Jimmy'
    }

    assert_that(map_1, not is_the_same_object(map_2))

def test_second_object_has_additional_fields():
    map_1 = {
        'name': 'Jimmy'
    }
    map_2 = {
        'name': 'Jimmy',
        'hobby': 'Surfing',
        'age': 23
    }

    assert_that(map_1, not is_the_same_object(map_2))

def test_objects_have_different_keys():
    map_1 = {
        'name': 'Justin',
        'age': 22,
        'activity': 'lifting',
        'car': 'toyota camry'
    }

    map_2 = {
        'name': 'Fred',
        'job': 'developer',
        'hobby': 'fishing',
        'music_preference': 'smooth jazz'
    }

    assert_that(map_1, not is_the_same_object(map_2))
