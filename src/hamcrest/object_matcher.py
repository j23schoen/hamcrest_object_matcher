from hamcrest.core.base_matcher import BaseMatcher
from tabulate import tabulate

class ObjectsMatch(BaseMatcher):

    def __init__(self, obj):
        self.object = obj
        self.incorrect_fields = {}
        self.missing_fields = []
        self.result = {}
        self.difference = set()
        self.extra_fields = set()

    def _matches(self, item):

        if len(item) != len(self.object):
            self.find_missing_fields(item)
        else:
            self.incorrect_fields = {key: [item[key]] for key in item if item[key] != self.object[key]}

        return not self.incorrect_fields and self.difference == set() and self.extra_fields == set()

    # this is the item and the fields on the item
    def describe_to(self, description):
        # description.append_text(self.difference)
        if self.extra_fields:
            description.append_text("The following field(s) only to be on the object:\n")
            keys = [key for key in self.object]
            description.append_text(keys)
        elif self.difference:
            description.append_text("The object to have all the following field(s):\n")
            description.append_text(self.difference)
        elif self.incorrect_fields:
            description.append_text("The following field(s) did not match:")
            description.append_text("\n")
            required_tabular_format = {key: [self.object[key]] for key in self.incorrect_fields }
            description.append_text(tabulate(required_tabular_format, headers='keys', tablefmt='fancy_grid'))

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
            mismatch_description.append_text("\n")
            mismatch_description.append_text(tabulate(self.incorrect_fields, headers='keys', tablefmt='fancy_grid'))
            

    def find_missing_fields(self, item):
        if len(item) > len(self.object):
            self.find_extra_fields(item)
        else:
            self.difference = set(self.object).difference(set(item))

    def find_extra_fields(self, item):
        self.extra_fields = set(item).difference(set(self.object))

def the_same_object(obj):
    return ObjectsMatch(obj)
