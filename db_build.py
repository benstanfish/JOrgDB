import sqlite3
import pandas as pd
import tools, statements, utils

connection = sqlite3.connect(':memory:')
# connection = sqlite3.connect('./store.db')
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')

create_orgs_sql = tools.create_table_sql(
    table_name=statements.orgs_schema['name'],
    fields=statements.orgs_schema['fields'],
    foreign_keys=statements.orgs_schema['foreign_keys']
)
cursor.execute(create_orgs_sql)
connection.commit()

cursor.execute('SELECT * FROM orgs')
for item in cursor.fetchall():
    print(item)



connection.close()
print('Connection closed.')