import test_age
import tag_parse as tag
import age
import family_structure_test


# JT User Stories
people, families = tag.read_file('./jt_list_recent_births.ged')
people = age.store_ages(families, people)
print(test_age.listRecentBirths(people))

# run validate age last because it will exit out the program when an invalid date is entered
# this is because there is no point in continuing with the rest of the program when the dates are invalid
people, families = tag.read_file('./jt_validate_age.ged')
people = age.store_ages(families, people)
print(test_age.test_validateDates(people))

