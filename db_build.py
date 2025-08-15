import sqlite3
import pandas as pd
import tools, statements, utils

# Create in-memory database for testing
connection = sqlite3.connect(':memory:')
# connection = sqlite3.connect('./store.db')
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')

# Create initial table for organizations

create_orgs_sql = tools.create_table_sql(
    table_name=statements.orgs_table['name'],
    fields=statements.orgs_table['fields'],
    foreign_keys=statements.orgs_table['foreign_keys']
)
cursor.execute(create_orgs_sql)
connection.commit()











connection.close()