from age import *

def test_less_than_one_fifty(key, people):
    if (less_than_one_fifty(key, people) == "Death Age Invalid") or (less_than_one_fifty(key, people) == "Current Age Invalid"):
        return "ERROR, less_than_one_fifty"

def test_marrige_after_fourteen(key, families, people):
    if (marrige_after_fourteen(key, families, people) == "Marrige under the age of 14 is invalid")
        return "ERROR, marrige_after_fourteen"