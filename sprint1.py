import test_age
import tag_parse as tag
import age
import family_structure_test


#KV User Stories
people, families = tag.read_file('./kvSprint1.ged')
people = age.store_ages(families, people)
print(test_age.test_birth_b4_marr('aa', people))
print(test_age.test_birth_b4_death(people))

#JT User Stories
people, families = tag.read_file('./jt_sprint1.ged')
people = age.store_ages(families, people)
print(test_age.test_less_than_one_fifty('@I1@', people))
print(test_age.test_marrige_after_fourteen('@I2@', people))

#JD User Stories
peopleJD, familiesJD = tag.read_file('./jdSprint1.ged')
print(family_structure_test.fiveLessBirthsTest(peopleJD, familiesJD))
print(family_structure_test.fifteenLessSiblingsTest(familiesJD))

#RT User Stories
people, families = tag.read_file('./rtSprint1.ged')
people = age.store_ages(families, people)
print(family_structure_test.parentsNotTooOldTest(people, '@F1@', families))
print(family_structure_test.maleLastNameTest(people, '@F1@', families))

