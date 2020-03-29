# A file for all tests that depend on family structure

import tag_parse as tag
import age
from collections import defaultdict 


def fiveLessBirths(people, families):   # Determines whether more than five siblings were born on the same date
    children = []   # list which will store individual lists of children separated by family
    for id in families:
        try:
            children.append(families[id]['CHIL'])
        except:
            pass
    isValid = True
    for related_children in children:   # iterate through each set of siblings
        dict_of_dates = {}
        for child in related_children:   # iterate through each child among siblings, storing each unique birthdate as
            # key and iterating value for non unique date - US14
            try:
                dict_of_dates[people[child]['BIRT']] += 1
            except:
                dict_of_dates[people[child]['BIRT']] = 1
        for date in dict_of_dates:
            if dict_of_dates[date] > 5:   # check for number of coincident births
                isValid = False
    if not isValid:
        return "More than five siblings were born on the same day"


def fifteenLessSiblings(families):   # Tests that each family has less than fifteen siblings - US15
    isValid = True
    for family in families:
        if len(families[family]["CHIL"]) > 14:
                isValid = False
        if not isValid:
            return "A family contains more than fourteen siblings"


def parents_not_too_old(people, family, families):
    motherid = families[family]['WIFE']
    fatherid = families[family]['HUSB']
    error_str = ""
    for child in families[family]['CHIL']:
        if(age.get_age(motherid, people) - age.get_age(child, people) >= 60):
            error_str += "Mother is too old - ID: " + child + " | "
        if (age.get_age(fatherid, people) - age.get_age(child, people) >= 80):
            error_str += "Father is too old - ID: " + child + " | "
    if (error_str != ""):
        return "ERROR: " + error_str


def get_last_name(key, people):
    name = people[key]['NAME'][:-1]
    while (name[0] != "/"):
        name = name[1:]
    return name[1:]


def male_last_names_align(people, family, families):
    male_ln = get_last_name(families[family]['HUSB'],people)
    for child in families[family]['CHIL']:
        if (people[child]['SEX'] == 'M'):
            if (get_last_name(child,people) != male_ln):
                return "ERROR: Male child's last name does not match father's - ID: " + child


def noChildMarry(families):
    father_dict = getFatherChildren(families)
    mother_dict = getMotherChildren(families)

    for family in families:
        wife = families[family]["WIFE"]
        husband = families[family]['HUSB']

        try:
            if husband in mother_dict[wife]:
                return "ERROR: FAMILY: US17 A mother ({}) is married to her child ({})".format(wife, husband)
        except:
            pass
        try:
            if wife in father_dict[husband]:
                return "ERROR: FAMILY: US17 A father ({}) is married to his child ({})".format(husband, wife)
        except:
            pass

    return ""

def getFatherChildren(families):   # Returns a dictionary with key being a father and value being list of their children
    fathers = {}
    for family in families:
        if 'HUSB' not in families[family] or 'CHIL' not in families[family]:
            continue
        if families[family]['HUSB'] in fathers:
            fathers[families[family]["HUSB"]].append(families[family]["CHIL"])
        else:
            fathers[families[family]["HUSB"]] = families[family]["CHIL"]
    return fathers

def getMotherChildren(families):
    mothers = {}
    for family in families:
        if 'WIFE' not in families[family] or 'CHIL' not in families[family]:
            continue
        if families[family]['WIFE'] in mothers:
            mothers[families[family]["WIFE"]].append(families[family]["CHIL"])
        else:
            mothers[families[family]["WIFE"]] = families[family]["CHIL"]
    return mothers

def uniqueIndividualIDs(people):
    bv = defaultdict(int)
    for individual in people:
        print(people[individual]['ID'])
        bv[people[individual]['ID']] += 1 
    for i in bv:
        if bv[i] > 1:
            return ("ERROR: INDIVIDUAL: US22: ID is not unique " + i)
    return "All ID's are unique"


def uniqueFamilyIDs(families):
    bv = defaultdict(int)
    for family in families:
        print(families[family]['ID'])
        bv[families[family]['ID']] += 1 
    for i in bv:
        if bv[i] > 1:
            return ("ERROR: FAMILIY: US22: Family ID is not unique " + i)
    return "All Family ID's are unique"

def listDeceased(people):
    dead_people = {}
    for person in people:
        if('DEAT' in people[person].keys()):
            dead_people[people[person]['ID']] = people[person]['NAME']
        else:
            continue
    return dead_people

def noSiblingMarriage(families):
    errors = []
    for family in families:
        husbandID = families[family]['HUSB']
        wifeID = families[family]['WIFE']
        for fam in families:
            if 'CHIL' in families[fam]:
                if (husbandID in families[fam]['CHIL'] and wifeID in families[fam]['CHIL']):
                    errors.append("ERROR: FAMILY: US18: " + husbandID + " & " + wifeID + ": Siblings cannot be married")
    return errors

