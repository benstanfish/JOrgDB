# Make sure 'PRAGMA foreign_keys = ON;' in sqlite. 'PRAGMA foreign_keys;' should return 1.

org_types_schema = {
    'name': 'org_types',
    'fields': {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'type_ja': 'TEXT UNIQUE',
        'kana': 'TEXT',
        'type_en': 'TEXT',
        'abbrev_ja': 'TEXT',
        'abbrev_en': 'TEXT',
        'notes': 'TEXT'
    }
}

orgs_schema = {
    'name': 'orgs',
    'fields': {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'friendly': 'TEXT',
        'name_en': 'TEXT',
        'name_ja': 'TEXT NOT NULL UNIQUE',
        'org_type_id': 'INTEGER',
        'affix_side': 'TEXT',
        'logo_path': 'TEXT',
        'notes': 'TEXT',
        'is_inactive': 'BOOL',
    },
    'foreign_keys': [
        {
        'key': 'org_type_id',
        'ref_table': 'org_types',
        'ref_key': 'id'
        }
    ]
}



