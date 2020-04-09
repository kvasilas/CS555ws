import unittest

from family_structure import *
from tag_parse import *
from age import *

class TestFamStruct(unittest.TestCase):

    def test_ListLivingMarried(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertNotEqual(ListLivingMarried(people), [])

    def test_ListLivingSingle(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertNotEqual(ListLivingSingle(people), [])

    def test_fiveLessBirths(self):
        people, families = read_file('./test_case.ged')
        self.assertIn("ERROR", fiveLessBirths(people, families))

    def test_fifteenLessSiblings(self):
        people, families = read_file('./test_case.ged')
        self.assertIn("ERROR", fifteenLessSiblings(families))

    def test_noChildMarry(self):
        people, families = read_file('./test_case.ged')
        self.assertIn("ERROR", noChildMarry(families))

    def test_uniqueFirst(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertIn("ERROR", uniqueFirst(people, families))

    def test_uniqueFam(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertIn("ERROR", uniqueFam(people, families))
    
    def test_cousinMarriage(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertNotEqual(True, noCousinMarriage(families))
    
    def test_nieceNephewMarriage(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertNotEqual(True, noNieceNephewMarriage(families))
    
    def test_siblingMarriage(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertNotEqual([], noSiblingMarriage(families))
    
    def test_correctGender(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertNotEqual([], correctGender(families, people))
    
    def test_parentAge(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertNotEqual(True, parents_not_too_old(people, families))
    
    def test_maleNames(self):
        people, families = read_file('./test_case.ged')
        people = store_ages(families, people)
        self.assertNotEqual(True, male_last_names_align(people, families))

if __name__ == '__main__':
    unittest.main()





# def fiveLessBirthsTest(people, families):
#     if family_structure.fiveLessBirths(people, families) == "More than five siblings were born on the same day":
#         return "Error, five or more births"

# def fifteenLessSiblingsTest(families):
#     if family_structure.fifteenLessSiblings(families) == "A family contains more than fourteen siblings":
#         return "Error, fifteen or more siblings in a family"

# def parentsNotTooOldTest(people, family, families):
#     ans = family_structure.parents_not_too_old(people, family, families)
#     if ("ERROR" in ans):
#         return ans

# def maleLastNameTest(people, family, families):
#     ans = family_structure.male_last_names_align(people, family, families)
#     if ("ERROR" in ans):
#         return ans

# def noChildMarryTest(families):
#     ans = family_structure.noChildMarry(families)
#     if ("ERROR" in ans):
#         return ans

# def uniqueIndividualIDsTest(people):
#     result = family_structure.uniqueIndividualIDs(people)
#     if ("ERROR" in result):
#         return result
#     else:
#         return "All Individual ID's are unique"

# def uniqueFamilyIDsTest(families):
#     result = family_structure.uniqueFamilyIDs(families)
#     if ("ERROR" in result):
#         return result
#     else:
#         return "All Family ID's are unique"

# def listDeceasedTest(people):
#     result = family_structure.listDeceased(people)
#     if ("ERROR" in result):
#         return result
#     else:
#         return "Here are all the dead people: " + str(result)

# def noSiblingMarriageTest(families):
#     errors = family_structure.noSiblingMarriage(families)
#     for x in errors:
#         print(x)

# def correctGenderTest(families, people):
#     errors = family_structure.correctGender(families, people)
#     for x in errors:
#         print(x)

# def noNieceNephewMarriageTest(families):
#     errors = family_structure.noNieceNephewMarriage(families)
#     if errors != True:
#         for x in errors:
#             print(x)

# def noCousinMarriageTest(families):
#     errors = family_structure.noCousinMarriage(families)
#     if errors != True:
#         for x in errors:
#             print(x)

# def test_ListLivingMarried(people):
#     return(family_structure.ListLivingMarried(people))

# def test_ListLivingSingle(people):
#     return(family_structure.ListLivingSingle(people))

# def test_unique_fam(people, families):
#     tmp = family_structure.uniqueFam(people, families)
#     if "ERROR" in tmp:
#         return tmp
#     else:
#         return "Pass"

# def test_unique_first(people, families):
#     tmp = family_structure.uniqueFirst(people, families)
#     if "ERROR" in tmp:
#         return tmp
#     else:
#         return "Pass"
