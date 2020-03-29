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
                my_list.append(my_dict[key][header]+' ' +people[my_dict[key][header]]['NAME'])
            else:
                my_list.append(my_dict[key][header])
        elif(header == 'SPOUSE'):
            for fam in families:
                if(my_dict[key]['ID'] == families[fam]['HUSB']):
                    my_list.append(families[fam]['WIFE'])
                elif(my_dict[key]['ID'] == families[fam]['WIFE']):
                    my_list.append(families[fam]['HUSB'])
                else:
                    my_list.append('NONE')
        elif(header == 'CHILD'):
            for fam in families:
                if(my_dict[key]['ID'] == families[fam]['HUSB'] or my_dict[key]['ID'] == families[fam]['WIFE']):
                    my_list.append(families[fam]['CHIL'])
                else:
                    my_list.append('NONE')
        else:
            my_list.append('NONE')
    return my_list

def print_tables(families, people):
    ind_table = PrettyTable()
    fam_table = PrettyTable()
    ind_headers = ['ID', 'NAME', 'SEX', 'BIRT','AGE', 'ALIVE', 'DEAT', 'CHILD', 'SPOUSE']
    fam_headers = ['ID', 'MARR', 'DIV','HUSB', 'WIFE', 'CHIL']

    for col in ind_headers:
        ind_table.add_column(col, get_vals('ind', people, families, col))
    print('Individuals', ind_table, sep='\n')
    for col in fam_headers:
        fam_table.add_column(col, get_vals('fam', people, families, col))
    print('Families', fam_table, sep='\n')
