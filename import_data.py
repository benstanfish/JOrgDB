import pandas as pd
import sqlite3
import tools, statements, utils

# Create in-memory database for testing
connection = sqlite3.connect(':memory:')
# connection = sqlite3.connect('../store.db')
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')

file_path = './planning/Organizations_Processing.xlsx'
df = pd.read_excel(file_path, 
                   sheet_name='org_types', 
                   keep_default_na=False, 
                   na_values=[], 
                   usecols=['type_ja','kana','type_en','abbrev_ja','abbrev_en','notes']
                   )

create_orgs_types_sql = tools.create_table_sql(
    table_name=statements.org_types_schema['name'],
    fields=statements.org_types_schema['fields']
)
cursor.execute(create_orgs_types_sql)
connection.commit()

list_of_data_as_tuples = [tuple(row) for row in df.values.tolist()]

insert_org_types_sql = tools.create_insert_sql('org_types', 
                                               ('type_ja',
                                                'kana',
                                                'type_en',
                                                'abbrev_ja',
                                                'abbrev_en',
                                                'notes'))

cursor.executemany(insert_org_types_sql, list_of_data_as_tuples)
connection.commit()

# cursor.execute('SELECT id, type_ja FROM org_types ORDER BY id ASC')
# for item in cursor.fetchall():
#     print(item)

# cursor.execute('SELECT * FROM org_types WHERE instr(abbrev_ja, "K") > 0')
# for item in cursor.fetchall():
#     print(item)