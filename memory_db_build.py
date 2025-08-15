import sqlite3
import tools, statements

# Create in-memory database for testing
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')

# Create initial table for organizations
create_users_sql = tools.create_table_sql(
    table_name=statements.users_table['name'],
    fields=statements.users_table['fields'],
    foreign_keys=statements.users_table['foreign_keys']
)

print(create_users_sql)
print()

create_orgs_sql = tools.create_table_sql(
    table_name=statements.orgs_table['name'],
    fields=statements.orgs_table['fields'],
    foreign_keys=statements.orgs_table['foreign_keys']
)

print(create_orgs_sql)

cursor.execute(create_users_sql)
cursor.execute(create_orgs_sql)
connection.commit()

cursor.execute('PRAGMA table_info(users)')
for item in cursor.fetchall():
    print(item)

print('-'*50)

cursor.execute('PRAGMA table_info(orgs)')
for item in cursor.fetchall():
    print(item)

print('-'*50)

# Insert some data to test data-entry methods
user1 = ('blaster', 'me@here.com', 10000, 'USA')
user2 = ('cutie', 'you@here.com', 500, 'Japan')
user3 = ('zero1', 'them@here.com', 3450, 'cambodia')

insert_user_sql = tools.create_insert_sql('users', ('username', 'email', 'highscore', 'nationality'))
print(insert_user_sql)


# cursor.execute(insert_user_sql, user1)
# cursor.execute(insert_user_sql, user2)
# cursor.execute(insert_user_sql, user3)
# connection.commit()

# Insert multiple at one time

cursor.executemany(insert_user_sql, [user1,
                                     user2,
                                     user3])
connection.commit()

# Grab all the entries in the table see if we did it!
cursor.execute('SELECT * FROM users')
resp = cursor.fetchall()
for item in resp:
    print(item)

print('-'*50)

cursor.execute('SELECT * FROM users WHERE nationality != "USA"')
resp = cursor.fetchall()
for item in resp:
    print(item)

print('-'*50)


# Use a row factory to grab column names with fetches
connection.row_factory = sqlite3.Row        # Need to create a new cursor
row_factory_cursor = connection.cursor()
row_factory_cursor.execute('SELECT * FROM users')
rows = row_factory_cursor.fetchall()
for row in rows:
    print(f'{tools.ANSI_ESCAPE_BOLD}{tools.ANSI_ESCAPE_YELLOW}{row['username']}{tools.ANSI_ESCAPE_RESET} from {tools.ANSI_ESCAPE_UNDERLINE}{tools.ANSI_ESCAPE_GREEN}{row['nationality']}{tools.ANSI_ESCAPE_RESET} has a high-score of {tools.ANSI_ESCAPE_RED}{row['highscore']}{tools.ANSI_ESCAPE_RESET}.')

connection.close()