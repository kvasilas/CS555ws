import test_age
import tag_parse as tag
import age
from family_structure_test import *
from multiprocessing import Process

#KV User Stories
people, families = tag.read_file('./kvSprint2.ged')
people = age.store_ages(families, people)
print(test_age.test_mar_b4_death('xp', people))
print(test_age.test_div_b4_death('xp', people))


#JD User Stories


#RT User Stories

#JT User Stories
people, families = tag.read_file('./kvSprint2.ged')
people = age.store_ages(families, people)
print(listDeceasedTest(people))

peopleFam, familiesFam = tag.read_file('./jt_sprint2Fam.ged')
peopleFam = age.store_ages(familiesFam, peopleFam)
print(uniqueFamilyIDsTest(familiesFam))

peopleIndi, familiesIndi = tag.read_file('./jt_sprint2.ged')
peopleIndi = age.store_ages(familiesIndi, peopleIndi)
print(uniqueIndividualIDsTest(peopleIndi))