def correctGender(families, people):
    errors = []
    for family in families:
        husbandID = families[family]['HUSB']
        wifeID = families[family]['WIFE']
        if (people[husbandID]['SEX'] != 'M'):
            errors.append("ERROR: FAMILY: US21: " + husbandID + ": Gender of Father is Female")
        if (people[wifeID]['SEX'] != 'F'):
            errors.append("ERROR: FAMILY: US21: " + wifeID + ": Gender of Mother is Male")
    return errors


def noNieceNephewMarriage(families):
    errors = []
    for f in families:
        husbandID = families[f]['HUSB']
        wifeID = families[f]['WIFE']
        for fam in families:
            if ('CHIL' in families[fam]):
                nntype = None
                if (husbandID in families[fam]['CHIL']):
                    nntype = "nephew"
                if (wifeID in families[fam]['CHIL']):
                    nntype = "niece"
                if (nntype != None):
                    father = families[fam]['HUSB']
                    mother = families[fam]['WIFE']
                    for family in families:
                        if ('CHIL' in families[family]):
                            if ((father in families[family]['CHIL']) or (mother in families[family]['CHIL'])):
                                if ((nntype == "nephew") and (wifeID in families[family]['CHIL'])):
                                    errors.append("ERROR: FAMILY: US20: " + wifeID + " & " + husbandID + ": Aunts and nephews cannot be married.")
                                if ((nntype == "niece") and (husbandID in families[family]['CHIL'])):
                                    errors.append("ERROR: FAMILY: US20: " + husbandID + " & " + wifeID + ": Uncles and nieces cannot be married.")
    return errors


def noCousinMarriage(families):
    errors = []
    for f in families:
        husbandID = families[f]['HUSB']
        wifeID = families[f]['WIFE']
        husbMom, husbDad, wifeMom, wifeDad = None, None, None, None
        for fam in families:
            if ('CHIL' in families[fam]):
                if (husbandID in families[fam]['CHIL']):
                    husbMom = families[fam]['WIFE']
                    husbDad = families[fam]['HUSB']
                if (wifeID in families[fam]['CHIL']):
                    wifeMom = families[fam]['WIFE']
                    wifeDad = families[fam]['HUSB']
        for family in families:
            if ('CHIL' in families[family]):
                if ((husbMom != None) and (wifeMom != None)):
                    if((husbMom in families[family]['CHIL']) and (wifeMom in families[family]['CHIL'])):
                        errors.append("ERROR: FAMILY: US19: " + husbandID + " & " + wifeID + ": First cousins cannot be married.")
                if ((husbMom != None) and (wifeDad != None)):
                    if((husbMom in families[family]['CHIL']) and (wifeDad in families[family]['CHIL'])):
                        errors.append("ERROR: FAMILY: US19: " + husbandID + " & " + wifeID + ": First cousins cannot be married.")
                if ((husbDad != None) and (wifeMom != None)):
                    if((husbDad in families[family]['CHIL']) and (wifeMom in families[family]['CHIL'])):
                        errors.append("ERROR: FAMILY: US19: " + husbandID + " & " + wifeID + ": First cousins cannot be married.")
                if ((husbDad != None) and (wifeDad != None)):
                    if((husbDad in families[family]['CHIL']) and (wifeDad in families[family]['CHIL'])):
                        errors.append("ERROR: FAMILY: US19: " + husbandID + " & " + wifeID + ": First cousins cannot be married.")
    return errors


def uniqueFam(people, families):   # US24
    print(families)
    print(people)
    fam_dict = {}
    for famID in families:
        husbID = families[famID]['HUSB']
        husb = people[husbID]['NAME']
        wifeID = families[famID]['WIFE']
        wife = people[wifeID]['NAME']
        marr = families[famID]['MARR']
        key_string = husb + wife + marr

        if key_string in fam_dict:
            return False
        else:
            fam_dict[key_string] = True
    return True

def uniqueFirst(people, families):   # US25
    for familyID in families:
        fam_dict = {}
        if 'CHIL' in families[familyID]:
            for childID in families[familyID]['CHIL']:
                key_string = people[childID]['NAME'] + people[childID]['BIRT']

                if key_string in fam_dict:
                    return False
                else:
                    fam_dict[key_string] = True
    return True

def ListLivingMarried(people):
    alive_married_list = []
    for key in people:
        if not age.is_dead(key, people):  # is alive?
            if 'MARR_AGE' in people[key].keys() and 'DIV_AGE' not in people[key].keys():
                alive_married_list.append(people[key]['NAME'])
    return alive_married_list


def ListLivingSingle(people):
    #List all living people over 30 who have never been married in a GEDCOM file
    alive_single_list = []
    for key in people:
        if not age.is_dead(key, people):  # is alive?
            if('MARR_AGE' not in people[key].keys() and people[key]['AGE'] >= 30):
                alive_single_list.append(people[key]['NAME'])
    return alive_single_list

