import sqlite3
import tools

# Create in-memory database for testing
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

# Create initial table for organizations
create_users_sql = tools.create_table_sql(
    'users',
    {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'username': 'TEXT NOT NULL UNIQUE',
        'email': 'TEXT',
        'highscore': 'INTEGER',
        'nationality': 'TEXT'
    }
)

cursor.execute(create_users_sql)
connection.commit()

cursor.execute('PRAGMA table_info(users)')
for item in cursor.fetchall():
    print(item)

connection.close()