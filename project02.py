# CS555 Project02
# Author: Ryan Tom
# I pledge my honor that I have abided by the Stevens Honor System.


def strip_line(ged_line):
    return ged_line.strip('\n').split(" ")



def validate_tags(line):
    zero_tags = ["INDI",  "FAM",  "HEAD", "TRLR", "NOTE"]
    one_tags = ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"]
    two_tags = ["DATE"]

    level = line.pop(0)
    tag = line.pop(0)
    args = " ".join(line)

    if (tag == "INDI" or tag == "FAM"):
        return "<-- " + level + "|" + tag + "|N|" + args

    if ((args in zero_tags) or (args in one_tags) or (args in two_tags)):
        temp = tag
        tag = args
        args = temp

    valid = "N"
    if ((level == "0") and (tag in zero_tags)):
        valid = "Y"
    elif ((level == "1") and (tag in one_tags)):
        valid = "Y"
    elif ((level == "2") and (tag in two_tags)):
        valid = "Y"

    return "<-- " + level + "|" + tag + "|" + valid + "|" + args



if __name__ == "__main__":
    file = open('./family.ged')
    ged_lines = file.readlines()
    for ged_line in ged_lines:
        print("--> " + ged_line.strip('\n'))
        print(validate_tags(strip_line(ged_line)))
    file.close
