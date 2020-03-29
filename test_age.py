import unittest
from age import *
from tag_parse import *

class TestAge(unittest.TestCase):

    def test_age_less_than_150(self):
        people, families = read_file('./sprint1/jt_sprint1.ged')
        people = store_ages(families, people)
        self.assertEqual(less_than_one_fifty('@I1@', people), 'Death Age Invalid')

if __name__ == '__main__':
    unittest.main()


# Commented out old tests. Add ur tests as methods for the TestAge Class and then add them indiviudally to travis

# def test_birth_b4_marr(key, people):
#     ans = check_birth_before_marr(key,people)
#     if("ERROR" in ans):
#         return(ans)
#     else:
#         return("test_birth_b4_marr passed")

# def test_birth_b4_death(people):
#     for key in people:
#         if('BIRT' in people[key].keys()):
#             if('Death' in people[key].keys()):
#                 if('AGE' in people[key].keys()):
#                     if(people[key]['AGE'] < 0):
#                         yield(key+"ERROR, Birth Before Death")
#                     else:
#                         yield(key+"PASS Birth Before Death")


# def test_mar_b4_death(people):
#     for key in people:
#         output = mar_b4_death(key, people)
#         if("ERROR" in output):
#             return output


# def test_div_b4_death(people):
#     for key in people:
#         output = div_b4_death(key, people)
#         if("ERROR" in output):
#             return output

# def test_date_before_current(people, families):
#     result = datesBeforeCurrent(people, families)
#     if "ERROR" in result:
#         print(result)

# def test_list_recent_births(people):
#     return listRecentBirths(people)


# def test_validateDates(people):
#     return calc_ages(people)
