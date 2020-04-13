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
                    bday = None
                try:
                    people[key]['BIRT'] = datetime.strptime(people[key]['BIRT'], '%d %b %Y')

                except:
                    people[key]['validBirth'] = False
                if bday:
                    people[key]['AGE'] = int((today - bday).days / 365.2425)

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
    d_age = None
    if('DEAT' in people[key].keys()):
        # print(people[key]['DEAT'])
        # print(key, type(people[key]['DEAT']), people[key]['DEAT'])
        if(type(people[key]['DEAT']) == str):
            try:
                dday = datetime.strptime(people[key]['DEAT'], '%d %b %Y')
                people[key]['DEAT'] = datetime.strptime(people[key]['DEAT'], '%d %b %Y')
                bday = datetime.strptime(people[key]['BIRT'], '%d %b %Y')
                people[key]['BIRT'] = datetime.strptime(people[key]['BIRT'], '%d %b %Y')
                d_age = int((dday-bday).days/365.2425)
            except:
                people[key]["validDeath"] = False
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
            return("ERROR: INDIVIDUAL: US07: DEATH AGE INVALID: " + people[key]['ID'])
    if(is_dead(key, people) is False):
        if('AGE' in people[key].keys()):
            if(get_age(key, people) >= 150):
                return("ERROR: INDIVIDUAL: US07: CURRENT AGE INVALID: " + people[key]['ID'])
    
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
            try:
                familiesDT[family]['MARR'] = datetime.strptime(familiesDT[family]['MARR'], '%d %b %Y')
            except:
                families[family]['invalidMARR'] = True
        if 'DIV' in familiesDT[family]:
            try:
                familiesDT[family]['DIV'] = datetime.strptime(familiesDT[family]['DIV'], '%d %b %Y')
            except: families[family]['invalidDIV'] = True

    return familiesDT

def datesBeforeCurrent(people, families):
    output = []
    today = datetime.now()
    families_dict = convertFamiliesToDT(families)
    for person in people:
        if type(people[person].get('BIRT', None)) != str:
            if people[person].get('BIRT', today) > today:
                output.append("ERROR: INDIVIDUAL: US01 {} has a birthday ({}) after today".format(person, people[person]['BIRT']))
        if type(people[person].get('DEAT', None)) != str:
            if "DEAT" in people[person]:
                if people[person]["DEAT"] > today:
                    output.append("ERROR: INDIVIDUAL: US01 {} has died ({}) after today".format(person, people[person]['DEAT']))
    for family in families_dict:
        if type(families_dict[family].get('MARR', None)) != str:
            if families_dict[family].get('MARR', today) > today:
                output.append("ERROR: FAMILY: US01 {} family has a marriage ({}) after today".format(family, families[family]['MARR']))
        if type(families_dict[family].get('DIV', None)) != str:
            if "DIV" in families_dict[family]:
                if families_dict[family]["DIV"] > today:
                    output.append("ERROR: FAMILY: US01 {} family has a divorce ({}) after today".format(family, families[family]['DIV']))
    result = ""
    for line in output[:-1]:
        result += line + "\n"
    result += output[-1]
    return result

def listRecentBirths(people):
    thirtyDaysAgo = datetime.now() - timedelta(30)
    newly_borns = []
    for person in people:
        if('BIRT' in people[person].keys()):  
            try:
                if people[person]['BIRT'] > thirtyDaysAgo:
                    newly_borns.append(people[person]['NAME'])
                else:
                    continue
            except:
                continue
    return newly_borns

def validateDates(person, people):
    if 'validBirth' in people[person]:
        return "ERROR: INDIVIDUAL: US42: Error parsing GEDCOM file - Invalid Birth Date for person: " + person
    if (is_dead(person, people) == True):
        if 'validDeath' in people[person]:
            return ("ERROR: INDIVIDUAL: US42: Error parsing GEDCOM file - Invalid Death Date for person: " + person)
    return None

