import pandas as pd
import sqlite3
import tools, statements, utils
from PIL import Image

# Create in-memory database for testing
is_localized = False
if is_localized:
    connection = sqlite3.connect('../store.db')
else:
    connection = sqlite3.connect(':memory:')
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')

file_path = './planning/Organizations_Processing.xlsx'

create_org_classes_sql = tools.create_table_sql(statements.org_classes)
cursor.execute(create_org_classes_sql)
connection.commit()

df_org_classes = pd.read_excel(file_path, 
                               sheet_name='org_classes', 
                               keep_default_na=False, 
                               na_values=[], 
                               )

# print(df_org_classes.columns[0])
# for row in df_org_classes.iloc[:, 1:].values.tolist():
#     print(row)


list_of_org_classes = tools.dataframe_to_list_of_tuples(df_org_classes)
insert_org_classes_sql = tools.create_insert_sql(statements.org_classes)

print(list_of_org_classes)
print(insert_org_classes_sql)
cursor.executemany(insert_org_classes_sql, list_of_org_classes)
connection.commit()

# df_org_types = pd.read_excel(file_path, 
#                    sheet_name='org_types', 
#                    keep_default_na=False, 
#                    na_values=[], 
#                    usecols=['type_ja','kana','type_en','abbrev_ja','abbrev_en','notes']
#                    )

# Create org_types table and insert data

create_org_types_sql = tools.create_table_sql(statements.org_types)
# create_orgs_types_sql = tools.create_table_sql_verbose(
#     table_name=statements.org_types['name'],
#     fields=statements.org_types['fields']
# )
print(create_org_types_sql)
cursor.execute(create_org_types_sql)
connection.commit()

df_org_types = pd.read_excel(file_path, 
                             sheet_name='org_types', 
                             keep_default_na=False, 
                             na_values=[], 
                             )
# list_of_data_as_tuples = [tuple(row) for row in df_org_types.iloc[:, 2:].values.tolist()]

list_of_org_types = tools.dataframe_to_list_of_tuples(df_org_types)

# column_names = df_org_types.columns.tolist()

# insert_org_types_sql = tools.create_insert_sql('org_types', 
#                                                ('type_ja',
#                                                 'kana',
#                                                 'type_en',
#                                                 'abbrev_ja',
#                                                 'abbrev_en',
#                                                 'notes'))

# insert_org_types_sql = tools.create_insert_sql('org_types', 
#                                                column_names)

insert_org_types_sql = tools.create_insert_sql(statements.org_types)
print(insert_org_types_sql)

cursor.executemany(insert_org_types_sql, list_of_org_types)
connection.commit()

# cursor.execute('SELECT id, type_ja FROM org_types ORDER BY id ASC')
# for item in cursor.fetchall():
#     print(item)

# cursor.execute('SELECT * FROM org_types WHERE instr(abbrev_ja, "K") > 0')
# for item in cursor.fetchall():
#     print(item)

# Create orgs table and insert data

# create_orgs_sql = tools.create_table_sql_verbose(
#     table_name=statements.orgs['name'],
#     fields=statements.orgs['fields'],
#     foreign_keys=statements.orgs['foreign_keys']
# )

create_orgs_sql = tools.create_table_sql(statements.orgs)

cursor.execute(create_orgs_sql)
connection.commit()

df_orgs = pd.read_excel(file_path, 
                        sheet_name='orgs', 
                        keep_default_na=False, 
                        na_values=[], 
                        )
list_of_orgs = tools.dataframe_to_list_of_tuples(df_orgs)
# column_names = df_orgs.columns.tolist()

# insert_org_types_sql = tools.create_insert_sql_verbose('orgs', column_names)
insert_org_types_sql = tools.create_insert_sql(statements.orgs)

cursor.executemany(insert_org_types_sql, list_of_orgs)
connection.commit()

# cursor.execute('SELECT * FROM orgs')
# for item in cursor.fetchmany(10):
#     print(item)

left_join_sql = """
    SELECT name_ja, org_types.type_ja, logo_path FROM orgs
    LEFT JOIN org_types
    ON orgs.org_type_id = org_types.id
    WHERE org_types.type_ja = "一般財団法人"
"""


cursor.execute(left_join_sql)
resp = cursor.fetchall();
# for item in resp:
#     # img_path = './img/'+ item[2]
#     # with Image.open(img_path) as img:
#     #     img.show()
    

print(type(resp))
nihon = [entity for entity in resp if '日本' in entity[0]]
for item in nihon:
    print(item)

compound_left_join_sql = """
    SELECT orgs.name_ja, org_types.type_en 
    FROM orgs
    LEFT JOIN org_types ON orgs.org_type_id = org_types.id
    LEFT JOIN org_classes ON org_types.org_class_id = org_classes.id
    WHERE org_classes.org_class_en = "private" AND instr(org_types.type_ja,"一般") > 0
"""

cursor.execute(compound_left_join_sql)
resp2 = cursor.fetchall();
for item in resp2:
    print(item)