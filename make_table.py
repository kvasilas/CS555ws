from prettytable import PrettyTable

def get_vals(my_dict, header):
    my_list = []
    for key in my_dict:
        if header in my_dict[key].keys():
            # if(header == 'WIFE' or header == 'HUSB'):
            #     my_list.append(my_dict[key][header]+' '+people[my_dict[key]['NAME'])
            # else:
            #    my_list.append(my_dict[key][header])
            my_list.append(my_dict[key][header])
        else:
            my_list.append('NONE')
    return my_list

def print_tables(families, people):
    ind_table = PrettyTable()
    fam_table = PrettyTable()
    ind_headers = ['ID', 'NAME', 'SEX', 'BIRT', 'AGE', 'ALIVE', 'DEAT']  # 'CHILD', 'SPOUSE'
    fam_headers = ['ID', 'MARR', 'DIV', 'HUSB', 'WIFE', 'CHIL', ]

    for col in ind_headers:
        ind_table.add_column(col, get_vals(people, col))
    print('Individuals', ind_table, sep='\n')
    for col in fam_headers:
        fam_table.add_column(col, get_vals(families, col))
    print('Families', fam_table, sep='\n')
