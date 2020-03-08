import test_age
import tag_parse as tag
import age

#KV User Stories
people, families = tag.read_file('./kvSprint2.ged')
people = age.store_ages(families, people)
print(test_age.test_mar_b4_death('xp', people))
print(test_age.test_div_b4_death('xp', people))


#JT User Stories


#JD User Stories


#RT User Stories
