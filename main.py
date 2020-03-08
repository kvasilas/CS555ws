import tag_parse as tag
import age 

people, families = tag.read_file('./proj02test.ged')
people = age.store_ages(families, people)

print(people['xp'])
print(people['xp']['DIV_AGE'])
print(families)

#print(age.marrige_after_fourteen('@I2@', people))
#age.check_birth_before_marr('xp', people)
