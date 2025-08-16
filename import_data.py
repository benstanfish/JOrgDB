import pandas as pd
import sqlite3
import tools, statements, utils
from PIL import Image

# Create in-memory database for testing
connection = sqlite3.connect(':memory:')
# connection = sqlite3.connect('../store.db')
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')

file_path = './planning/Organizations_Processing.xlsx'
# df_org_types = pd.read_excel(file_path, 
#                    sheet_name='org_types', 
#                    keep_default_na=False, 
#                    na_values=[], 
#                    usecols=['type_ja','kana','type_en','abbrev_ja','abbrev_en','notes']
#                    )

# Create org_types table and insert data


create_orgs_types_sql = tools.create_table_sql(
    table_name=statements.org_types_schema['name'],
    fields=statements.org_types_schema['fields']
)
cursor.execute(create_orgs_types_sql)
connection.commit()

df_org_types = pd.read_excel(file_path, 
                             sheet_name='org_types', 
                             keep_default_na=False, 
                             na_values=[], 
                             )
list_of_data_as_tuples = [tuple(row) for row in df_org_types.values.tolist()]
column_names = df_org_types.columns.tolist()

# insert_org_types_sql = tools.create_insert_sql('org_types', 
#                                                ('type_ja',
#                                                 'kana',
#                                                 'type_en',
#                                                 'abbrev_ja',
#                                                 'abbrev_en',
#                                                 'notes'))

insert_org_types_sql = tools.create_insert_sql('org_types', 
                                               column_names)

cursor.executemany(insert_org_types_sql, list_of_data_as_tuples)
connection.commit()

# cursor.execute('SELECT id, type_ja FROM org_types ORDER BY id ASC')
# for item in cursor.fetchall():
#     print(item)

# cursor.execute('SELECT * FROM org_types WHERE instr(abbrev_ja, "K") > 0')
# for item in cursor.fetchall():
#     print(item)




# Create orgs table and insert data
create_orgs_sql = tools.create_table_sql(
    table_name=statements.orgs_schema['name'],
    fields=statements.orgs_schema['fields'],
    foreign_keys=statements.orgs_schema['foreign_keys']
)
cursor.execute(create_orgs_sql)
connection.commit()

df_orgs = pd.read_excel(file_path, 
                        sheet_name='orgs', 
                        keep_default_na=False, 
                        na_values=[], 
                        )
list_of_data_as_tuples = [tuple(row) for row in df_orgs.values.tolist()]
column_names = df_orgs.columns.tolist()

insert_org_types_sql = tools.create_insert_sql('orgs', 
                                               column_names)

cursor.executemany(insert_org_types_sql, list_of_data_as_tuples)
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
    

# print(type(resp))
# nihon = [entity for entity in resp if '日本' in entity[0]]
# for item in nihon:
#     print(item)