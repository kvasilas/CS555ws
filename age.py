from datetime import timedelta, datetime
import copy

def calc_ages(people): #runs on whole dictionary
    today = datetime.now()
    for key in people:
        _ = validateDates(key, people) # check that the dates are valid
        # print(err)
        if('BIRT' in people[key].keys()):
            if(is_dead(key, people) == False):
                people[key]['ALIVE'] = True
                try:
                    bday = datetime.strptime(people[key]['BIRT'], '%d %b %Y')
                except:
                    Warning("ERROR: FAMILY: US22: Family ID is not unique")
                people[key]['BIRT'] = datetime.strptime(people[key]['BIRT'], '%d %b %Y')
                people[key]['AGE'] = int((today - bday).days/365.2425)
            else:
                #if dead age is their last living age people[key]['AGE']
                people[key]['ALIVE'] = False
                age = death_age(key, people)
                people[key]['AGE'] = age
                # if(age < 0): #death before birth
                #     print("ERROR: Invalid death date, death before birth")
                # else:
                #     people[key]['AGE']= age
    return people

def is_dead(key, people): #by person
    if('DEAT' in people[key].keys()):
        return True
    else:
        return False

def get_age(key, people): #by person
    #not totally needed but it could make life easy maybe.  can also just do a ditct call
    return (people[key]['AGE'])


def death_age(key, people): #by person
    if('DEAT' in people[key].keys()):
        # print(people[key]['DEAT'])
        # print(key, type(people[key]['DEAT']), people[key]['DEAT'])
        if(type(people[key]['DEAT']) == str):
            dday = datetime.strptime(people[key]['DEAT'], '%d %b %Y')
            people[key]['DEAT'] = datetime.strptime(people[key]['DEAT'], '%d %b %Y')
            bday = datetime.strptime(people[key]['BIRT'], '%d %b %Y')
            people[key]['BIRT'] = datetime.strptime(people[key]['BIRT'], '%d %b %Y')
            d_age = int((dday-bday).days/365.2425)
        else:
            d_age = int(
                (people[key]['DEAT'] - people[key]['BIRT']).days/365.2425)
        return(d_age)
        

def marr_and_div_ages(families, people): #runs on whole dictionary
    for key in families:
        if ('MARR' in families[key]):
            marr_date = datetime.strptime(families[key]['MARR'], '%d %b %Y')
            if ('DIV' in families[key]):
                div_date = datetime.strptime(families[key]['DIV'], '%d %b %Y')
                people[families[key]['HUSB']]['DIV_AGE'] = int((div_date-people[families[key]['HUSB']]['BIRT']).days/365.2425)
                people[families[key]['WIFE']]['DIV_AGE'] = int((div_date-people[families[key]['WIFE']]['BIRT']).days/365.2425)
            try:
                people[families[key]['HUSB']]['MARR_AGE'] = int((marr_date-people[families[key]['HUSB']]['BIRT']).days/365.2425)
            except:
                Warning("ERROR: INDIVIDUAL: US22: ID is not unique ")

            try:
                people[families[key]['WIFE']]['MARR_AGE'] = int((marr_date-people[families[key]['WIFE']]['BIRT']).days/365.2425)
            except:
                Warning("ERROR: INDIVIDUAL: US22: Individual ID is not unique ")
    return(people)

def check_birth_before_marr(key, people):
    if('MARR_AGE' in people[key].keys()):
        if(people[key]['MARR_AGE'] < 0):
            return("ERROR: INDIVIDUAL: US02: "+people[key]["NAME"]+" Married before birth")

def check_birth_before_death(key, people):
    if('BIRT' in people[key].keys()):
        if('Death' in people[key].keys()):
            if('AGE' in people[key].keys()):
                if(people[key]['AGE'] < 0):
                    return("ERROR: INDIVIDUAL: US03: "+people[key]["NAME"]+" Birth Before Death")

def store_ages(families, people):
    people = calc_ages(people)
    people = marr_and_div_ages(families, people)
    return people

