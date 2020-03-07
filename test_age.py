from age import *

def test_less_than_one_fifty(key, people):
    if (less_than_one_fifty(key, people) == "Death Age Invalid") or (less_than_one_fifty(key, people) == "Current Age Invalid"):
        return "test_less_than_one_fifty passed"

def test_marrige_after_fourteen(key, people):
    if (marrige_after_fourteen(key,people) == "Marrige under the age of 14 is invalid"):
        return "marrige_after_fourteen passed"

def test_birth_b4_marr(key, people):
    ans = check_birth_before_marr(key,people)
    if("ERROR" in ans):
        return(ans)
    else:
        return("test_birth_b4_marr passed")

def test_birth_b4_death(people):
    for key in people:
        if('BIRT' in people[key].keys()):
            if('Death' in people[key].keys()):
                if('AGE' in people[key].keys()):
                    if(people[key]['AGE'] < 0):
                        yield(key+"ERROR, Birth Before Death")
                    else:
                        yield(key+"PASS Birth Before Death")


def test_mar_b4_death(key, people):
    if(mar_b4_death(key, people) == False):
        return("ERROR: Married before death")
    else:
        return("Mirrage and death dates valid")


def test_div_b4_death(key, people):
    if(div_b4_death(key, people) == False):
        return("ERROR: Divorced before death")
    else:
        return("Dicorce and death dates valid")

def test_date_before_current(people, families):
    result = datesBeforeCurrent(people, families)
    if "ERROR" in result:
        print(result)