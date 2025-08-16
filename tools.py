from typing import Dict, Tuple, Optional

def create_table_sql(table_name: str, fields: Dict, foreign_keys=None) -> str:
    field_list = []
    for field_name, field_options in fields.items():
        field_list.append(f'{field_name} {field_options}')

    if foreign_keys:
        for fk in foreign_keys:
            field_list.append(f'FOREIGN KEY ({fk['key']}) REFERENCES {fk['ref_table']}({fk['ref_key']})')
        
    fields_and_options = ', '.join(field_list)
    return f'CREATE TABLE IF NOT EXISTS {table_name} ({fields_and_options});'

def create_insert_sql(table_name: str, fields) -> str:
    field_list = [field for field in fields]
    qmark_list = ['?' for field in fields]
    return f'INSERT INTO {table_name} ({', '.join(field_list)}) VALUES ({', '.join(qmark_list)});'

