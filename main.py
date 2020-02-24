import tag_parse as tag
import age 

people, families = tag.read_file('./jt_sprint1.ged')
people = age.store_ages(families, people)

print(people['@I2@']['MARR_AGE'])
print(age.marrige_after_fourteen('@I2@', people))
#age.check_birth_before_marr('xp', people)
