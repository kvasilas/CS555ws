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
            if (type(people[p]['BIRT']) == str):
                birthday = people[p]['BIRT']
            else:
                birthday = "" + str(people[p]['BIRT'].year) + "-" + str(people[p]['BIRT'].month) + "-" + str(people[p]['BIRT'].day)
        else:
            birthday = 'NA'
        if ('AGE' in people[p]):
            age = people[p]['AGE']
        else:
            age = 'NA'
        if ('DEAT' in people[p]):
            if (type(people[p]['DEAT']) == str):
                death = people[p]['DEAT']
            else:
                death = "" + str(people[p]['DEAT'].year) + "-" + str(people[p]['DEAT'].month) + "-" + str(people[p]['DEAT'].day)
            alive = "False"
        else:
            death = 'NA'
            alive = "True"
        print("ID: " + id + " | Name: " + name + " | Gender: " + gender + " | Birthday: " + birthday + " | Age: " + str(age) + " | Alive: " + alive + " | Death: " + death)

def pretty_print_families(families, people):
    print("Families")
    for f in families:
        id = families[f]['ID']
        if ('MARR' in families[f]):
            if (type(families[f]['MARR']) == str):
                married = families[f]['MARR']
            else:
                married = "" + str(families[f]['MARR'].year) + "-" + str(families[f]['MARR'].month) + "-" + str(families[f]['MARR'].day)
        else:
            married = 'NA'
        if ('DIV' in families[f]):
            if (type(families[f]['DIV']) == str):
                divorced = families[f]['DIV']
            else:
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
pretty_print_people(people)
pretty_print_families(families, people)
print(test_age.test_mar_b4_death(people))
print(test_age.test_div_b4_death(people))


#JD User Stories
people, families = tag.read_file('./jd_sprint2.ged')
#people = age.store_ages(families, people)
pretty_print_people(people)
pretty_print_families(families, people)
print(noChildMarryTest(families))
print(test_age.test_date_before_current(people, families))

#RT User Stories
people, families = tag.read_file('./rtSprint2.ged')
people = age.store_ages(families, people)
pretty_print_people(people)
pretty_print_families(families, people)
noSiblingMarriageTest(families)
correctGenderTest(families, people)


#JT User Stories
people, families = tag.read_file('./kvSprint2.ged')
people = age.store_ages(families, people)

pretty_print_people(people)
pretty_print_families(families, people)

print(listDeceasedTest(people))

peopleFam, familiesFam = tag.read_file('./jt_sprint2Fam.ged')
peopleFam = age.store_ages(familiesFam, peopleFam)
print(uniqueFamilyIDsTest(familiesFam))

peopleIndi, familiesIndi = tag.read_file('./jt_sprint2.ged')
peopleIndi = age.store_ages(familiesIndi, peopleIndi)
print(uniqueIndividualIDsTest(peopleIndi))
