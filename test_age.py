import unittest
from age import *
from tag_parse import *

class TestAge(unittest.TestCase):

    def test_age_less_than_150(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertIn('ERROR', less_than_one_fifty('@I1JT01@', people))
    
    def test_marrige_after_fourteen(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertIn('ERROR', marrige_after_fourteen('@I1JT01@', people))

    def test_birth_b4_marr(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        for key in people:
            self.assertIsNotNone('ERROR', check_birth_before_marr(key, people))

    def test_birth_b4_death(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        for key in people:
            self.assertIsNotNone('ERROR', check_birth_before_death(key, people))

    def test_mar_b4_death(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        for key in people:
            self.assertIsNotNone('ERROR', mar_b4_death(key, people))
    
    def test_div_b4_death(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        for key in people:
            self.assertIsNotNone('ERROR', div_b4_death(key, people))

    def test_datesBeforeCurrent(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertIn("ERROR", datesBeforeCurrent(people, families))

    def test_birth_before_death_of_parents(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        for fam in families:
            if('CHIL' in families[fam].keys()):
                for kid in families[fam]['CHIL']:
                    self.assertIsNotNone('ERROR',birth_before_death_of_parents(kid, fam, people, families))

    def test_birth_before_marr_of_parents(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        for fam in families:
            if('CHIL' in families[fam].keys()):
                for kid in families[fam]['CHIL']:
                    self.assertIsNotNone('ERROR',birth_before_marr_of_parents(kid, fam, people, families))

    def test_listRecentSurvivors(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertIn("@I2JS02@", listRecentSurvivors(people, families))

    def test_listRecentBirths(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertIn('Baby /Person/', listRecentBirths(people))

    def test_ValidateDates(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertIn('ERROR', validateDates('@I3JT95@', people))

    def test_listRecentDeaths(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertIn('John /Don/', listRecentDeaths(people))

    def test_listUpcomingBirthdays(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertIn('Will /Donovan/', listUpcomingBirthdays(people))


if __name__ == '__main__':
    unittest.main()


# Commented out old tests. Add ur tests as methods for the TestAge Class and then add them individually to travis

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
