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
            self.incorrect_fields = {key: item[key] for key in item if item[key] != self.object[key]}

        return not self.incorrect_fields and self.difference == set() and self.extra_fields == set()

    # the 'expected' response
    def describe_to(self, description):
        # description.append_text("\n")
        # description.append_text(self.extra_fields)
        # description.append_text("\n")
        # description.append_text(self.difference)
        description.append_text("\n")
        # for key in self.incorrect_fields:
        #     description.append_text("{}: {}\n".format(key, self.object[key]))
        objectsss = {key: [self.object[key]] for key in self.incorrect_fields }
        description.append_text(tabulate(objectsss, headers='keys', tablefmt='fancy_grid'))

    # the 'but got' part
    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text("\n")
        required_tabular_format = {key: [self.incorrect_fields[key]] for key in self.incorrect_fields}
        mismatch_description.append_text(tabulate(required_tabular_format, headers='keys', tablefmt='fancy_grid'))

    def find_missing_fields(self, item):
        if len(item) > len(self.object):
            self.find_extra_fields(item)
        else:
            self.difference = set(self.object).difference(set(item))

    def find_extra_fields(self, item):
        self.extra_fields = set(item).difference(set(self.object))

def the_same_object(obj):
    return ObjectsMatch(obj)
