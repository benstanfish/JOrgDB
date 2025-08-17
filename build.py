import pandas as pd
import sqlite3
import tools, statements

is_localized = True
if is_localized:
    connection = sqlite3.connect('../store.db')
else:
    connection = sqlite3.connect(':memory:')

cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')

file_path = './planning/Organizations_Processing.xlsx'

# Create org_classes table and load with data

create_org_classes_sql = tools.create_table_sql(statements.org_classes)
cursor.execute(create_org_classes_sql)
connection.commit()

df_org_classes = pd.read_excel(file_path, 
                               sheet_name='org_classes', 
                               keep_default_na=False, 
                               na_values=[], 
                               )

list_of_org_classes = tools.dataframe_to_list_of_tuples(df_org_classes)
insert_org_classes_sql = tools.create_insert_sql(statements.org_classes)
cursor.executemany(insert_org_classes_sql, list_of_org_classes)
connection.commit()

# Create org_types table and load with data

create_org_types_sql = tools.create_table_sql(statements.org_types)

cursor.execute(create_org_types_sql)
connection.commit()

df_org_types = pd.read_excel(file_path, 
                             sheet_name='org_types', 
                             keep_default_na=False, 
                             na_values=[], 
                             )
list_of_org_types = tools.dataframe_to_list_of_tuples(df_org_types)
insert_org_types_sql = tools.create_insert_sql(statements.org_types)

cursor.executemany(insert_org_types_sql, list_of_org_types)
connection.commit()

# Create org table and load with data

create_orgs_sql = tools.create_table_sql(statements.orgs)

cursor.execute(create_orgs_sql)
connection.commit()

df_orgs = pd.read_excel(file_path, 
                        sheet_name='orgs', 
                        keep_default_na=False, 
                        na_values=[], 
                        )
list_of_orgs = tools.dataframe_to_list_of_tuples(df_orgs)
insert_org_types_sql = tools.create_insert_sql(statements.orgs)

cursor.executemany(insert_org_types_sql, list_of_orgs)
connection.commit()

# Create disciplines table and load with data









connection.close()

