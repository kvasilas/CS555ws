import tag_parse as tag
import age 
from make_table import print_tables
import family_structure_test


# people, families = tag.read_file('./old/proj02test.ged')
# people = age.store_ages(families, people)

# print(people['rn'].keys())
# print(families['f2'].keys())
# #print(type(people['xp']['AGE']))
# print()

# print_tables(families, people)
# test single
# married not divorced dead - 


people, families = tag.read_file('./sprint3/kv_sprint3.ged')
people = age.store_ages(families, people)
print_tables(families, people)
print("US30 - List living Married",
      family_structure_test.test_ListLivingMarried(people))
print("US30 - List living Single",
      family_structure_test.test_ListLivingSingle(people))
print('\n##########################################################################\n')
