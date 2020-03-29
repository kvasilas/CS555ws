import tag_parse as tag
import age 
import list_members as lister

people, families = tag.read_file('./old/proj02test.ged')
people = age.store_ages(families, people)

print(people)
print()
# print(people['xp'])
print(type(people['xp']['AGE']))
print(families)

#lister.ListLivingMarried(people)
print(lister.list_living_single(people))


#print(age.marrige_after_fourteen('@I2@', people))
#age.check_birth_before_marr('xp', people)
