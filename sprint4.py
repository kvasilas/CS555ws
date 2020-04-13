import test_age
import tag_parse as tag
import age
import family_structure_test
from make_table import print_tables
import family_structure

# File Setup
people, families = tag.read_file('./test_case.ged')
people = age.store_ages(families, people)
print_tables(families, people)

####Error Message Prints###
print("\nGEDCOM File Errors:")
# Put Sprint 4 at top
for x in family_structure.uniqueNameBirth(people):
    print(x)
for x in family_structure.divorceBeforeMarriage(families):
    print(x)
#US08
for fam in families:
    if('CHIL' in families[fam].keys()):
        for kid in families[fam]['CHIL']:
            x = age.birth_before_marr_of_parents(kid, fam, people, families)
            if(x):
                print(x)
#US09
for fam in families:
    if('CHIL' in families[fam].keys()):
        for kid in families[fam]['CHIL']:
            x = age.birth_before_death_of_parents(kid, fam, people, families)
            if(x):
                print(x)


# End sprint 4
# JD User Stories
# Sprint 1
print(family_structure.fiveLessBirths(people, families))
print(family_structure.fifteenLessSiblings(families))
# Sprint 2
print(family_structure.noChildMarry(families))
print(age.datesBeforeCurrent(people, families))
# Sprint 3
print(family_structure.uniqueFam(people, families))
print(family_structure.uniqueFirst(people, families))


# RT User Stories
# Sprint 1
for x in family_structure.parents_not_too_old(people, families):
    print(x)
for x in family_structure.male_last_names_align(people, families):
    print(x)
# Sprint 2
for x in family_structure.noSiblingMarriage(families):
    print(x)
for x in family_structure.correctGender(families, people):
    print(x)
# Sprint 3
for x in family_structure.noCousinMarriage(families):
    print(x)
for x in family_structure.noNieceNephewMarriage(families):
    print(x)
#Sprint 4
for x in family_structure.uniqueNameBirth(people):
    print(x)
for x in family_structure.divorceBeforeMarriage(families):
    print(x)


# JT User Stories
# Sprint 1
for person in people:
    x = age.less_than_one_fifty(person, people)
    if (x != None):
        print(x)
for person in people:
    x = age.marrige_after_fourteen(person, people)
    if (x != None):
        print(x)
# Sprint 3
for person in people:
   x = age.validateDates(person, people)
   if (x != None):
       print(x)
for family in families:
    x = age.validateDates(family, families)
    if x:
        print(x)


# KV User Stories
##sprint 1
#US02
for key in people:
    x = age.check_birth_before_marr(key, people)
    if (x != None):
       print(x)
#US03
for key in people:
    x = age.check_birth_before_death(key, people)
    if (x != None):
       print(x)
##sprint 2
#US05
for key in people:
    x = age.mar_b4_death(key, people)
    if (x != None):
       print(x)
#US06
for key in people:
    x = age.div_b4_death(key, people)
    if (x != None):
       print(x)

print(family_structure.uniqueIndividualIDs(people))
print(family_structure.uniqueFamilyIDs(families))


####Information User story demonstrations###
print("\nUser Story Demonstrations:")

#Sprint 4 here
print("US37: List Recent Survivors: ", age.listRecentSurvivors(people, families))
print("US32: List Multiple Births:\n{}".format(family_structure.listSameBirth(people, families)))

print("US36: List recent deaths: ", age.listRecentDeaths(people))
print("US38: List upcoming birthdays: ", age.listUpcomingBirthdays(people))

# JT User Stories
# Sprint 2
print("US29: List of deceased people: ", family_structure.listDeceased(people))
# Sprint 3
print("US35: List of recent births: ", age.listRecentBirths(people))
#KV User Stories
##sprint 3
#US30
resp, val = family_structure.ListLivingMarried(people)
print(resp, val, sep=' ')
#US31
resp, val = family_structure.ListLivingSingle(people)
print(resp, val, sep=' ')