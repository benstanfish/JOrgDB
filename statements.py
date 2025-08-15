# Make sure 'PRAGMA foreign_keys = ON;' in sqlite. 'PRAGMA foreign_keys;' should return 1.

users_table = {
    'name': 'users',
    'fields': {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'username': 'TEXT NOT NULL UNIQUE',
        'email': 'TEXT',
        'highscore': 'INTEGER',
        'nationality': 'TEXT'
    },
    'foreign_keys': []
}

orgs_table = {
    'name': 'orgs',
    'fields': {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'friendly': 'TEXT',
        'name_en': 'TEXT',
        'name_jp': 'TEXT NOT NULL UNIQUE',
        'org_type': 'INTEGER',
        'affix_side': 'TEXT',
        'logo_path': 'TEXT',
        'notes': 'TEXT',
        'is_inactive': 'BOOL',
    },
    'foreign_keys': [
        'FOREIGN KEY(org_type) REFERENCES org_types(id)'
    ]
}

org_types = {
    'name': 'org_types',
    'fields': {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'org_type_jp': 'TEXT',
        'org_type_en': 'TEXT',
        'abbrev_jp': 'TEXT',
        'abbrev_en': 'TEXT',
        'notes': 'TEXT'
    },
    'foreign_keys': [
        'FOREIGN KEY(org_type) REFERENCES org_types(id)'
    ]  
}

