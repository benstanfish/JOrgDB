from typing import Dict, Tuple, Optional

ANSI_ESCAPE_RESET = '\033[0m'
ANSI_ESCAPE_BOLD = '\033[1m'
ANSI_ESCAPE_FAINT = '\033[2m'
ANSI_ESCAPE_ITALIC = '\033[3m'
ANSI_ESCAPE_UNDERLINE = '\033[4m'

ANSI_ESCAPE_RED = '\033[31m'
ANSI_ESCAPE_GREEN = '\033[32m'
ANSI_ESCAPE_YELLOW = '\033[33m'
ANSI_ESCAPE_BLUE = '\033[34m'
ANSI_ESCAPE_MAGENTA = '\033[35m'
ANSI_ESCAPE_CYAN = '\033[36M'

def create_table_sql(table_name: str, fields: Dict, foreign_keys: Dict = None) -> str:
    field_list = []
    for field_name, field_options in fields.items():
        field_list.append(f'{field_name} {field_options}')

    if foreign_keys:
        for fk in foreign_keys:
            field_list.append(fk)
        
    fields_and_options = ', '.join(field_list)
    return f'CREATE TABLE IF NOT EXISTS {table_name} ({fields_and_options});'

def create_insert_sql(table_name: str, fields: Tuple) -> str:
    field_list = [field for field in fields]
    qmark_list = ['?' for field in fields]
    return f'INSERT INTO {table_name} ({', '.join(field_list)}) VALUES ({', '.join(qmark_list)});'

