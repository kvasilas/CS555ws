import tag_parse as tag
import age

people, families = tag.read_file('./runme.ged')
print(people)
print(age.death_age('xp', people))
people = age.store_ages(families, people)

#age.check_birth_before_marr('xp', people)
