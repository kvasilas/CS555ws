import test_age
import tag_parse as tag
import age
from family_structure_test import *
import datetime


#Print IDs and Families
def pretty_print_people(people):
    print()
    print("People")
    for p in people:
        id = people[p]['ID']
        name = people[p]['NAME']
        if ('SEX' in people[p]):
            gender = people[p]['SEX']
        else:
            gender = 'NA'
        if ('BIRT' in people[p]):
            birthday = "" + str(people[p]['BIRT'].year) + "-" + str(people[p]['BIRT'].month) + "-" + str(people[p]['BIRT'].day)
        else:
            birthday = 'NA'
        if ('AGE' in people[p]):
            age = people[p]['AGE']
        else:
            age = 'NA'
        if ('DEAT' in people[p]):
            death = "" + str(people[p]['DEAT'].year) + "-" + str(people[p]['DEAT'].month) + "-" + str(people[p]['DEAT'].day)
            alive = "False"
        else:
            death = 'NA'
            alive = "True"
        print("ID: " + id + " | Name: " + name + " | Gender: " + gender + " | Birthday: " + birthday + " | Age: " + str(age) + " | Alive: " + alive + " | Death: " + death)

def pretty_print_families(families, people):
    print()
    print("Families")
    for f in families:
        id = families[f]['ID']
        if ('MARR' in families[f]):
            married = "" + str(families[f]['MARR'].year) + "-" + str(families[f]['MARR'].month) + "-" + str(families[f]['MARR'].day)
        else:
            married = 'NA'
        if ('DIV' in families[f]):
            divorced = "" + str(families[f]['DIV'].year) + "-" + str(families[f]['DIV'].month) + "-" + str(families[f]['DIV'].day)
        else:
            divorced = 'NA'
        if ('HUSB' in families[f]):
            husband = families[f]['HUSB']
            husname = people[husband]['NAME']
        else:
            husband = 'None'
            husname = 'NA'
        if ('WIFE' in families[f]):
            wife = families[f]['WIFE']
            wifename = people[wife]['NAME']
        else:
            wife = 'None'
            wifename = 'NA'
        if ('CHIL' in families[f]):
            children = families[f]['CHIL']
        else:
            children = 'None'
        print("ID: " + id + " | Married: " + married + " | Divorced: " + divorced + " | Husband ID: " + husband + " | Husband Name: " + husname + " | Wife ID: " + wife + " | Wife Name: " + wifename + " | Children:", children)


#KV User Stories
people, families = tag.read_file('./kvSprint2.ged')
people = age.store_ages(families, people)
print(test_age.test_mar_b4_death('xp', people))
print(test_age.test_div_b4_death('xp', people))


#JT User Stories
people, families = tag.read_file('./kvSprint2.ged')
people = age.store_ages(families, people)
print(uniqueIndividualIDsTest(people))
print(uniqueFamilyIDsTest(families))
print(listDeceasedTest(people))

#JD User Stories
people, families = tag.read_file('./jd_sprint2.ged')
print(noChildMarryTest(families))
print(test_age.test_date_before_current(people, families))

#RT User Stories
people, families = tag.read_file('./rtSprint2.ged')
people = age.store_ages(families, people)
pretty_print_people(people)
pretty_print_families(families, people)
print()
noSiblingMarriageTest(families)
correctGenderTest(families, people)

