# A file for all tests that depend on family structure

import tag_parse as tag
import age
from collections import defaultdict
from datetime import datetime


def fiveLessBirths(people, families):   # Determines whether more than five siblings were born on the same date
    children = {}   # dict which will store individual lists of children by family id
    for fam_id in families:
        if 'CHIL' in families[fam_id]:
            children[fam_id] = families[fam_id]['CHIL']
    for fam_id in children:   # iterate through each set of siblings
        dict_of_dates = {}
        for child in children[fam_id]:   # iterate through each child among siblings, storing each unique birthdate as
            # key and iterating value for non unique date - US14
            if 'BIRT' in people[child]:
                if people[child]['BIRT'] in dict_of_dates:
                    dict_of_dates[people[child]['BIRT']].append(child)
                else:
                    dict_of_dates[people[child]['BIRT']] = [child]
        for date in dict_of_dates:
            if len(dict_of_dates[date]) > 5:   # check for number of coincident births
                return "ERROR: FAMILY: US14: {} all have than same birth in family {} - [NOT] fewer than five births".format(dict_of_dates[date], fam_id)
    return True


def fifteenLessSiblings(families):   # Tests that each family has less than fifteen siblings - US15
    for family in families:
        if 'CHIL' in families[family]:
            if len(families[family]["CHIL"]) > 14:
                return "ERROR: FAMILY: US15: Family {} has more than fourteen siblings".format(family)
    return True


def parents_not_too_old(people, families):
    errors = []
    for family in families:
        if(('WIFE' in families[family]) and ('CHIL' in families[family])):
            motherid = families[family]['WIFE']
            for child in families[family]['CHIL']:
                if ((motherid in people) and (child in people)):
                    if (age.get_age(motherid, people) - age.get_age(child, people) >= 60):
                        errors.append("ERROR: FAMILY: US12: " + family + " | " + motherid + " & " + child + ": Mother is too old")
        if(('HUSB' in families[family]) and ('CHIL' in families[family])):
            fatherid = families[family]['HUSB']
            for child in families[family]['CHIL']:
                if ((fatherid in people) and (child in people)):
                    if (age.get_age(fatherid, people) - age.get_age(child, people) >= 80):
                        errors.append("ERROR: FAMILY: US12: " + family + " | " + fatherid + " & " + child + ": Father is too old")
    if (errors != []):
        return errors
    return True

def get_last_name(key, people):
    name = people[key]['NAME']
    while (" " in name):
        name = name[1:]
    if(name[0] == "/"):
        name = name[1:-1]
    return name


def male_last_names_align(people, families):
    errors = []
    for family in families:
        if ('HUSB' in families[family]):
            if (families[family]['HUSB'] in people):
                fatherid = families[family]['HUSB']
                male_ln = get_last_name(fatherid, people)
                if('CHIL' in families[family]):
                    for child in families[family]['CHIL']:
                        if (child in people):
                            if ('SEX' in people[child]):
                                if (people[child]['SEX'] == 'M'):
                                    if (get_last_name(child,people) != male_ln):
                                        errors.append("ERROR: FAMILY: US16: " + family + " | " + fatherid + " & " + child
                                        + ": Father's last name '" + male_ln + "' does not match son's '" + get_last_name(child,people) + "'")
    if (errors != []):
        return errors
    return True


def noChildMarry(families):
    father_dict = getFatherChildren(families)
    mother_dict = getMotherChildren(families)

    for family in families:
        wife = families[family].get("WIFE", None)
        husband = families[family].get('HUSB', None)

        if husband in mother_dict.get(wife, []):
            return "ERROR: FAMILY: US17: A mother ({}) is married to her child ({})".format(wife, husband)
        if wife in father_dict.get(husband, []):
            return "ERROR: FAMILY: US17: A father ({}) is married to his child ({})".format(husband, wife)
    return True

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
        #print(people[individual]['ID'])
        bv[people[individual]['ID']] += 1 
    for i in bv:
        if bv[i] > 1:
            return ("ERROR: INDIVIDUAL: US22: ID is not unique " + i)
    return "All Individual ID's are unique"


