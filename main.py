import tag_parse as tag
import age 
from make_table import print_tables
import family_structure_test
from datetime import timedelta, datetime


# people, families = tag.read_file('./old/proj02test.ged')
# people = age.store_ages(families, people)

# print(people['rn'].keys())
# print(families['f2'].keys())
# #print(type(people['xp']['AGE']))
# print()

# print_tables(families, people)
# test single
# married not divorced dead - 


people, families = tag.read_file('./sprint4/kv_s4.ged')
people = age.store_ages(families, people)
print_tables(families, people)


for fam in families:
      for kid in families[fam]['CHIL']:
            x = age.birth_before_death_of_parents(kid, fam, people, families)
            y = age.birth_before_marr_of_parents(kid, fam, people, families)
            if(x):
                  print(x)
            if(y):
                  print(y)