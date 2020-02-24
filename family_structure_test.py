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