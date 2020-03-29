import tag_parse as tag
import age 
#from prettytable import PrettyTable
from make_table import print_tables

# def get_vals(my_dict, header):
#     my_list = []
#     for key in my_dict:
#         if header in my_dict[key].keys():
#             my_list.append(my_dict[key][header])
#         else:
#             my_list.append('NONE')
#     return my_list

people, families = tag.read_file('./old/proj02test.ged')
people = age.store_ages(families, people)

print(people['rn'].keys())
print(families['f2'].keys())
#print(type(people['xp']['AGE']))
print()

print_tables(families, people)

# ind_table = PrettyTable()
# fam_table = PrettyTable()
# ind_headers = ['ID', 'NAME', 'SEX', 'BIRT','AGE', 'ALIVE', 'DEAT']  # 'CHILD', 'SPOUSE'
# fam_headers = ['ID', 'MARR', 'DIV', 'HUSB', 'WIFE', 'CHIL', ]

# for col in ind_headers:
#     ind_table.add_column(col, get_vals(people,col))
# print('Individuals', ind_table, sep='\n')

# for col in fam_headers:
#     fam_table.add_column(col, get_vals(families, col))
# print('Families', fam_table, sep='\n')
