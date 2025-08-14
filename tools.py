from typing import Dict

def create_table_sql(table_name: str, fields: Dict) -> str:
    field_list = []
    for field_name, field_options in fields.items():
        field_list.append(f'{field_name} {field_options}')

    fields_and_options = ', '.join(field_list)
    return f'CREATE TABLE IF NOT EXISTS {table_name} ({fields_and_options});'


