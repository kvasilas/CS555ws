import tag_parse as tag
import age

people, families = tag.read_file('./proj02test.ged')
print(age.curr_age(people))
