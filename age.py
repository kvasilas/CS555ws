from datetime import timedelta, datetime

def curr_age(people):
    today = datetime.now()
    for key in people:
        if('BIRT' in people[key].keys()):
            #check if dead
            print(people[key]['BIRT'])
            bday = datetime.strptime(people[key]['BIRT'], '%d %b %Y')
            print(int((today - bday).days/365.2425))

def death_age():
    pass

def marr_age():
    pass