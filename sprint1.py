import test_age
import tag_parse as tag
import age

# #store all information
# people, families = tag.read_file('./kvSprint1.ged')
# people = age.store_ages(families, people)

# #KV User Stories
# print(test_age.test_birth_b4_marr('aa', people))
# #print(test_age.test_birth_b4_death(people))

#JT User Stories
people, families = tag.read_file('./jt_sprint1.ged')
people = age.store_ages(families, people)
print(test_age.test_less_than_one_fifty('@I1@', people))
print(test_age.test_marrige_after_fourteen('@I2@', people))
#JD User Stories
#RT User Stories