def less_than_one_fifty(key, people):
    # Ticket US07 - Death should be less than 150 years after 
    # birth for dead people, and current date should be less 
    # than 150 years after birth for all living people
    if(is_dead(key, people) is True):
        if(death_age(key, people) >= 150):
            return("ERROR: US07: DEATH AGE INVALID" + people[key]['ID'])
    if(is_dead(key, people) is False):
        if('AGE' in people[key].keys()):
            if(get_age(key, people) >= 150):
                return("ERROR: US07: CURRENT AGE INVALID" + people[key]['ID'])
    
def marrige_after_fourteen(key, people):
    # Ticket US10 - Marriage should be at least 14 years after birth 
    # of both spouses (parents must be at least 14 years old)
    if('MARR_AGE' in people[key].keys()):
        if(people[key]['MARR_AGE'] <= 14):
            return("ERROR: INDIVIDUAL: US10: Marrige under the age of 14 is invalid: " + people[key]['ID'])
    else:
        return 


def mar_b4_death(key, people):
    if('MARR_AGE' in people[key].keys() and 'AGE' in people[key].keys()):
        if(people[key]['MARR_AGE'] > people[key]['AGE']):
            return "ERROR: INDIVIDUAL: US05 Person '{}' was married after their death".format(key)

def div_b4_death(key, people):
    if('DIV_AGE' in people[key].keys()):
        if(people[key]['DIV_AGE'] > people[key]['AGE']):
            return "ERROR: INDIVIDUAL: US06 Person '{}' was divorced after their death ".format(key)

def convertFamiliesToDT(families):   # Converts each family date to datetime
    familiesDT = copy.deepcopy(families)
    for family in familiesDT:
        if 'MARR' in familiesDT[family]:
            familiesDT[family]['MARR'] = datetime.strptime(familiesDT[family]['MARR'], '%d %b %Y')
        if 'DIV' in familiesDT[family]:
            familiesDT[family]['DIV'] = datetime.strptime(familiesDT[family]['DIV'], '%d %b %Y')
    return familiesDT

def datesBeforeCurrent(people, families):
    today = datetime.now()
    families_dict = convertFamiliesToDT(families)
    for person in people:
        if people[person].get('BIRT', today) > today:
            return "ERROR: INDIVIDUAL: US01 {} has a birthday ({}) after today".format(person, people[person]['BIRT'])
        if "DEAT" in people[person]:
            if people[person]["DEAT"] > today:
                return "ERROR: INDIVIDUAL: US01 {} has died ({}) after today".format(person, people[person]['DEAT'])
    for family in families_dict:
        if families_dict[family].get('MARR', today) > today:
            return "ERROR: FAMILY: US01 {} family has a marriage ({}) after today".format(family, families[family]['MARR'])
        if "DIV" in families_dict[family]:
            if families_dict[family]["DIV"] > today:
                return "ERROR: FAMILY: US01 {} family has a divorce ({}) after today".format(family, families[family]['DIV'])

def listRecentBirths(people):
    thirtyDaysAgo = datetime.now() - timedelta(30)
    newly_borns = []
    for person in people:
        if('BIRT' in people[person].keys()):  
            if people[person]['BIRT'] > thirtyDaysAgo:
                newly_borns.append(people[person]['NAME'])
            else:
                continue
    return newly_borns

def validateDates(person, people):
    if (is_dead(person, people) == False):
        try:
            _ = datetime.strptime(people[person]['BIRT'], '%d %b %Y')
        except:
            Warning("ERROR: PERSON: US42: Error parsing GEDCOM file - Invalid Birth Date for person: "+ people[person]['ID']) 
            return("ERROR: PERSON: US42: Error parsing GEDCOM file - Invalid Birth Date for person: "+ people[person]['ID']) 
    else:
        try:
            _ = datetime.strptime(people[person]['BIRT'], '%d %b %Y')
        except:
            Warning("ERROR: PERSON: US42: Error parsing GEDCOM file - Invalid Birth Date for person: " + people[person]['ID'])
            return("ERROR: PERSON: US42: Error parsing GEDCOM file - Invalid Birth Date for person: "+ people[person]['ID']) 
        try:
            _ = datetime.strptime(people[person]['DEAT'], '%d %b %Y')
        except:
            Warning("ERROR: PERSON: US42: Error parsing GEDCOM file - Invalid Death Date for person: " + people[person]['ID'])
            return("ERROR: PERSON: US42: Error parsing GEDCOM file - Invalid Birth Date for person: "+ people[person]['ID']) 

