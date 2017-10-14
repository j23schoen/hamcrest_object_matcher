from hamcrest.core.base_matcher import BaseMatcher
from tabulate import tabulate

class ObjectsMatch(BaseMatcher):

    def __init__(self, obj):
        self.object = obj
        self.incorrect_fields = {}
        self.difference = set()
        self.extra_fields = set()
        self.different_keys = []
        self.item_is_dict = False
        self.object_is_dict = False
   
    def _matches(self, item):
        objects_are_equal = False
        self.item_is_dict = isinstance(item, dict)
        self.object_is_dict = isinstance(self.object, dict)

        if not self.item_is_dict or not self.object_is_dict:
            raise Exception("The inputs are required to be dictionaries.")
        elif len(item) != len(self.object):
            self.find_missing_fields(item)
        else:
            objects_are_equal = self.item_equals_object(item)

        return objects_are_equal

    # this is the item and the fields on the item
    def describe_to(self, description):
        if self.extra_fields:
            description.append_text("The following field(s) only to be on the object:\n")
            keys = [key for key in self.object]
            description.append_text(keys)
        elif self.difference:
            description.append_text("The object to have all the following field(s):\n")
            description.append_text(self.difference)
        elif self.incorrect_fields:
            description.append_text("The object to have the following field(s) with the corresponding values:\n")
            required_tabular_format = {key: [self.object[key]] for key in self.incorrect_fields }
            description.append_text(tabulate(required_tabular_format, headers='keys', tablefmt='fancy_grid'))
        elif self.different_keys:
            description.append_text("The object to have the following key(s):\n")
            description.append_text(self.different_keys)
            
    # this is the object part
    def describe_mismatch(self, item, mismatch_description):
        if self.extra_fields:
            mismatch_description.append_text("The following field(s) were also on the object:\n")
            mismatch_description.append_text(self.extra_fields)
        elif self.difference:
            mismatch_description.append_text("The object only has the following fields(s):\n")
            keys = [key for key in item]
            mismatch_description.append_text(keys)
        elif self.incorrect_fields:
            mismatch_description.append_text("The object's value(s) do not match: \n")
            required_tabular_format = {key: [item[key]] for key in self.incorrect_fields }
            mismatch_description.append_text(tabulate(required_tabular_format, headers='keys', tablefmt='fancy_grid'))
        elif self.different_keys:
            mismatch_description.append_text("The object has the following key(s):\n")
            keys = [key for key in item]
            mismatch_description.append_text(keys)
            
    def item_equals_object(self, item):
        for key in self.object:
            if not key in item:
                self.different_keys.append(key)
            elif self.object[key] != item[key]:
                self.incorrect_fields[key] = item[key]
        
        return True if not self.different_keys and not self.incorrect_fields else False
                
    def find_missing_fields(self, item):
        if len(item) > len(self.object):
            self.find_extra_fields(item)
        else:
            self.difference = set(self.object).difference(set(item))

    def find_extra_fields(self, item):
        self.extra_fields = set(item).difference(set(self.object))

def is_the_same_object(obj):
    return ObjectsMatch(obj)