def validateFamilyDates(family, families):
    if "invalidMARR" in families[family]:
        return ("ERROR: FAMILY: US42: Error parsing GEDCOM file - Invalid Marriage Date for family: " +
                family)
    if "invalidDIV" in families[family]:
        return ("ERROR: FAMILY: US42: Error parsing GEDCOM file - Invalid Divorce Date for family: " +
                family)
    return None

    #     try:
    #         _ = datetime.strptime(people[person]['BIRT'], '%d %b %Y')
    #     except:
    #         Warning("ERROR: PERSON: US42: Error parsing GEDCOM file - Invalid Birth Date for person: " + people[person]['ID'])
    #         return("ERROR: INDIVIDUAL: US42: Error parsing GEDCOM file - Invalid Birth Date for person: " + people[person]['ID'])
    # else:
    #     try:
    #         _ = datetime.strptime(people[person]['BIRT'], '%d %b %Y')
    #     except:
    #         Warning("ERROR: PERSON: US42: Error parsing GEDCOM file - Invalid Birth Date for person: " + people[person]['ID'])
    #         return("ERROR: INDIVIDUAL: US42: Error parsing GEDCOM file - Invalid Birth Date for person: " + people[person]['ID'])
    #     try:
    #         _ = datetime.strptime(people[person]['DEAT'], '%d %b %Y')
    #     except:
    #         Warning("ERROR: PERSON: US42: Error parsing GEDCOM file - Invalid Death Date for person: " + people[person]['ID'])
    #         return("ERROR: INDIVIDUAL: US42: Error parsing GEDCOM file - Invalid Birth Date for person: " + people[person]['ID'])

def birth_before_marr_of_parents(kid,fam,people,families):
    families = convertFamiliesToDT(families)
    if('MARR' in families[fam].keys() and kid in people.keys() and people[kid]['BIRT'] - families[fam]['MARR'] < timedelta(days=0)):
        return('ERROR: FAMILY: US08: '+kid+' Birth before Marriage')
    elif('DIV' in families[fam].keys() and kid in people.keys() and people[kid]['BIRT'] - families[fam]['DIV'] > timedelta(days=90)):
        return('ERROR: FAMILY: US08: '+kid+' Birth more than 9 months after divorce')
    return

def birth_before_death_of_parents(kid,fam,people,families):
    if(is_dead(families[fam]['WIFE'], people) == True and kid in people.keys()):
        if(people[kid]['BIRT'] - people[families[fam]['WIFE']]['DEAT'] > timedelta(days=0)):
            return('ERROR: FAMILY: US09: '+kid+' Birth after death of Mother')
    elif(is_dead(families[fam]['HUSB'], people) == True and kid in people.keys()):
        if(people[kid]['BIRT'] - people[families[fam]['HUSB']]['DEAT'] > timedelta(days=90)):
            return('ERROR: FAMILY: US09: '+kid+' Birth more than 9 months after death of Father')
    return


def listRecentDeaths(people):
    thirtyDaysAgo = datetime.now() - timedelta(30)
    newly_dead = []
    for person in people:
        if('DEAT' in people[person].keys()):  
            if people[person]['DEAT'] > thirtyDaysAgo:
                newly_dead.append(people[person]['NAME'])
            else:
                continue
    return newly_dead

def listUpcomingBirthdays(people):
    # now = datetime.now()
    # thirtyDaysFuture =  now + timedelta(30)
    # upcoming_birthdays = []
    # for person in people:
    #     if('BIRT' in people[person].keys()):
    #         birthday = people[person]['BIRT'].replace(now.year)
    #         if birthday < thirtyDaysFuture:
    #             upcoming_birthdays.append(people[person]['NAME'])
    #         else:
    #             continue
    # return upcoming_birthdays

    now = datetime.now()
    thirtyDaysFuture =  now + timedelta(30)
    upcoming_birthdays = []
    for person in people:
        if('BIRT' in people[person].keys()):
            birthday = people[person]['BIRT']
            if isinstance(birthday, str):
                continue
            current_bd = datetime(now.year, birthday.month, birthday.day)
            if current_bd < thirtyDaysFuture:
                upcoming_birthdays.append(people[person]['NAME'])
            else:
                continue
    return upcoming_birthdays


def listRecentSurvivors(people, families):
    output = []
    today = datetime.now()
    for fam_id in families:
        family_list = []
        husb_id = families[fam_id].get("HUSB", None)
        wife_id = families[fam_id].get("WIFE", None)
        husb_recent = False
        if "DEAT" in people.get(husb_id, []):
            death_date = people[husb_id]['DEAT']
            # print(death_date)
            # datetime_death = datetime.strptime(death_date, '%d %b %Y')
            if death_date > today - timedelta(days=30):
                husb_recent = True
                family_list.append(families[fam_id].get("WIFE", None))
                children = families[fam_id].get('CHIL', None)
                for child in children:
                    family_list.append(child)

        if "DEAT" in people.get(wife_id, []):
            death_date = people[wife_id]['DEAT']
            # datetime_death = datetime.strptime(death_date, '%d %b %Y')
            if death_date > today - timedelta(days=30):
                family_list.append(families[fam_id].get("HUSB", None))
                if husb_recent == False:
                    children = families[fam_id].get('CHIL', None)
                    for child in children:
                        family_list.append(child)
        for survivor in family_list:
            output.append(survivor)
    return output