def uniqueFamilyIDs(families):
    bv = defaultdict(int)
    for family in families:
        #print(families[family]['ID'])
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
        if (('HUSB' in families[family]) and ('WIFE' in families[family])):
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
        if (('HUSB' in families[family]) and ('WIFE' in families[family])):
            husbandID = families[family]['HUSB']
            wifeID = families[family]['WIFE']
            if (husbandID in people):
                if ('SEX' in people[husbandID]):
                    if (people[husbandID]['SEX'] != 'M'):
                        errors.append("ERROR: FAMILY: US21: " + family + " & " + husbandID + ": Gender of Father is Female")
            if (wifeID in people):
                if ('SEX' in people[wifeID]):
                    if (people[wifeID]['SEX'] != 'F'):
                        errors.append("ERROR: FAMILY: US21: " + family + " & " + wifeID + ": Gender of Mother is Male")
    return errors


def noNieceNephewMarriage(families):
    errors = []
    for f in families:
        if (('HUSB' in families[f]) and ('WIFE' in families[f])):
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
                        father, mother = None, None
                        if ('HUSB' in families[fam]):
                            father = families[fam]['HUSB']
                        if ('WIFE' in families[fam]):
                            mother = families[fam]['WIFE']
                        for family in families:
                            if ('CHIL' in families[family]):
                                if ((father in families[family]['CHIL']) or (mother in families[family]['CHIL'])):
                                    if ((nntype == "nephew") and (wifeID in families[family]['CHIL'])):
                                        errors.append("ERROR: FAMILY: US20: " + wifeID + " & " + husbandID + ": Aunts and nephews cannot be married.")
                                    if ((nntype == "niece") and (husbandID in families[family]['CHIL'])):
                                        errors.append("ERROR: FAMILY: US20: " + husbandID + " & " + wifeID + ": Uncles and nieces cannot be married.")
    if(errors != None):
        return errors
    else:
        return True


def noCousinMarriage(families):
    errors = []
    for f in families:
        if (('HUSB' in families[f]) and ('WIFE' in families[f])):
            husbandID = families[f]['HUSB']
            wifeID = families[f]['WIFE']
            husbMom, husbDad, wifeMom, wifeDad = None, None, None, None
            for fam in families:
                if ('CHIL' in families[fam]):
                    if (husbandID in families[fam]['CHIL']):
                        if ('WIFE' in families[fam]):
                            husbMom = families[fam]['WIFE']
                        if ('HUSB' in families[fam]):
                            husbDad = families[fam]['HUSB']
                    if (wifeID in families[fam]['CHIL']):
                        if ('WIFE' in families[fam]):
                            wifeMom = families[fam]['WIFE']
                        if ('HUSB' in families[fam]):
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
    if(errors != []):
        return errors
    else:
        return True


def uniqueFam(people, families):   # US24
    fam_dict = {}
    for famID in families:
        husbID = families[famID].get('HUSB', None)
        husb = people.get(husbID, False)
        if husb:
            husb = husb.get('NAME', False)
        wifeID = families[famID].get('WIFE', None)
        wife = people.get(wifeID, False)
        if wife:
            wife = wife.get('NAME', False)
        marr = families[famID].get('MARR', False)
        marr = marr.strftime("%m/%d/%Y")
        if not husb or not wife or not marr:
            continue
        key_string = husb + wife + marr

        if key_string in fam_dict:
            return "ERROR: FAMILY: US24: Families: " + famID + " and " + fam_dict[key_string] + " seem to be duplicates"
        else:
            fam_dict[key_string] = famID
    return True

def uniqueFirst(people, families):   # US25
    for familyID in families:
        fam_dict = {}
        if 'CHIL' in families[familyID]:
            for childID in families[familyID]['CHIL']:
                if 'BIRT' not in people[childID]:
                    continue
                key_string = people[childID]['NAME'] + people[childID]['BIRT'].strftime("%m/%d/%Y")

                if key_string in fam_dict:
                    return "ERROR: INDIVIDUAL: US25: " + people[childID]['NAME'] + " appears twice within familiy id: " + familyID
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

