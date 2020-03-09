import family_structure

def fiveLessBirthsTest(people, families):
    if family_structure.fiveLessBirths(people, families) == "More than five siblings were born on the same day":
        return "Error, five or more births"

def fifteenLessSiblingsTest(families):
    if family_structure.fifteenLessSiblings(families) == "A family contains more than fourteen siblings":
        return "Error, fifteen or more siblings in a family"

def parentsNotTooOldTest(people, family, families):
    ans = family_structure.parents_not_too_old(people, family, families)
    if ("ERROR" in ans):
        return ans

def maleLastNameTest(people, family, families):
    ans = family_structure.male_last_names_align(people, family, families)
    if ("ERROR" in ans):
        return ans

def noChildMarryTest(families):
    ans = family_structure.noChildMarry(families)
    if ("ERROR" in ans):
        return ans

def uniqueIndividualIDsTest(people):
    result = family_structure.uniqueIndividualIDs(people)
    if ("ERROR" in result):
        return result
    else:
        return "All Individual ID's are unique"

def uniqueFamilyIDsTest(families):
    result = family_structure.uniqueFamilyIDs(families)
    if ("ERROR" in result):
        return result
    else:
        return "All Family ID's are unique"

def listDeceasedTest(people):
    result = family_structure.listDeceased(people)
    if ("ERROR" in result):
        return result
    else:
        return "Here are all the dead people: " + str(result)

def noSiblingMarriageTest(families):
    errors = family_structure.noSiblingMarriage(families)
    for x in errors:
        print(x)

def correctGenderTest(families, people):
    errors = family_structure.correctGender(families, people)
    for x in errors:
        print(x)