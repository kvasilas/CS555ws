# Kirk Vasilas
# adapted from Ryan Tom
# python3.5
# to run call tag_parse.read_file('./proj02test.ged')

def strip_line(ged_line):
    return ged_line.strip('\n').split(" ")


def validate(line):
    zero_tags = ["INDI",  "FAM",  "HEAD", "TRLR", "NOTE"]
    one_tags = ["NAME", "SEX", "BIRT", "DEAT", "FAMC",
                "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"]
    two_tags = ["DATE"]

    level = line.pop(0)
    tag = line.pop(0)
    args = " ".join(line)
    status = False

    if (tag == "INDI" or tag == "FAM"):
        status = False

    if ((args in zero_tags) or (args in one_tags) or (args in two_tags)):
        temp = tag
        tag = args
        args = temp
    if ((level == "0") and (tag in zero_tags)):
        status = True
    elif ((level == "1") and (tag in one_tags)):
        status = True
    elif ((level == "2") and (tag in two_tags)):
        status = True
    return(status, tag, args)


def read_file(path):
    file = open(path)
    ged_lines=file.readlines()
    person_date_tags = ["BIRT", "DEAT"]
    fam_date_tags= ["MARR","DIV"]
    fam_flag=False
    date_type=''
    people={}
    curr_id = ""
    families={}
    for ged_line in ged_lines:
        status, tag, args = validate(strip_line(ged_line))
        if(status == True):
            if(tag == "INDI"):
                curr_id = args
                if curr_id in people:
                    people[curr_id]["isDuplicate"] = True
                else:
                    people[curr_id] = {}
                people[curr_id]["ID"] = args
                fam_flag = False

            if(tag == "NAME" or tag == "SEX"):
                people[curr_id][tag] = args

            if(tag in person_date_tags):
                date_type = tag
            if(tag == "DATE"):
                if(fam_flag == False):
                    people[curr_id][date_type] = args
                else:
                    families[curr_id][date_type] = args

            if(tag == "FAM"):
                curr_id = args
                fam_flag = True
                if curr_id in families:
                    families[curr_id]["isDuplicate"] = True
                else:
                    families[curr_id] = {}
                families[curr_id]["ID"] = args

            if(tag in fam_date_tags):
                date_type = tag
            if(tag == "HUSB" or tag == "WIFE"):
                families[curr_id][tag]=args
            if(tag == "CHIL"):
                if( tag not in families[curr_id].keys() ):
                    families[curr_id][tag] = [args]
                else:
                    families[curr_id][tag].append(args)

    file.close
    return(people, families)

    #old do not delete its good reference for now
    # print(people, families, sep='\n')
    # print(people.keys())
    # print(people['rn'].keys())
    # print("\n###  Individuals  ###")
    # for key in people:
    #     print("id =",people[key]['ID'], "| name =", people[key]['NAME'], sep=' ')
    # print("\n\n###  Families  ###")
    # for key in families:
    #     print("\nFamily =",families[key]['ID'], sep=' ')
    #     print("Husband => id =", families[key]['HUSB'],"| Name =",people[families[key]['HUSB']]['NAME'] )
    #     print("Wife => id =", families[key]['WIFE'],"| Name =", people[families[key]['WIFE']]['NAME'])

#read_file('./proj02test.ged')
#read_file('./targ.ged')
