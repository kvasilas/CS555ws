import tag_parse as tag
import age

people, families = tag.read_file('./proj02test.ged')
print(families)
people = age.store_ages(families, people)

age.check_birth_before_marr('xp', people)
