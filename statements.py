# Make sure 'PRAGMA foreign_keys = ON;' in sqlite. 'PRAGMA foreign_keys;' should return 1.

org_classes = {
    'name': 'org_classes',
    'fields': {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'org_class_en': 'TEXT UNIQUE',
        'org_class_ja': 'TEXT'
    }
}

org_types = {
    'name': 'org_types',
    'fields': {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'type_ja': 'TEXT UNIQUE',
        'kana': 'TEXT',
        'type_en': 'TEXT',
        'org_class_id': 'INTEGER',
        'abbrev_ja': 'TEXT',
        'abbrev_en': 'TEXT',
        'notes': 'TEXT'
    },
    'foreign_keys': [
        {
        'key': 'org_class_id',
        'ref_table': 'org_classes',
        'ref_key': 'id'
        }
    ]
}

orgs = {
    'name': 'orgs',
    'fields': {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'friendly': 'TEXT',
        'name_en': 'TEXT',
        'name_ja': 'TEXT NOT NULL',
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



