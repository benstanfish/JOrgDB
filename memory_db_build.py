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

# Insert some data to test data-entry methods
user1 = ('blaster', 'me@here.com', 10000, 'USA')
user2 = ('cutie', 'you@here.com', 500, 'Japan')
user3 = ('zero1', 'them@here.com', 3450, 'cambodia')

insert_user_sql = tools.create_insert_sql('users', ('username', 'email', 'highscore', 'nationality'))
print(insert_user_sql)

cursor.execute(insert_user_sql, user1)
cursor.execute(insert_user_sql, user2)
cursor.execute(insert_user_sql, user3)
connection.commit()


# Grab all the entries in the table see if we did it!
cursor.execute('SELECT * FROM users')
resp = cursor.fetchall()
for item in resp:
    print(item)


cursor.execute('SELECT * FROM users WHERE nationality != "USA"')
resp = cursor.fetchall()
for item in resp:
    print(item)

connection.close()