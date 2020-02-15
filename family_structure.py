# A file for all tests that depend on family structure

import tag_parse as tag

people, families = tag.read_file('./proj02test.ged')

def fiveLessBirths(people, families):   # Determines whether more than any five siblings were born on the same date
    children = []   # list which will store individual lists of children separated by family
    for id in families:
        children.append(families[id]['CHIL'])
    isValid = True
    for related_children in children:   # iterate through each set of siblings
        dict_of_dates = {}
        for child in related_children:   # iterate through each child among siblings, story each unique birthdate as key and iterating value for non unique date
            try:
                dict_of_dates[people[child]['BIRT']] += 1
            except:
                dict_of_dates[people[child]['BIRT']] = 1
        for date in dict_of_dates:
            if dict_of_dates[date] > 5:   # check for number of coincident births
                isValid = False
    return isValid

print(fiveLessBirths(people, families))