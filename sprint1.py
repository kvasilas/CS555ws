import test_age
import tag_parse as tag
import age

#store all information
people, families = tag.read_file('./sprint1.ged')
people = age.store_ages(families, people)

#KV User Stories
print(test_age.test_birth_b4_marr('aa', people))
print(test_age.test_birth_b4_death(people))

#JT User Stories
#JD User Stories
#RT User Stories
