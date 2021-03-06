import test_age
import tag_parse as tag
import age
import family_structure_test
from make_table import print_tables

#Table Management
#Initialize dictonaries with KC's GEDCOM
people, families = tag.read_file('./sprint3/kv_sprint3.ged')
people = age.store_ages(families, people)
#Add Ryan's GEDCOM
peopleRT, familiesRT = tag.read_file('./sprint3/rtSprint3.ged')
peopleRT = age.store_ages(familiesRT, peopleRT)
people.update(peopleRT)
families.update(familiesRT)
#Add Detone's GEDCOM
peopleJD, familiesJD = tag.read_file('./sprint3/jd_sprint3.ged')
peopleJD = age.store_ages(familiesJD, peopleJD)
people.update(peopleJD)
families.update(familiesJD)
#Add Trugman's GEDCOM (Only the non-breaking error)
peopleJT, familiesJT = tag.read_file('./sprint3/jt_list_recent_births.ged')
peopleJT = age.store_ages(familiesJT, peopleJT)
people.update(peopleJT)
families.update(familiesJT)
print_tables(families, people)



#Demonstration user stories
print("\nUser story demonstrations: US30, US31, US35:")

#KV User Stories
#US30 -List living married
#US31 -List living single
people, families = tag.read_file('./sprint3/kv_sprint3.ged')
people = age.store_ages(families, people)
    #print('KV User Stories: US30 - List living married and US31 -List living single')
    #print_tables(families, people)
print("US30 - List living Married: ", family_structure_test.test_ListLivingMarried(people))
print("US31 - List living Single over 30: ", family_structure_test.test_ListLivingSingle(people))
    #print('\n##########################################################################\n')

# JT User Story #1
#US35
people, families = tag.read_file('./sprint3/jt_list_recent_births.ged')
people = age.store_ages(families, people)
    #print('JT user stories US35 and US42')
    #print_tables(families, people)
print("US35 - Recent Births:", age.listRecentBirths(people))



#Error user stories
print("\nUser story demonstrations: US19, US20, US24, US25, US42:")

#RT User Stories
    #print("RT user stories US19 & US20")
people, families = tag.read_file('./sprint3/rtSprint3.ged')
people = age.store_ages(families, people)
    #print_tables(families, people)
#US19 - First cousins should not marry
family_structure_test.noCousinMarriageTest(families)
#US20 - Aunts and uncles should not marry nieces and nephews
family_structure_test.noNieceNephewMarriageTest(families)
    #print('\n##########################################################################\n')

# JD User Stories
    #print('JD User Stories 24 & 25')
people, families = tag.read_file('./sprint3/jd_sprint3.ged')
people = age.store_ages(families, people)
    #print_tables(families, people)
# US24
print(family_structure_test.test_unique_fam(people, families))
# US25
print(family_structure_test.test_unique_first(people, families))
    #print('\n##########################################################################\n')



# JT User Story #2
# run validate age last because it will exit out the program when an invalid age is entered
# this is because there is no point in continuing with the rest of the program when the dates are invalid
#US 42
people, families = tag.read_file('./sprint3/jt_validate_age.ged')
people = age.store_ages(families, people)
    #print_tables(families, people)
print('US42 - Reject illegitamite Dates:', age.calc_ages(people))
