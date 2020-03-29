import test_age
import tag_parse as tag
import age
import family_structure_test
from make_table import print_tables

#KV User Stories
#US30 -List living married
#US31 -List living single
people, families = tag.read_file('./sprint3/kv_sprint3.ged')
people = age.store_ages(families, people)
print('KV User Stories: US30 - List living married and US31 -List living single')
print_tables(families, people)
print("US30 - List living Married: ", family_structure_test.test_ListLivingMarried(people))
print("US31 - List living Single over 30: ", family_structure_test.test_ListLivingSingle(people))
print('\n##########################################################################\n')



#RT User Stories
people, families = tag.read_file('./sprint3/rtSprint3.ged')
people = age.store_ages(families, people)
print_tables(families, people)
family_structure_test.noNieceNephewMarriageTest(families)
family_structure_test.noCousinMarriageTest(families)
print('\n##########################################################################\n')



# JT User Stories
#US35
people, families = tag.read_file('./sprint3/jt_list_recent_births.ged')
people = age.store_ages(families, people)
print('JT user stories US35 and US42')
print_tables(families, people)
print("US35 - Recent Births:", age.listRecentBirths(people))

# run validate age last because it will exit out the program when an invalid age is entered
# this is because there is no point in continuing with the rest of the program when the dates are invalid
#US 42
people, families = tag.read_file('./sprint3/jt_validate_age.ged')
people = age.store_ages(families, people)
print_tables(families, people)
print('US42 - Reject illegitamite Dates:', age.calc_ages(people))

