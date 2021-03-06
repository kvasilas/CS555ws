from prettytable import PrettyTable

def get_vals(curr_dict, people, families, header):
    my_list = []
    if curr_dict == 'fam':
        my_dict = families
    else:
        my_dict = people
    for key in my_dict:
        if header in my_dict[key].keys():
            if(header == 'WIFE' or header == 'HUSB'):
                tmp_append = my_dict[key][header]
                ind_id = people.get(my_dict[key][header], None)
                if ind_id != None:
                    ind_id = ind_id.get("NAME", "N/A")
                else:
                    ind_id = "N/A"
                my_list.append(str(tmp_append) + " " + ind_id)
            else:
                my_list.append(my_dict[key][header])
        elif(header == 'SPOUSE'):
            count = 0
            for fam in families:
                if (my_dict[key]['ID'] == families[fam].get('HUSB', False)):
                    my_list.append(families[fam]['WIFE'])
                    break
                elif (my_dict[key]['ID'] == families[fam].get('WIFE', False)):
                    my_list.append(families[fam]['HUSB'])
                    break
                else:
                    if(count == len(families.keys())-1):
                        my_list.append('NONE')
                    else:
                        count += 1
        elif(header == 'CHILD'):
            count=0
            for fam in families:
                if(my_dict[key]['ID'] == families[fam].get('HUSB', False) or my_dict[key]['ID'] == families[fam].get('WIFE', False)):
                    if 'CHIL' in families[fam].keys():
                        my_list.append(families[fam]['CHIL'])
                    else:
                        my_list.append('NONE')
                    break
                else:
                    if( count == len(families.keys())-1 ):
                        my_list.append('NONE')
                    else:
                        count+=1
        else:
            my_list.append('NONE')
    return my_list

def print_tables(families, people):
    ind_table = PrettyTable()
    fam_table = PrettyTable()
    ind_headers = ['ID', 'NAME', 'SEX', 'BIRT','AGE', 'ALIVE', 'DEAT', 'CHILD', 'SPOUSE']
    fam_headers = ['ID', 'MARR', 'DIV','HUSB', 'WIFE', 'CHIL']

    for col in ind_headers:
        #print(get_vals('ind', people, families, col))
        ind_table.add_column(col, get_vals('ind', people, families, col))
    print('Individuals', ind_table, sep='\n')
    for col in fam_headers:
        fam_table.add_column(col, get_vals('fam', people, families, col))
    print('Families', fam_table, sep='\n')
